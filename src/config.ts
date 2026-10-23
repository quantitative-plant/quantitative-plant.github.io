// Réglages globaux du site — à adapter avant mise en ligne.
export const SITE = {
  title: 'Quantitative Plant',
  tagline: 'A curated, community-maintained catalogue of software, datasets and models for quantitative plant science.',
  // Dépôt GitHub qui héberge le contenu (utilisé pour « Edit this page » et les formulaires de soumission)
  repo: 'quantitative-plant/quantitative-plant.github.io', // TODO: remplacer par le vrai dépôt
  branch: 'main',
  contact: 'plantimageanalysis@gmail.com', // TODO: adresse de contact à mettre à jour ?
  since: 2013,
};
export const repoUrl = `https://github.com/${SITE.repo}`;
export const editUrl = (collection: string, slug: string) =>
  `${repoUrl}/edit/${SITE.branch}/src/content/${collection}/${slug}/index.md`;
export const issueUrl = (template: string, title = '') =>
  `${repoUrl}/issues/new?template=${template}${title ? `&title=${encodeURIComponent(title)}` : ''}`;
