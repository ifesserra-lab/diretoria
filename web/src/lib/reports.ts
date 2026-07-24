// Catálogo dos painéis analíticos. Os .html já existem em ../docs/relatorios (SSOT).
// `path`  = servido localmente a partir de public/ (copiado no prebuild).
// `ext`   = versão publicada em GitHub Pages dedicado (árvores grandes geradas).
// status: ok | wip | exp   ·   spark: line | area | bars (dado decorativo do card)

export type Report = {
  slug: string;
  titulo: string;
  tag: string;
  descricao: string;
  status: 'ok' | 'wip' | 'exp';
  path?: string;
  ext?: string;
  heavy?: boolean;   // árvore grande: link vai para `ext` por padrão
  destaque?: boolean;
  spark: 'line' | 'area' | 'bars';
};

export const reports: Report[] = [
  {
    slug: 'campus-serra', titulo: 'Extensão — Campus Serra (SRC)', tag: 'Extensão · SRC',
    descricao: '201 ações, 525 atividades e 757 extensionistas. Busca, jornada do formado, pendências e dados abertos (JSON + llms.txt).',
    status: 'ok', path: 'relatorios/campus-serra/index.html', ext: 'https://ifesserra-lab.github.io/src/', heavy: true, destaque: true, spark: 'area',
  },
  {
    slug: 'roi-impacto-pesquisa', titulo: 'ROI e Impacto da Pesquisa', tag: 'Multidimensional',
    descricao: 'Payback · CAHS · Manifesto de Leiden/DORA · REF. Painel de 7 dimensões, valores em ordem de grandeza. Exercício metodológico.',
    status: 'ok', path: 'relatorios/roi-impacto-pesquisa.html', destaque: true, spark: 'bars',
  },
  {
    slug: 'egressos', titulo: 'Egressos — Impacto na Carreira', tag: 'Experimental',
    descricao: 'Trajetória de 28 egressos da mesma base (IC, LEDS/IFES, Morpheus) até posições sênior. Anonimizado A–AB, dados preliminares.',
    status: 'exp', path: 'relatorios/egressos/index.html', ext: 'https://ifesserra-lab.github.io/egressos/', heavy: true, destaque: true, spark: 'line',
  },
  {
    slug: 'pesquisa-x-extensao', titulo: 'Pesquisa × Extensão', tag: 'Cruzamento',
    descricao: '78% dos coordenadores de pesquisa também fazem extensão — e fazer extensão não reduz o impacto científico (FWCI mediano).',
    status: 'ok', path: 'relatorios/pesquisa-x-extensao.html', spark: 'line',
  },
  {
    slug: 'captacao-projetos', titulo: 'Captação de Projetos — FAPES + FACTO', tag: 'Fomento',
    descricao: 'Projetos por ano, captação em índice, bolsistas ao longo do tempo, rubricas do orçamento e liderança de captação por coordenador.',
    status: 'ok', path: 'relatorios/captacao-projetos.html', spark: 'area',
  },
  {
    slug: 'indice-extensao', titulo: 'Índice de Extensão (FORPROEX)', tag: '5 dimensões',
    descricao: 'A extensão do campus nas cinco dimensões dos Indicadores Brasileiros de Extensão (FORPROEX, 2017), só com dados verificáveis.',
    status: 'ok', path: 'relatorios/indice-extensao.html', spark: 'bars',
  },
  {
    slug: 'docentes-veiculos-impacto', titulo: 'Docentes — Veículos e Impacto', tag: 'Bibliometria',
    descricao: 'Onde os docentes publicam (SJR/SCImago Q1–Q4, Qualis CAPES) cruzado com impacto real (citações, FWCI, h/g/m) via OpenAlex.',
    status: 'ok', path: 'relatorios/docentes-veiculos-impacto.html', spark: 'bars',
  },
  {
    slug: 'dashboard-impacto-docentes', titulo: 'Dashboard de Impacto dos Docentes', tag: 'Uso interno',
    descricao: 'Ascensão, produção de elite (top 10%/1%), eficiência fracionada, concentração (Lorenz/Gini), benchmark por área. Simulação.',
    status: 'wip', path: 'relatorios/dashboard-impacto-docentes.html', spark: 'line',
  },
  {
    slug: 'ppp-edital-13-2026', titulo: 'Edital PRPPG 13/2026 — PPP', tag: 'Elegibilidade',
    descricao: 'Elegibilidade dos docentes ao Programa Pesquisador de Produtividade (PQ-1/2/3): pontuação por percentil e orientações concluídas.',
    status: 'ok', path: 'relatorios/ppp-edital-13-2026.html', spark: 'bars',
  },
  {
    slug: 'pesquisa-na-formacao', titulo: 'Pesquisa na Formação', tag: 'Formação',
    descricao: 'Participação em pesquisa dos egressos da graduação (SI e ECA) e a trajetória dos discentes do mestrado PPComp.',
    status: 'ok', path: 'relatorios/pesquisa-na-formacao.html', spark: 'area',
  },
  {
    slug: 'formandos-pesquisa-detalhado', titulo: 'Formandos × Pesquisa (detalhado)', tag: 'Dados nominais',
    descricao: 'Versão operacional: cotas, fomento por agência, tempo ajustado por curso, funil IC→TCC e pipeline graduação→mestrado.',
    status: 'wip', path: 'relatorios/formandos-pesquisa-detalhado.html', spark: 'line',
  },
  {
    slug: 'rede-colaboracao', titulo: 'Rede de Colaboração', tag: 'Interativo',
    descricao: 'Ego-rede de coautoria por pesquisador, detecção de comunidades (Louvain) e padrões por área. Versão preliminar.',
    status: 'wip', path: 'relatorios/rede-colaboracao.html', spark: 'line',
  },
];

/** resolve o link do card conforme o ambiente (base do Astro) */
export function reportHref(r: Report, base: string): string {
  if (r.heavy && r.ext) return r.ext;
  if (r.path) return joinBase(base, r.path);
  return r.ext ?? '#';
}
export function joinBase(base: string, p: string): string {
  return `${base.replace(/\/$/, '')}/${p.replace(/^\//, '')}`;
}
