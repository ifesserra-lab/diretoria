import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// SSOT: o Astro lê o MESMO Markdown que já vive em ../docs (nada é duplicado).
// Os arquivos atuais não têm frontmatter — por isso todo campo é OPCIONAL e o
// título/data são derivados do nome do arquivo quando ausentes (ver src/lib/derive.ts).
// Ao adicionar frontmatter no futuro, o schema já o valida no build.
const base = {
  titulo: z.string().optional(),
  descricao: z.string().optional(),
  ordem: z.number().optional(),
  oculto: z.boolean().optional(),
};

const docsGlob = (dir: string) =>
  glob({ pattern: '**/*.{md,mdx}', base: `../docs/${dir}` });

const atas = defineCollection({
  loader: docsGlob('atas'),
  schema: z.object({
    ...base,
    data: z.coerce.date().optional(),
    tipo: z.string().optional(),
    participantes: z.array(z.string()).optional(),
  }),
});

const decisoes = defineCollection({
  loader: docsGlob('decisoes'),
  schema: z.object({
    ...base,
    numero: z.number().optional(),
    status: z.enum(['proposta', 'aceita', 'revisada', 'substituida']).optional(),
    data: z.coerce.date().optional(),
    tags: z.array(z.string()).optional(),
  }),
});

const atividades = defineCollection({
  loader: docsGlob('atividades'),
  schema: z.object({ ...base, mes: z.string().optional() }),
});

const comissoes = defineCollection({
  loader: docsGlob('comissao'),
  schema: z.object({ ...base, responsavel: z.string().optional() }),
});

const processos = defineCollection({
  loader: docsGlob('processo'),
  schema: z.object({ ...base }),
});

const pautas = defineCollection({
  loader: docsGlob('pautas'),
  schema: z.object({ ...base, data: z.coerce.date().optional() }),
});

const paginas = defineCollection({
  // páginas soltas: equipe/index.md, tools/README.md, dashboards/*
  loader: glob({ pattern: '{equipe,tools,dashboards}/**/*.md', base: '../docs' }),
  schema: z.object({ ...base }),
});

export const collections = { atas, decisoes, atividades, comissoes, processos, pautas, paginas };
