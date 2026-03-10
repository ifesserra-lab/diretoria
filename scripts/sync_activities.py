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
        "--json", "number,title,state,labels,assignees,createdAt,closedAt,url,body,comments"
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
            
        if in_section:
            line_str = line.strip()
            # Ignorar cabeçalhos de tabela e linhas vazias
            if not line_str or "---|---" in line_str or "| Tarefa | Descrição |" in line_str:
                continue
                
            if line_str.startswith("- ") or line_str.startswith("| "):
                # Se não é uma issue do Github, consideramos manual
                if "github.com" not in line_str and "[ISSUE #ID]" not in line_str:
                    manual_entries.append(line_str)
                
    return manual_entries

if __name__ == "__main__":
    issues = get_gh_issues()
    if issues:
        sync_csv(issues)
        
        now = datetime.now()
        current_month_str = now.strftime("%Y-%m")
        
        # Mapeamento simples de meses (opcional, pode usar locale mas isso é seguro)
        months_pt = {
            "01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril",
            "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto",
            "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"
        }
        
        def generate_content(file_issues, month_name, log_file):
            template_content = TEMPLATE_FILE.read_text()
            content = template_content.replace("[MÊS/ANO]", month_name)
            total_closed = len([i for i in file_issues if i.get('state') == "CLOSED"])
            content = content.replace("**Total de Issues Concluídas:** 0", f"**Total de Issues Concluídas:** {total_closed}")
            
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
                for issue in file_issues:
                    is_in_area = any(l['name'] == area for l in issue['labels'])
                    if is_in_area:
                        link = f"[#{issue['number']}]({issue['url']})"
                        status_emoji = "✅" if issue['state'] == "CLOSED" else "⏳"
                        
                        title = issue['title'].replace('|', '&#124;')
                        body = issue.get('body', '') or ''
                        body_lines = [line.strip() for line in body.split('\n') if line.strip() and not line.startswith('#')]
                        desc = body_lines[0] if body_lines else ""
                        desc = (desc[:60] + '...') if len(desc) > 60 else desc
                        desc = desc.replace('|', '&#124;')
                        
                        responsavel = issue['assignees'][0]['login'] if issue.get('assignees') else "N/A"
                        abertura = issue.get('createdAt', '').split('T')[0] if issue.get('createdAt') else ""
                        fechamento = issue.get('closedAt', '').split('T')[0] if issue.get('closedAt') else "-"
                        
                        detalhes = []
                        comments = issue.get('comments', [])
                        if comments:
                            last_comment = comments[-1]['body']
                            last_comment_clean = last_comment.replace('\n', ' ').replace('\r', '').replace('|', '&#124;')
                            last_comment_clean = (last_comment_clean[:80] + '...') if len(last_comment_clean) > 80 else last_comment_clean
                            detalhes.append(f"**Último comentário:** {last_comment_clean}")
                        
                        detalhes_str = "<br>".join(detalhes) if detalhes else "-"
                        
                        row = f"| {link} - {title} | {desc} | @{responsavel} | {abertura} | {fechamento} | {status_emoji} | {detalhes_str} |"
                        area_issues.append(row)
                
                # 2. Fetch manual lines already in the file for this area
                manual_entries = get_existing_manual_entries(log_file, target_header)
                if manual_entries:
                    for entry in manual_entries:
                        if entry.startswith("|"):
                            # Se por acaso o script encontrou uma tabela, tentamos só reutilizar preservando-o (fallback) ou ignorar pois vai ser recriada
                            pass 
                        else:
                            clean_entry = entry.removeprefix("- ").strip().replace('|', '&#124;')
                            row = f"| {clean_entry} | - | Manual | - | - | ⏳ | - |"
                            area_issues.append(row)
                
                # 3. Replace template section
                target_template_block = f"{target_header}\n- [ISSUE #ID] - Descrição breve da entrega."
                if area == "Pesquisa":
                    target_template_block += "\n- [Atividade Ad-hoc] - Descrição de algo não planejado que foi executado."
                
                if area_issues:
                    table_header = "| Tarefa | Descrição | Responsável | Abertura | Fechamento | Status | Outros Detalhes |\n|---|---|---|---|---|:---:|---|"
                    replacement = target_header + "\n\n" + table_header + "\n" + "\n".join(area_issues)
                    content = content.replace(target_template_block, replacement)
                    
            return content

        for log_file in ACTIVITIES_DIR.glob("*-atividades.md"):
            if "modelo" in log_file.name: continue
            
            # Obter mês e ano do arquivo (ex: 2026-03)
            file_month_str = log_file.name[:7]
            year = file_month_str[:4]
            month = file_month_str[5:7]
            month_name_pt = f"{months_pt.get(month, month)}/{year}"

            # Extrair issue ID numbers que já estão neste arquivo para não perder histórico
            existing_content = log_file.read_text()
            existing_issue_numbers = set(int(m) for m in re.findall(r'\[#(\d+)\]', existing_content))
            
            # Definir quais issues irão para este log
            file_issues = []
            for issue in issues:
                # Se a issue já estava no markdwon antigo, ela pertence a este mês
                if issue['number'] in existing_issue_numbers:
                    file_issues.append(issue)
                # Se for o arquivo do mês atual, adiciona as issues criadas ou fechadas no mês atual, ou abertas
                elif file_month_str == current_month_str:
                    file_issues.append(issue)
            
            # Remover duplicatas mantendo a ordem para o current_month_str
            seen = set()
            file_issues_unique = []
            for i in file_issues:
                if i['number'] not in seen:
                    seen.add(i['number'])
                    file_issues_unique.append(i)

            final_content = generate_content(file_issues_unique, month_name_pt, log_file)
            
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
            print(f"Log mensal atualizado em {log_file.name}")
