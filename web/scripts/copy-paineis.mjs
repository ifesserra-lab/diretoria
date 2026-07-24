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

async function main() {
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
  console.log(`[copy-paineis] ${n} painéis de topo copiados. (PAINEIS=all para incluir árvores geradas)`);
}

main().catch((e) => { console.error(e); process.exit(1); });
