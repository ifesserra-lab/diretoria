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

- **Task Synchronization from Minutes**: Skilled in synchronizing tasks from minutes to GitHub.
    - **Trigger**: New entries in `## 3. Plano de Ações (Issues)` in `docs/atas/`.
    - **Extraction**: Reads items like `- [ ] Task Name (Responsible: @user, Area: Area, Priority: Priority, Deadline: YYYY-MM-DD)`.
    - **Action**: Creates GitHub Issues in the repository, assigns to Project #7, and updates the Markdown with the Issue link (- [Issue #123](URL) Task Name...).

## Governance Workflow Pattern
`Reunião → Ata → Deliberação → Issues → Project → Gráficos → Relatório mensal`

---

# Portal (Astro) — Design & Voice

The public portal lives in `web/` (Astro). It reads the **same** Markdown from `docs/` via
content-collection glob loaders — `docs/` stays the single source of truth. When generating any
page, component, or copy, follow the identity below. Precedence: the user's words > this system > your choices.

## Design System — "Registro Vivo"

The concept: the DPPGE content is simultaneously a **formal record** (atas, decisões/ADR — serif)
and a **data instrument** (16 painéis, bibliometria, Git — mono). Typography carries that duality.

- **Color (tokens in `web/src/styles/global.css`)** — a single bold gesture, used sparingly:
    - `--green` **#17654A** (verde-pinheiro): primary. Links, active nav, primary buttons, accents.
    - `--gold` **#B8791F** (ocre): the **data / Git layer** — GitStrip, report tags, eyebrows, "how to read" notes.
    - `--danger` **#B23A2E** (tijolo): **only** for danger/experimental/preliminary warnings.
    - Neutrals are **green-biased**, never pure grey: `--paper` #F6F7F4, `--ink` #14201A (dark: #0D1512 / #E9EFEA).
    - Every color goes through a CSS custom property. Never hardcode a hex in a component.
- **Typography (3 roles)** — production faces self-hosted via `@fontsource` (CSP blocks CDNs):
    - `--serif` **Fraunces** → the record: all headings, document titles, report card titles, stat numbers.
    - `--sans` **Public Sans** (a face designed for government) → body / reading.
    - `--mono` **IBM Plex Mono** → the data/Git layer: commit SHAs, labels, eyebrows, tabular numbers, `.kbd`.
    - Keep running text ~65ch; headings `text-wrap: balance`; uppercase labels get `.06–.12em` letter-spacing.
- **Both themes always.** Light + dark are defined token-by-token (media query + `data-theme` override, both directions). Give dark equal care — don't invert.
- **Components** (in `web/src/components/`): `Callout` (note/warn/danger — replaces MkDocs admonitions),
  `GitStrip`, `QuickCard`, `StatStrip`, `ReportCard` + `Spark`, `DocList`. Reuse these; don't reinvent.
- **No AI-generic tics**: no emoji as section markers (the 🚧 status pill is the one deliberate exception),
  no purple→blue gradients, no everything-centered, no rounded-everything. Structure (eyebrows, mono
  metadata, status pills) must encode something true, not decorate.

## Voice & Copy (pt-BR)

Write like an office **rendering accounts (prestação de contas)**, not marketing. Direct, verifiable, no hype.
Honesty about data limits is a brand trait — it builds trust in a governance portal.

- **Avoid:** "soluções inovadoras", "bem-vindo ao nosso portal!", "dados incríveis", "clique aqui", hype adjectives, exclamation.
- **Use:** "Toda decisão tem uma origem rastreável.", "Fonte única de verdade — pública e auditável.",
  active voice, exact numbers ("28 egressos", "78%"), and action labels that say what happens ("Abrir painel →").
- **Limits are first-class copy.** Keep the status pills (`experimental`, `🚧 em construção`) and the
  "Como ler e decidir" / privacy notes. Always state what the data does **not** prove.
- **Buttons/links** name the destination or action, never "saiba mais". Errors explain what's wrong and how to fix it.

See `web/README.md` for the stack, the MkDocs→Astro mapping, and how to run/build/deploy.
