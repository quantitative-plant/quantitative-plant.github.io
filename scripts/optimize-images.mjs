// Réduit les images du contenu (max 1600 px, WebP) et met à jour les références dans index.md.
// Usage : node scripts/optimize-images.mjs [src/content]
import sharp from 'sharp';
import { readdir, readFile, writeFile, stat, unlink } from 'node:fs/promises';
import { join, extname, basename } from 'node:path';

const root = process.argv[2] ?? 'src/content';
const MAX = 1600;
let before = 0, after = 0, n = 0;
for (const coll of await readdir(root)) {
  const cdir = join(root, coll);
  if (!(await stat(cdir)).isDirectory()) continue;
  for (const entry of await readdir(cdir)) {
    const dir = join(cdir, entry);
    if (!(await stat(dir)).isDirectory()) continue;
    const md = join(dir, 'index.md');
    let text = await readFile(md, 'utf8').catch(() => null);
    if (text === null) continue;
    for (const f of await readdir(dir)) {
      const ext = extname(f).toLowerCase();
      if (!['.png', '.jpg', '.jpeg', '.gif'].includes(ext)) continue;
      const src = join(dir, f);
      const out = basename(f, extname(f)) + '.webp';
      const size = (await stat(src)).size;
      const buf = await sharp(src, { animated: false })
        .resize({ width: MAX, height: MAX, fit: 'inside', withoutEnlargement: true })
        .webp({ quality: 82 }).toBuffer();
      await writeFile(join(dir, out), buf);
      await unlink(src);
      text = text.replaceAll(`./${f}`, `./${out}`);
      before += size; after += buf.length; n++;
    }
    await writeFile(md, text);
  }
}
console.log(`${n} images: ${(before / 1e6).toFixed(1)} MB → ${(after / 1e6).toFixed(1)} MB`);
