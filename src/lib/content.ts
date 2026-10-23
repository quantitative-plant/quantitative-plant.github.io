import { getCollection, type CollectionEntry } from 'astro:content';

const visible = <T extends { data: { draft: boolean } }>(e: T) => import.meta.env.DEV || !e.data.draft;
const byTitle = (a: any, b: any) => a.data.title.localeCompare(b.data.title, 'en', { sensitivity: 'base' });

export const getTools = async () => (await getCollection('tools', visible)).sort(byTitle);
export const getDatasets = async () => (await getCollection('datasets', visible)).sort(byTitle);
export const getModels = async () => (await getCollection('models', visible)).sort(byTitle);

export const doiUrl = (doi?: string) => (doi ? `https://doi.org/${doi}` : undefined);
export const pmidUrl = (pmid?: string) => (pmid ? `https://pubmed.ncbi.nlm.nih.gov/${pmid}/` : undefined);

/** Compte les valeurs d'un champ liste à travers une collection (pour les facettes). */
export function facet<T>(items: T[], get: (t: T) => string[]) {
  const m = new Map<string, number>();
  for (const it of items) for (const v of get(it)) m.set(v, (m.get(v) ?? 0) + 1);
  return [...m.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
}

/** Outils proches : même organe, mesures partagées. */
export function similar(all: CollectionEntry<'tools'>[], t: CollectionEntry<'tools'>, n = 4) {
  return all
    .filter((o) => o.id !== t.id)
    .map((o) => {
      const org = o.data.organs.filter((x) => t.data.organs.includes(x)).length;
      const mes = o.data.measurements.filter((x) => t.data.measurements.includes(x)).length;
      return { o, score: org * 3 + mes };
    })
    .filter((x) => x.score > 3)
    .sort((a, b) => b.score - a.score)
    .slice(0, n)
    .map((x) => x.o);
}
