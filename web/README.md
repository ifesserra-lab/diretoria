# Portal DPPGE — web (Astro · "Registro Vivo")

Releitura do Portal de Governança do DPPGE (IFES Campus Serra) em **Astro**. Migra do MkDocs
Material mantendo o modelo **GitOps**: o Markdown em `../docs/` continua sendo a **fonte única de
verdade** — o Astro lê os mesmos arquivos via *content collections* (nada é duplicado).

## Rodar

```bash
cd web
npm install
npm run dev       # http://localhost:4321/diretoria
npm run build     # gera dist/ + índice de busca (Pagefind)
npm run preview   # serve o dist/ localmente
```

Painéis pesados (árvores geradas de `campus-serra` e `egressos`, ~99M): por padrão o `prebuild`
copia só os painéis leves de topo. Para incluir tudo localmente:

```bash
PAINEIS=all npm run build
```

## Como funciona a identidade "Registro Vivo"

Serifa = o registro (atas, decisões) · mono = o dado/Git · sans = leitura. Verde-pinheiro é o
único gesto forte; ocre = camada de dados/Git; tijolo = só alertas. Tokens em
`src/styles/global.css`; princípios e voz em [`../.agent/AGENTS.md`](../.agent/AGENTS.md).

## De MkDocs para Astro

| Antes (MkDocs) | Agora (Astro) |
| --- | --- |
| `nav:` no `mkdocs.yml` | roteamento por arquivo + `getCollection()` |
| `docs/atas/*.md` etc. | coleções com glob loader apontando p/ `../docs` (`src/content.config.ts`) |
| `!!! note / warning / danger` | componente `<Callout>` (`.mdx`) |
| busca do Material | **Pagefind** — índice estático gerado no build, roda no navegador |
| `mermaid2` | Mermaid client-side (só carrega se a página tiver bloco `mermaid`) |
| `relatorios/*.html` (painéis) | servidos de `public/` (copiados no prebuild) ou GitHub Pages dedicado |
| `edit_uri` | botão "Editar no GitHub" por página |
| tema indigo | sistema "Registro Vivo" (claro/escuro token-a-token) |

Os arquivos em `docs/` **não têm frontmatter**; os schemas Zod são tolerantes e o
título/data são derivados do nome do arquivo (`src/lib/derive.ts`). Adicionar frontmatter no
futuro é opcional — o schema já o valida no build.

## Estrutura

```
web/
├─ src/
│  ├─ content.config.ts     # coleções + schemas Zod (glob p/ ../docs)
│  ├─ layouts/              # Base, Doc
│  ├─ components/           # Nav, Callout, GitStrip, QuickCard, StatStrip, ReportCard, Spark, DocList
│  ├─ lib/                  # nav, sections, reports, derive
│  ├─ pages/                # index + seções (atas, decisoes, comissoes, processos, pautas, atividades) + relatorios + equipe
│  └─ styles/global.css     # tokens "Registro Vivo"
├─ scripts/copy-paineis.mjs # copia painéis de ../docs/relatorios p/ public/
└─ astro.config.mjs         # base: /diretoria
```

## Deploy

`.github/workflows/deploy-web.yml` roda **automaticamente** a cada push no `master` que toque em
`web/**`, `docs/**` ou no próprio workflow (inclui a atualização noturna do bot) — e também sob
demanda (**workflow_dispatch**). Roda `npm run build` e publica `web/dist/` no GitHub Pages. O
carimbo da `GitStrip` é injetado no build via `PUBLIC_GIT_SHA` / `PUBLIC_GIT_MSG` / `PUBLIC_GIT_WHEN`.

> Requer, uma vez: **Settings → Pages → Source: GitHub Actions**.
