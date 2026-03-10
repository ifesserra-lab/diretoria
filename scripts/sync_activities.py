import subprocess
import json
import pandas as pd
from pathlib import Path
from datetime import datetime
import re

# Configurações de caminhos
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "tasks.csv"
ACTIVITIES_DIR = BASE_DIR / "docs" / "atividades"
TEMPLATE_FILE = ACTIVITIES_DIR / "modelo-atividades.md"

AREAS = ["Pesquisa", "Extensão", "Gestão"]

def get_gh_issues():
    """Busca issues do GitHub com as labels de interesse."""
    cmd = [
        "gh", "issue", "list",
        "--repo", "ifesserra-lab/diretoria",
        "--limit", "100",
        "--state", "all",
        "--json", "number,title,state,labels,assignees,closedAt,url"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Erro ao buscar issues: {result.stderr}")
        return []
    return json.loads(result.stdout)

def sync_csv(issues):
    """Atualiza o arquivo data/tasks.csv com base nas issues."""
    rows = []
    for issue in issues:
        # Identificar área pela label
        area = "Geral"
        for label in issue['labels']:
            if label['name'] in AREAS:
                area = label['name']
                break
        
        assignee = issue['assignees'][0]['login'] if issue['assignees'] else "N/A"
        closed_at = issue['closedAt'].split('T')[0] if issue['closedAt'] else ""
        
        status = "Concluído" if issue['state'] == "CLOSED" else "Em andamento"
        
        rows.append({
            "title": issue['title'],
            "status": status,
            "area": area,
            "responsavel": assignee,
            "closed_at": closed_at
        })
    
    df = pd.DataFrame(rows)
    df.to_csv(DATA_FILE, index=False)
    print(f"CSV atualizado em {DATA_FILE}")

def get_existing_manual_entries(log_file, area_title):
    """Recupera entradas manuais iterando pelas linhas após o título da seção até a próxima."""
    if not log_file.exists():
        return []
        
    lines = log_file.read_text().splitlines()
    manual_entries = []
    in_section = False
    
    for line in lines:
        if line.startswith("### "):
            in_section = (line.strip() == area_title)
            continue
        elif line.startswith("## ") and in_section:
            break
            
        if in_section and line.startswith("- "):
            # Se não é uma issue do Github, consideramos manual
            if "github.com" not in line and "[ISSUE #ID]" not in line:
                manual_entries.append(line)
                
    return manual_entries

if __name__ == "__main__":
    issues = get_gh_issues()
    if issues:
        sync_csv(issues)
        
        now = datetime.now()
        month_str = now.strftime("%Y-%m")
        log_file = ACTIVITIES_DIR / f"{month_str}-atividades.md"
        
        def generate_content(issues, month_name):
            template_content = TEMPLATE_FILE.read_text()
            content = template_content.replace("[MÊS/ANO]", month_name)
            total_closed = len([i for i in issues if i['state'] == "CLOSED"])
            content = content.replace("Total de Issues Concluídas: 0", f"Total de Issues Concluídas: {total_closed}")
            
            # Map of area headers
            area_headers = {
                "Pesquisa": "### 🔬 Pesquisa",
                "Extensão": "### 🚀 Extensão",
                "Gestão": "### 🏛️ Gestão (DPPGE)"
            }
            
            for area in AREAS:
                target_header = area_headers[area]
                
                # 1. Fetch GH Issues for this area
                area_issues = []
                for issue in issues:
                    is_in_area = any(l['name'] == area for l in issue['labels'])
                    if is_in_area:
                        link = f"[#{issue['number']}]({issue['url']})"
                        status_emoji = "✅" if issue['state'] == "CLOSED" else "⏳"
                        area_issues.append(f"- {link} - {issue['title']} ({status_emoji})")
                
                # 2. Fetch manual lines already in the file for this area
                manual_entries = get_existing_manual_entries(log_file, target_header)
                if manual_entries:
                    area_issues.extend(manual_entries)
                
                # 3. Replace template section
                target_template_block = f"{target_header}\n- [ISSUE #ID] - Descrição breve da entrega."
                if area == "Pesquisa":
                    target_template_block += "\n- [Atividade Ad-hoc] - Descrição de algo não planejado que foi executado."
                
                if area_issues:
                    replacement = target_header + "\n" + "\n".join(area_issues)
                    content = content.replace(target_template_block, replacement)
                    
            return content

        final_content = generate_content(issues, now.strftime("%B/%Y"))
        
        # Preserve observations block if they were edited
        if log_file.exists():
            old_lines = log_file.read_text().splitlines()
            old_obs_idx = -1
            for i, line in enumerate(old_lines):
                if line.startswith("## 📈 Observações e Destaques"):
                    old_obs_idx = i
                    break
            
            if old_obs_idx != -1:
                # Find the footer
                footer_idx = -1
                for i in range(old_obs_idx, len(old_lines)):
                    if old_lines[i] == "---":
                        footer_idx = i
                        break
                
                if footer_idx != -1:
                    old_obs_block = "\n".join(old_lines[old_obs_idx:footer_idx])
                    
                    # Target default observations from template in new content to replace
                    default_obs_block = "## 📈 Observações e Destaques\n- (Espaço para comentar marcos importantes ou impedimentos do mês)\n"
                    if default_obs_block in final_content:
                        final_content = final_content.replace(default_obs_block, old_obs_block + "\n")
                    
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(final_content)
        print(f"Log mensal atualizado em {log_file}")
