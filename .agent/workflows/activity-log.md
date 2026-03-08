---
description: Workflow para registro de atividades ad-hoc, criação de tarefas e atualização do log mensal.
---

Este workflow simplifica o registro de atividades que surgem no dia a dia, garantindo que elas virem Issues no GitHub e sejam registradas no log de estatísticas mensal.

### Comandos:
- `/record-activity`: Registra uma nova atividade, cria a Issue e atualiza o arquivo mensal.

### Passo a Passo:

1. **Coleta de Informações**:
   - Descrição da atividade/tarefa.
   - Área (Pesquisa, Extensão, Gestão).
   - Status: "Para Fazer" (Cria Issue) ou "Concluída" (Apenas registra no log).

2. **Criação de Task (Se aplicável)**:
   - Se o status for "Para Fazer", utilize a skill `github-issue-creator` para gerar a Issue.
   - Capture o número da Issue (#ID).

3. **Atualização do Log Mensal**:
   - Verifique se o arquivo do mês atual existe em `docs/atividades/YYYY-MM-atividades.md`.
   - Se não existir, crie-o usando o `modelo-atividades.md`.
   - Adicione a atividade na seção correspondente à Área.
   - Se for uma Issue, inclua o link `[#ID](...)`.
   - **Peça aprovação do rascunho da atualização antes de salvar.**

4. **Sincronização**:
   - Realize o commit e push com a confirmação do usuário.

---
> [!TIP]
> Use este workflow para "Aprovações Emergenciais" ou tarefas rápidas que não passaram por uma ata de reunião formal.
