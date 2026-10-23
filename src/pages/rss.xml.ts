import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import { getTools, getDatasets } from '../lib/content';
import { SITE } from '../config';

export async function GET(context: APIContext) {
  const items = [
    ...(await getTools()).map((e) => ({ e, link: `/software/${e.id}` })),
    ...(await getDatasets()).map((e) => ({ e, link: `/dataset/${e.id}` })),
  ]
    .filter(({ e }) => e.data.added)
    .sort((a, b) => +b.e.data.added! - +a.e.data.added!)
    .slice(0, 50);
  return rss({
    title: SITE.title,
    description: SITE.tagline,
    site: context.site!,
    items: items.map(({ e, link }) => ({
      title: e.data.title, link, pubDate: e.data.added,
      description: (e.body ?? '').split('\n').find((l) => l.trim().length > 40),
    })),
  });
}
