// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://www.quantitative-plant.org',
  trailingSlash: 'ignore',
  integrations: [sitemap({ filter: (page) => !page.includes('/admin') })],
  redirects: {
    // anciennes URL Kirby
    '/1-software': '/software',
    '/2-dataset': '/dataset',
    '/3-model': '/model',
    '/datasets': '/dataset',
    '/models': '/model',
    '/tools': '/software',
    '/5-submit': '/submit',
    '/6-about': '/about',
    '/feed': '/rss.xml',
  },
});
