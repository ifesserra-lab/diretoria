// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// Portal de Governança DPPGE — IFES Campus Serra
// Publicado hoje em GitHub Pages sob /diretoria (mesmo caminho do MkDocs).
export default defineConfig({
  site: 'https://ifesserra-lab.github.io',
  base: '/diretoria',
  trailingSlash: 'ignore',
  integrations: [mdx(), sitemap()],
  markdown: {
    shikiConfig: { theme: 'github-light', wrap: true },
  },
});
