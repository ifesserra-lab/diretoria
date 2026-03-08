# 🏛️ IFES Serra - DPPGE (GitOps para Governança)

Este repositório é a **Fonte Única de Verdade (SSOT)** para a gestão da Diretoria de Pesquisa, Pós-Graduação e Extensão (DPPGE) do IFES Campus Serra. Utilizamos o princípio de GitOps para garantir rastreabilidade, transparência e automação em todos os processos de governança.

---

## 📅 Atalhos Rápidos

- 🗓️ **[Calendário de Reuniões 2026](file:///home/paulossjunior/projects/diretoria/docs/pautas/calendario-reunioes-2026.md)** (Quinzenal/Sextas)
- 📜 **[Última Ata (2026-02-27)](file:///home/paulossjunior/projects/diretoria/docs/atas/2026-02-27-planejamento-dppge.md)**
- ⚖️ **[Registro de Decisões Formalizadas](file:///home/paulossjunior/projects/diretoria/docs/decisoes/001-diretrizes-planejamento-dppge.md)**
- 📊 **[GitHub Project #7](https://github.com/orgs/ifesserra-lab/projects/7)** (Gestão de Tarefas)

---

## 📂 Estrutura do Ecossistema

- `docs/atas/` : Registros cronológicos de todas as reuniões.
- `docs/decisoes/` : Documentos de decisões formais (ADR - Architecture/Action Decision Records).
- `docs/pautas/` : Planejamento de reuniões e calendário anual.
- `docs/dashboards/` : Indicadores automáticos e gráficos de desempenho.
- `docs/relatorios/` : Consolidados mensais e trimestrais.
- `.agent/` : Inteligência e automação (Workflows e Skills do Agente).

---

## 👥 Equipe Gestora

| Nome | Área | Papel | E-mail |
| :--- | :--- | :--- | :--- |
| **Paulo Sérgio Jr.** | Geral | Diretor | [E-mail](mailto:paulossjunior@ifes.edu.br) |
| **Richard Godinez** | Pesquisa | Coordenador | [E-mail](mailto:richard@ifes.edu.br) |
| **Celio Maioli** | Extensão | Coordenador | [E-mail](mailto:cpmaioli@ifes.edu.br) |
| **Julia** | Apoio | Técnica | - |

---

## ⚙️ Automação e Fluxo

Para manter a governança ágil, utilizamos o comando especializado do Agente:

### `/governance-flow`
Este comando automatiza o ciclo de vida de uma reunião:
1. **Rascunho**: Gera a ata baseada no modelo oficial.
2. **Issues**: Extrai tarefas e cria Issues automaticamente no GitHub.
3. **Draft**: Pede aprovação antes de persistir ou fazer push.

### `/activity-log`
Utilizado para registro de atividades ad-hoc e demandas fora de reunião:
1. **Log**: Atualiza o arquivo mensal em `docs/atividades/`.
2. **Task**: Cria a Issue correspondente se a atividade for "Para Fazer".
3. **Draft**: Pede aprovação antes de persistir ou fazer push.

#### Como Contribuir:
- **Tarefas**: Abra uma Issue usando o template de `Tarefa`.
- **Pautas**: Sugira tópicos criando um arquivo em `docs/pautas/`.
- **Decisões**: Novas diretrizes passam por Pull Request na pasta `docs/decisoes/`.

---
*Atualizado em: 2026-03-08 | Diretoria do IFES Campus Serra.*
