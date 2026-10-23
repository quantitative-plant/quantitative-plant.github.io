import type { APIRoute } from 'astro';
import { loaders, serialize, json } from '../../../lib/api';

export async function getStaticPaths() {
  const out = [];
  for (const [collection, load] of Object.entries(loaders))
    for (const e of await load()) out.push({ params: { collection, id: e.id }, props: { e, collection } });
  return out;
}
export const GET: APIRoute = async ({ props }) => json(await serialize(props.e, props.collection));
