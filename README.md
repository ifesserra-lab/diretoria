# IFES Serra - Diretoria (Governança)

Este repositório serve como a **fonte oficial de verdade** para a gestão da diretoria, seguindo os princípios de **GitOps para Governança**. Aqui são centralizadas pautas, atas, decisões, tarefas e indicadores.

## Estrutura do Repositório

- `docs/atas/`: Registros de todas as reuniões da diretoria.
- `docs/decisoes/`: Documentação de decisões formais e de longo prazo.
- `docs/dashboards/`: Visão consolidada de indicadores e gráficos.
- `docs/relatorios/`: Relatórios mensais e trimestrais de gestão.
- `data/`: Dados brutos (CSV/JSON) que alimentam os gráficos.
- `scripts/`: Automações para geração de relatórios e visualizações.
- `.github/`: Templates de Issues e workflows de CI/CD para governança.


## Modelo de Funcionamento

O fluxo de trabalho segue a seguinte lógica:
1. **Reunião**: Gera uma pauta e, posteriormente, uma **Ata**.
2. **Ata**: Lista deliberações e ações que viram **Issues**.
3. **Issues**: São categorizadas e acompanhadas no [GitHub Project](https://github.com/orgs/ifesserra-lab/projects).
4. **Relatórios**: Workflows automáticos geram gráficos a partir das tarefas para o dashboard.

## Como Contribuir

- **Nova Tarefa**: Abra uma Issue usando o template de `Tarefa`.
- **Nova Decisão**: Crie um PR adicionando um arquivo em `docs/decisoes/`.
- **Registro de Ata**: Adicione o arquivo Markdown em `docs/atas/` após a reunião.

---
*Mantido pela Diretoria do IFES Campus Serra.*
