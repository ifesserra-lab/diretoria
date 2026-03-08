import subprocess
import json
import pandas as pd
from pathlib import Path
from datetime import datetime

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

def update_monthly_log(issues):
    """Atualiza o arquivo Markdown mensal com as atividades."""
    now = datetime.now()
    month_str = now.strftime("%Y-%m")
    month_name = now.strftime("%B/%Y") # Ex: March/2026
    log_file = ACTIVITIES_DIR / f"{month_str}-atividades.md"
    
    # Se não existe, inicia com o modelo
    if not log_file.exists() and TEMPLATE_FILE.exists():
        content = TEMPLATE_FILE.read_text()
        content = content.replace("[MÊS/ANO]", month_name)
    else:
        # Para simplificar, vamos reconstruir as seções de atividades
        # mas manter o cabeçalho se o arquivo já existir
        content = TEMPLATE_FILE.read_text().replace("[MÊS/ANO]", month_name)

    # Contagem estatística
    total_closed = len([i for i in issues if i['state'] == "CLOSED"])
    
    # Substituir resumo
    content = content.replace("Total de Issues Concluídas: 0", f"Total de Issues Concluídas: {total_closed}")
    
    # Agrupar por área para o Markdown
    for area in AREAS:
        area_issues = []
        for issue in issues:
            is_in_area = any(l['name'] == area for l in issue['labels'])
            if is_in_area:
                link = f"[#{issue['number']}]({issue['url']})"
                area_issues.append(f"- {link} - {issue['title']} (Status: {issue['state']})")
        
        placeholder = f"### {area}\n- [ISSUE #ID] - Descrição breve da entrega."
        if area == "Gestão":
            placeholder = f"### Gestão (DPPGE)\n- [ISSUE #ID] - Descrição breve da entrega."
            
        if area_issues:
            new_section = f"### {area if area != 'Gestão' else 'Gestão (DPPGE)'}\n" + "\n".join(area_issues)
            content = content.replace(placeholder, new_section)

    log_file.write_to_file(content, overwrite=True)
    print(f"Log mensal atualizado em {log_file}")

if __name__ == "__main__":
    issues = get_gh_issues()
    if issues:
        sync_csv(issues)
        # update_monthly_log(issues) # Comentado até resolver o método write_to_file do Path ou similar
        
        # Correção simples para escrita de arquivo
        now = datetime.now()
        month_str = now.strftime("%Y-%m")
        log_file = ACTIVITIES_DIR / f"{month_str}-atividades.md"
        
        # (Lógica de montagem de conteúdo repetida para o script final funcional)
        def generate_content(issues, month_name):
            template_content = TEMPLATE_FILE.read_text()
            content = template_content.replace("[MÊS/ANO]", month_name)
            total_closed = len([i for i in issues if i['state'] == "CLOSED"])
            content = content.replace("Total de Issues Concluídas: 0", f"Total de Issues Concluídas: {total_closed}")
            
            for area in AREAS:
                area_issues = []
                for issue in issues:
                    is_in_area = any(l['name'] == area for l in issue['labels'])
                    if is_in_area:
                        link = f"[#{issue['number']}]({issue['url']})"
                        status_emoji = "✅" if issue['state'] == "CLOSED" else "⏳"
                        area_issues.append(f"- {link} - {issue['title']} ({status_emoji})")
                
                # Mapeamento do template (usando busca por texto parcial para ser mais robusto)
                if area == "Pesquisa":
                    target = "### 🔬 Pesquisa\n- [ISSUE #ID] - Descrição breve da entrega."
                elif area == "Extensão":
                    target = "### 🚀 Extensão\n- [ISSUE #ID] - Descrição breve da entrega."
                elif area == "Gestão":
                    target = "### 🏛️ Gestão (DPPGE)\n- [ISSUE #ID] - Descrição breve da entrega."
                
                if area_issues:
                    replacement = target.split('\n')[0] + "\n" + "\n".join(area_issues)
                    content = content.replace(target, replacement)
            return content

        final_content = generate_content(issues, now.strftime("%B/%Y"))
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(final_content)
        print(f"Log mensal atualizado em {log_file}")
