import { getImage } from 'astro:assets';
import { getTools, getDatasets, getModels, doiUrl } from './content';

const SITE = 'https://www.quantitative-plant.org';
const paths = { tools: 'software', datasets: 'dataset', models: 'model' } as const;

export async function serialize(e: any, collection: keyof typeof paths) {
  const { logo, gallery, draft, legacy_url, slug, ...d } = e.data;
  return {
    id: e.id,
    type: collection === 'tools' ? 'tool' : collection.slice(0, -1),
    url: `${SITE}/${paths[collection]}/${e.id}`,
    ...d,
    added: d.added?.toISOString().slice(0, 10),
    last_checked: d.last_checked?.toISOString().slice(0, 10),
    doi_url: doiUrl(d.doi),
    logo: logo ? SITE + (await getImage({ src: logo, width: 256, format: 'png' })).src : undefined,
    description: e.body?.trim(),
  };
}
export const loaders = { tools: getTools, datasets: getDatasets, models: getModels };
export const json = (data: unknown) =>
  new Response(JSON.stringify(data, null, 1), { headers: { 'Content-Type': 'application/json; charset=utf-8' } });
