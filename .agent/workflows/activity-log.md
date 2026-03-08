---
description: Workflow para criação de atividades ad-hoc e lançamento no GitHub.
---

Este workflow orienta o agente na criação de novas atividades/tarefas diretamente no GitHub, garantindo a formatação correta para que a automação diária as processe nos relatórios.

### Comandos:
- `/activity-log`: Registra uma nova demanda e cria a Issue correspondente.

### Passo a Passo:

1. **Coleta de Informações**:
   - Título da atividade.
   - Responsável (ex: @paulo, @celio, @richard).
   - Área (**Pesquisa**, **Extensão**, ou **Gestão**).
   - Prazo (opcional).

2. **Lançamento no GitHub**:
   - Use a skill `github-issue-creator` para gerar a Issue.
   - Adicione obrigatoriamente as labels: `tarefa` + a área correspondente (`Pesquisa`, `Extensão` ou `Gestão`).
   - Garanta que o corpo da Issue siga o padrão de governança.

3. **Confirmação**:
   - Informe ao usuário o número da Issue criada (#ID).
   - **Nota Importante**: Informe que o arquivo em `docs/atividades/` será atualizado automaticamente pela automação diária (GitHub Action), não sendo necessária atualização manual neste momento.

---
> [!NOTE]
> Este fluxo prioriza o registro no GitHub. O agrupamento estatístico e documental é feito via script automatizado (`sync_activities.py`).
