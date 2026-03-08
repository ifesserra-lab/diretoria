# Agent Skills: Governance and GitOps

## Core Governance Skills

- **Meeting Minutes (Atas)**: Skilled in generating meeting minutes in Markdown format.
    - **Target Directory**: `docs/atas/`
    - **Naming Convention**: `YYYY-MM-DD-meeting-name.md`
    - **Content Requirements**: Date, participants, agenda, deliberations, and a checklist of actions.

- **Formal Decisions**: Skilled in documenting significant governance decisions.
    - **Target Directory**: `docs/decisoes/`
    - **Naming Convention**: `NNN-decision-description.md`
    - **Content Requirements**: Context, the decision itself, responsibles, and the effective date.

- **Task Management**: Skilled in task orchestration using GitHub Issues and Projects.
    - **Workflow**: Create Issues using specific templates.
    - **Tracking**: Monitor in GitHub Projects ([Diretoria - Governança #7](https://github.com/orgs/ifesserra-lab/projects/7)) with custom fields: `Status`, `Area`, `Responsible`, `Priority`, `Deadline`, and `Origin`.

- **Dashboards and Indicators**: Skilled in automated reporting and visualization.
    - **Visuals**: Use Mermaid diagrams (PIE, GANTT) within Markdown for immediate visualization.
    - **Automation**: Implement Python/GitHub Actions workflows to generate PNG charts from `data/tasks.csv` to `docs/dashboards/graficos/`.

## Governance Workflow Pattern
`Reunião → Ata → Deliberação → Issues → Project → Gráficos → Relatório mensal`
