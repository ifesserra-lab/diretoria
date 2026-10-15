// Copia os painéis HTML já gerados (SSOT em ../docs/relatorios) para public/,
// para o Astro servi-los como estáticos. Mantém a fonte única de verdade intacta.
// Por padrão copia só os painéis leves de topo (~1.7M); as árvores geradas
// grandes (campus-serra, egressos) ficam em GitHub Pages dedicado — ver src/lib/reports.ts.
import { cp, mkdir, readdir, stat } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const SRC = resolve(__dirname, '../../docs/relatorios');
const DEST = resolve(__dirname, '../public/relatorios');
const COPY_ALL = process.env.PAINEIS === 'all'; // PAINEIS=all copia tudo (99M)

// Apresentação dos Grupos de Pesquisa: cards e slides (SSOT em ../docs/apresentacao_grupo_pesquisa).
// Roda em qualquer modo — inclusive PAINEIS=all, usado no deploy.
async function copyGruposPesquisa() {
  const GP = resolve(__dirname, '../../docs/apresentacao_grupo_pesquisa');
  if (!existsSync(GP)) return;
  const GP_DEST = resolve(__dirname, '../public/grupos-de-pesquisa');
  await mkdir(GP_DEST, { recursive: true });
  for (const name of await readdir(GP)) {
    if (/\.(pdf|jpe?g|png|webp)$/i.test(name)) await cp(join(GP, name), join(GP_DEST, name));
  }
}

async function main() {
  await copyGruposPesquisa();
  if (!existsSync(SRC)) {
    console.warn('[copy-paineis] ../docs/relatorios não encontrado — pulando.');
    return;
  }
  await mkdir(DEST, { recursive: true });

  if (COPY_ALL) {
    await cp(SRC, DEST, { recursive: true });
    console.log('[copy-paineis] copiado TUDO (PAINEIS=all).');
    return;
  }

  // Só os .html/.json de topo de docs/relatorios (leves).
  const entries = await readdir(SRC);
  let n = 0;
  for (const name of entries) {
    const from = join(SRC, name);
    const info = await stat(from);
    if (info.isFile() && /\.(html|json|txt)$/i.test(name)) {
      await cp(from, join(DEST, name));
      n++;
    }
  }

  // img/ vai junto: são as imagens que os painéis de topo referenciam por
  // caminho relativo (ex.: img/paineis/*.jpg no balanço). Sem isso o Astro
  // serve o HTML e quebra as imagens.
  const IMG = join(SRC, 'img');
  let imgs = 0;
  if (existsSync(IMG)) {
    await cp(IMG, join(DEST, 'img'), { recursive: true });
    for (const dir of await readdir(IMG)) {
      const sub = join(IMG, dir);
      imgs += (await stat(sub)).isDirectory() ? (await readdir(sub)).length : 1;
    }
  }
  console.log(`[copy-paineis] ${n} painéis de topo e ${imgs} imagens copiados. (PAINEIS=all para incluir árvores geradas)`);
}

main().catch((e) => { console.error(e); process.exit(1); });
