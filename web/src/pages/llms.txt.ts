import type { APIRoute } from 'astro';
import { getCollection, type CollectionEntry } from 'astro:content';
import { sections } from '../lib/sections';
import { reports } from '../lib/reports';
import { displayTitle, dateFromId, fmtDate } from '../lib/derive';

// llms.txt (https://llmstxt.org): índice do portal em Markdown para consumo
// por LLMs. Gerado no build a partir das mesmas coleções das listagens.

const SITE = 'https://ifesserra-lab.github.io';
const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');

const abs = (path: string) => `${SITE}${BASE}${path}`;

function linkLine(e: CollectionEntry<any>, href: string): string {
  const data = (e.data as any)?.data ?? dateFromId(e.id);
  const desc = (e.data as any)?.descricao ?? (e.data as any)?.responsavel;
  const extra = [data ? fmtDate(data) : null, desc].filter(Boolean).join(' — ');
  return `- [${displayTitle(e as any)}](${abs(href)}/${e.id})${extra ? `: ${extra}` : ''}`;
}

async function sectionBlock(key: keyof typeof sections): Promise<string> {
  const s = sections[key];
  const entries = (await getCollection(s.key as any))
    .filter((e) => !/^(modelo-|template)/i.test(e.id.split('/').pop() ?? ''));
  const rows = entries.map((e) => ({ e, data: (e.data as any)?.data ?? dateFromId(e.id) }));
  if (s.dateSort) rows.sort((a, b) => (b.data?.getTime() ?? 0) - (a.data?.getTime() ?? 0));
  else rows.sort((a, b) => displayTitle(a.e as any).localeCompare(displayTitle(b.e as any), 'pt-BR'));
  return [`## ${s.label}`, '', s.intro, '', ...rows.map(({ e }) => linkLine(e, s.href))].join('\n');
}

export const GET: APIRoute = async () => {
  const blocks = await Promise.all(
    (['atas', 'decisoes', 'comissoes', 'processos', 'pautas', 'atividades'] as const).map(sectionBlock)
  );

  const relatorios = [
    '## Relatórios',
    '',
    'Painéis analíticos de pesquisa, pós-graduação e extensão do campus.',
    '',
    ...reports.map((r) => {
      const url = r.ext ?? (r.path ? abs(`/${r.path}`) : abs('/relatorios'));
      return `- [${r.titulo}](${url}): ${r.resumo}`;
    }),
  ].join('\n');

  const body = [
    '# Portal de Governança DPPGE — IFES Campus Serra',
    '',
    '> Fonte única de verdade (SSOT, via GitOps) da Diretoria de Pesquisa, Pós-Graduação e Extensão (DPPGE) do IFES Campus Serra: atas de reunião, decisões formalizadas (ADR), comissões, processos, pautas, atividades e relatórios analíticos.',
    '',
    'Todo o conteúdo é Markdown versionado em https://github.com/ifesserra-lab/diretoria (pasta `docs/`). As páginas listadas abaixo são a versão publicada desse mesmo conteúdo.',
    '',
    ...blocks.flatMap((b) => [b, '']),
    relatorios,
    '',
    '## Optional',
    '',
    `- [Equipe](${abs('/equipe')}): equipe gestora da diretoria e contatos`,
    `- [Sitemap](${abs('/sitemap-index.xml')}): índice completo de páginas`,
    '',
  ].join('\n');

  return new Response(body, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
