import type { APIRoute } from 'astro';
import { loaders, serialize, json } from '../../lib/api';

export function getStaticPaths() {
  return ['tools', 'datasets', 'models', 'all'].map((collection) => ({ params: { collection } }));
}
export const GET: APIRoute = async ({ params }) => {
  const c = params.collection as keyof typeof loaders | 'all';
  const keys = c === 'all' ? (Object.keys(loaders) as (keyof typeof loaders)[]) : [c];
  const items = (await Promise.all(keys.map(async (k) => Promise.all((await loaders[k]()).map((e) => serialize(e, k)))))).flat();
  return json({ generated: new Date().toISOString(), license: 'ODC-By-1.0', count: items.length, items });
};
