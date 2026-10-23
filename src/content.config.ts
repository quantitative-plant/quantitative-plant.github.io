import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const common = (image: any) => ({
  title: z.string(),
  slug: z.string().optional(),
  added: z.coerce.date().optional(),
  organs: z.array(z.string()).default([]),
  species: z.array(z.string()).default([]),
  developer: z.string().optional(),
  website: z.string().url().optional(),
  download: z.string().url().optional(),
  doi: z.string().regex(/^10\./).optional(),
  pmid: z.string().regex(/^\d+$/).optional(),
  citation: z.string().optional(),
  description_source: z.string().optional(),
  logo: image().optional(),
  gallery: z.array(z.object({ src: image(), caption: z.string().optional() })).default([]),
  draft: z.boolean().default(false),
  last_checked: z.coerce.date().optional(),
  legacy_url: z.string().optional(),
});

const software = (image: any) =>
  z.object({
    ...common(image),
    status: z.enum(['active', 'unverified', 'unmaintained', 'deprecated']).default('unverified'),
    measurements: z.array(z.string()).default([]),
    automation: z.array(z.enum(['automated', 'semi-automated', 'manual'])).default([]),
    platforms: z.array(z.enum(['windows', 'macos', 'linux', 'web', 'ios', 'android'])).default([]),
    requires: z.array(z.string()).default([]),
    license: z.array(z.enum(['open-source', 'freeware', 'commercial', 'on-request'])).default([]),
    license_name: z.string().optional(),
    source_code: z.string().url().optional(),
    input_formats: z.array(z.string()).default([]),
    export_formats: z.array(z.string()).default([]),
  });

const tools = defineCollection({
  loader: glob({ pattern: '*/index.md', base: './src/content/tools', generateId: ({ entry }) => entry.split('/')[0] }),
  schema: ({ image }) => software(image),
});
const models = defineCollection({
  loader: glob({ pattern: '*/index.md', base: './src/content/models', generateId: ({ entry }) => entry.split('/')[0] }),
  schema: ({ image }) =>
    z.object({
      ...common(image),
      status: z.enum(['active', 'unverified', 'unmaintained', 'deprecated']).default('unverified'),
      category: z.array(z.string()).default([]),      // FSPM, CSM, SPM, gbCSM, ODE, PDE…
      scales: z.array(z.string()).default([]),        // cell, organ, whole-plant, field, regional, global
      predictions: z.array(z.string()).default([]),
      languages: z.array(z.string()).default([]),
      platforms: z.array(z.enum(['windows', 'macos', 'linux', 'web', 'ios', 'android'])).default([]),
      license: z.array(z.enum(['open-source', 'freeware', 'commercial', 'on-request'])).default([]),
      license_name: z.string().optional(),
      integration: z.array(z.string()).default([]),  // OpenAlea, GroIMP, DSSAT…
      source_code: z.string().url().optional(),
    }),
});
const datasets = defineCollection({
  loader: glob({ pattern: '*/index.md', base: './src/content/datasets', generateId: ({ entry }) => entry.split('/')[0] }),
  schema: ({ image }) =>
    z.object({
      ...common(image),
      status: z.enum(['active', 'unverified', 'unmaintained', 'deprecated']).default('unverified'),
      n_images: z.number().int().optional(),
      n_images_text: z.string().optional(),
      paper_url: z.string().url().optional(),
      ground_truth: z.boolean().default(false),
      license_data: z.string().optional(),
    }),
});

export const collections = { tools, datasets, models };
