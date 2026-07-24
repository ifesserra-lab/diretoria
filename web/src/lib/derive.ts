// Deriva metadados de exibição quando o Markdown não tem frontmatter.
// Fonte única de verdade continua sendo o conteúdo do arquivo em ../docs.

const MESES = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'];

/** slug "comissao-gestao-laboratorios" -> "Comissão de Gestão de Laboratórios" (aprox.) */
export function prettify(slug: string): string {
  const last = slug.split('/').pop() ?? slug;
  const base = last.replace(/\.(md|mdx)$/,'');
  // data-prefixada: 2026-03-12-reuniao-geral
  const m = base.match(/^(\d{4})-(\d{2})(?:-(\d{2}))?-?(.*)$/);
  if (m) {
    const [, y, mo, d, rest] = m;
    const label = rest ? rest.replace(/[-_]/g,' ') : `${MESES[+mo-1] ?? mo} de ${y}`;
    const pretty = capitalize(label);
    return d ? `${pretty}` : pretty;
  }
  return capitalize(base.replace(/^readme$/i,'Resumo').replace(/[-_]/g,' '));
}

/** extrai a data ISO de um id data-prefixado, senão undefined */
export function dateFromId(id: string): Date | undefined {
  const last = id.split('/').pop() ?? id;
  const m = last.match(/^(\d{4})-(\d{2})-(\d{2})/);
  if (m) return new Date(`${m[1]}-${m[2]}-${m[3]}T12:00:00`);
  const my = last.match(/^(\d{4})-(\d{2})/);
  if (my) return new Date(`${my[1]}-${my[2]}-01T12:00:00`);
  return undefined;
}

export function fmtDate(d?: Date): string {
  if (!d) return '';
  return d.toLocaleDateString('pt-BR', { day:'2-digit', month:'2-digit', year:'numeric' });
}

export function fmtMonth(d?: Date): string {
  if (!d) return '';
  return `${MESES[d.getMonth()]} de ${d.getFullYear()}`;
}

function capitalize(s: string) {
  const t = s.trim();
  return t.charAt(0).toUpperCase() + t.slice(1);
}

/** primeiro "# Título" do corpo Markdown (título real, com acentos) */
export function titleFromBody(body?: string): string | undefined {
  if (!body) return undefined;
  const m = body.match(/^\s*#\s+(.+?)\s*#*\s*$/m);
  if (!m) return undefined;
  // remove marcações inline simples (**, *, `, links)
  return m[1]
    .replace(/\*\*|__|\*|`/g, '')
    .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
    .trim();
}

/** título de exibição: frontmatter > primeiro H1 do corpo > slug prettificado */
export function displayTitle(entry: { id: string; body?: string; data?: any }): string {
  return entry.data?.titulo ?? titleFromBody(entry.body) ?? prettify(entry.id);
}

/** modelos/templates não vão para as listagens públicas */
export function isTemplate(id: string): boolean {
  return /modelo|template|readme/i.test(id.split('/').pop() ?? id) && !/^readme$/i.test((id.split('/').pop()??''));
}
