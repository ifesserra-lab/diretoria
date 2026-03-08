---
description: Workflow para redação de atas e criação de tarefas (GitOps para Governança)
---

Este workflow orienta o agente na criação de atas de reunião e na sincronização de tarefas com o GitHub, garantindo que o usuário valide cada etapa.

## Regra de Ouro
**Sempre pergunte e aguarde a aprovação do usuário antes de realizar qualquer ação persistente (salvar arquivos, criar issues, fazer commit/push).**

## Fluxo de Execução

### 1. Coleta de Informações
O agente deve solicitar ao usuário os dados básicos da reunião:
- Data
- Participantes
- Tópicos discutidos (Pauta)
- Principais decisões (Deliberações)

### 2. Rascunho da Ata
- O agente gera um rascunho em Markdown baseado no `docs/atas/modelo-ata.md`.
- **Ação:** Apresentar o rascunho ao usuário.
- **Pergunta:** "O rascunho da ata está correto? Posso salvá-lo em `docs/atas/`?"

### 3. Registro do Arquivo
- Após aprovação, o agente salva o arquivo em `docs/atas/YYYY-MM-DD-reuniao.md`.
- **Ação:** Informar ao usuário que o arquivo foi salvo.

### 4. Sincronização de Tarefas (Issues)
- O agente extrai as tarefas da seção `## 3. Plano de Ações (Issues)`.
- O agente deve listar as tarefas identificadas e seus metadados (Responsável, Área, Prioridade, Prazo).
- **Pergunta:** "Identifiquei as seguintes tarefas. Posso criar as Issues no GitHub e adicioná-las ao Project #7?"

### 5. Criação e Atualização
- Após aprovação, o agente cria as Issues via CLI/API.
- O agente atualiza o arquivo da ata com os links das Issues criadas.
- **Ação:** Apresentar o resumo das Issues criadas.

### 6. Publicação (Commit/Push)
- **Pergunta:** "Posso realizar o commit e push das alterações para o repositório remoto?"

## Comandos Úteis
- Iniciar o fluxo: `/governance-flow`
