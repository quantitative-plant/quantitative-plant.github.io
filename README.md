# Quantitative Plant — quantitative-plant.org (v2, 2026)

Refonte du site **Quantitative Plant** (anciennement [plant-image-analysis.org](https://www.plant-image-analysis.org), nouveau domaine `www.quantitative-plant.org`) : passage d'un CMS PHP (Kirby 2.5.5, 2017) à un **site statique versionné sur GitHub**, sans serveur, sans base de données, alimenté par la communauté via pull requests et formulaires.

## Démarrer

```bash
npm install
npm run dev        # http://localhost:4321 (les brouillons sont visibles en dev)
npm run build      # génère dist/ + l'index de recherche Pagefind
npm run preview    # sert dist/ localement
```

Node ≥ 20. Le dossier `dist/` se dépose tel quel sur n'importe quel hébergement statique.

---

## 1. Diagnostic de l'existant

| Constat | Conséquence |
|---|---|
| Kirby **2.5.5** (2017), PHP, plus maintenu | failles non corrigées, incompatibilités PHP 8, licence payante par domaine |
| `site/config/config.php` : `debug = true` et **identifiants MySQL en clair** | fuite d'informations ; **à changer immédiatement** si le serveur est encore en ligne |
| Contenu mis à jour pour la dernière fois en **2019** | liens morts probables, outils abandonnés non signalés |
| Doublons (`011-` et `151-image-harvest`, `010-` et `153-maize-kernel…`) et pages de test (`test`, `test2`, `testsoftware`, `dan-ahsnfguiltopne`) | compteur surestimé |
| Fiche modèle « CPlantBox » contenant le texte de *Assess* | contenu erroné |
| Vocabulaires libres (`Excell`/`excell`/`xls`, `Arabidopsis`/`arabidopsis`, `mac`…) | filtres incohérents |
| Soumissions via Google Forms, commentaires Disqus, Google Charts | dépendances externes, traçage, pas de traçabilité des modifications |
| Images non optimisées (146 Mo de PNG) | pages lentes |
| API dynamique PHP (`/api?type=…&field=…&q=…`) | dépend du serveur PHP |

## 2. Nouvelle architecture

```
GitHub (source de vérité)                         Visiteurs
 ├─ src/content/tools/<slug>/index.md  ─┐
 ├─ src/content/datasets/<slug>/…       ├─ Astro build ─► dist/ (HTML statique) ─► GitHub Pages / Netlify / serveur UCLouvain
 ├─ src/content/models/<slug>/…         │   + schéma validé (zod)      ├─ /software, /dataset, /model
 │   (YAML + Markdown + images)        ─┘   + images WebP optimisées   ├─ /api/*.json  (API statique)
 ├─ Issue forms ─► curation ─► PR                                      ├─ /search      (Pagefind, hors-ligne)
 └─ Actions : build à chaque PR, déploiement sur main,                 └─ /rss.xml, sitemap
              vérification mensuelle des liens
```

**Choix clés**

- **Astro 5** (générateur statique) : HTML pur, quasiment zéro JavaScript ; seul le filtre du catalogue (≈ 3 Ko de JS vanilla) et la recherche sont interactifs.
- **Contenu = fichiers** : une fiche = un dossier `index.md` + logo + captures. Lisible, diffable, citable, archivable sur Zenodo.
- **Schéma validé** (`src/content.config.ts`) : une fiche mal formée fait échouer le build de la PR → qualité garantie sans relecture manuelle des champs.
- **Vocabulaires contrôlés** (`src/data/vocab.ts`) : organes, plateformes, licences, automatisation, statut.
- **Recherche plein texte** Pagefind (index statique, pas de service tiers).
- **API JSON statique** : `/api/tools.json`, `/api/datasets.json`, `/api/models.json`, `/api/all.json`, `/api/{collection}/{id}.json`.
- **URL conservées** : `/software/<slug>` et `/dataset/<slug>` identiques à l'ancien site → pas de liens cassés depuis les articles qui citent le site ; redirections pour `/1-software`, `/feed`, etc.
- **SEO / FAIR** : JSON-LD `SoftwareApplication` / `Dataset` sur chaque fiche, sitemap, RSS, DOI résolus.
- **Clair / sombre** automatique, responsive, accessible (navigation clavier, contrastes).

## 3. Modèle de données

Trois collections : `tools` (logiciels), `datasets`, `models`. Fiche outil :

```yaml
title: DIRT
slug: dirt
added: 2014-09-09
status: unverified        # active | unverified | unmaintained | deprecated   ← NOUVEAU
last_checked: 2026-10-22  #                                                     ← NOUVEAU
organs: [root-system]
measurements: [length, shape, diameter]
automation: [automated]
platforms: [windows, macos, linux, web]
requires: [matlab]        # dépendances (matlab, imagej, python…)                ← NOUVEAU
license: [open-source, freeware]
source_code: https://github.com/…                                               ← NOUVEAU
input_formats: [any]
export_formats: [csv]
species: [any]
developer: Georgia Tech and PennState University
website: …   download: …   doi: …   pmid: …   citation: …
logo: ./logo.webp
gallery: [{ src: ./dirt-1.webp, caption: "Source: Plant Physiology" }]
```

Les modèles ont leurs propres champs : `category` (FSPM, CSM, SPM, gbCSM, ODE…), `organs` (partie de plante), `scales` (cell → global), `predictions`, `species`, `languages`, `integration` (OpenAlea, GroIMP, DSSAT…), `platforms`, `license`. Les datasets : `n_images` (ou `n_images_text`), `ground_truth`, `status`, `paper_url`.

Toutes les fiches migrées ont le statut **`unverified`** : la page l'affiche avec un lien « report a problem ». La revue progressive (passage à `active` + `last_checked`) est la principale tâche éditoriale à venir.

## 4. Contribuer

- **Formulaire** (aucune connaissance Git) : `.github/ISSUE_TEMPLATE/new-tool.yml`, `new-dataset.yml`, `report-problem.yml`.
- **Pull request** : copier `templates/tool/index.md` dans `src/content/tools/<nom>/`, remplir, ouvrir la PR. Le workflow `deploy.yml` construit le site et refuse les fiches invalides.
- Chaque fiche a des liens « Suggest an edit on GitHub » et « Report a problem ».
- `check-links.yml` ouvre chaque mois une issue listant les liens morts.

## 5. Migration (reproductible)

```bash
python3 scripts/migrate_kirby.py <ancien_site>/content src/content   # Kirby .txt → Markdown/YAML
node scripts/optimize-images.mjs src/content                          # PNG → WebP ≤ 1600 px (146 Mo → 19 Mo)
```

Étape 1 — migration depuis la dernière version du site Kirby (dossier `quantitative_plant`, contenu jusqu'en 2019) : descriptions, captures, logos, dates (images 197 Mo → 23 Mo).

Étape 2 — import des données à jour (exports `data/import/{tools,datasets,models}.json`) :

```bash
python3 scripts/import_json.py      # rapport : data/import/import-report.json
```

Le JSON fait foi pour la liste des entrées et leurs champs structurés ; les descriptions, images, dates et citations existantes sont conservées. Les fiches absentes du JSON passent en brouillon (rien n'est supprimé). Résultat au 23/10/2026 : **201 outils** (23 nouveaux), **42 datasets** (14 nouveaux), **120 modèles** (nouvelle section). Les noms marqués `[deprecated]` ont le statut `deprecated` ; 5 liens de téléchargement signés et expirés (Plant Physiology / Silverchair) ont été retirés.

## 6. Déploiement

1. Créer le dépôt GitHub (ex. `quantitative-plant/quantitative-plant.org`) et mettre à jour `SITE.repo` dans `src/config.ts`.
2. Settings → Pages → Source : *GitHub Actions*.
3. Pointer le DNS `www.quantitative-plant.org` vers GitHub Pages (fichier `public/CNAME`). Rediriger l'ancien domaine `plant-image-analysis.org` vers le nouveau (les chemins `/software/<slug>` et `/dataset/<slug>` sont identiques, une redirection de domaine suffit).
4. Couper l'ancien serveur PHP **et changer le mot de passe MySQL**.

Alternative : le dossier `dist/` peut être servi par n'importe quel serveur web (UCLouvain, OVH…) sans PHP.

## 7. Éditeur web (Decap CMS)

Une interface d'édition est disponible sur **`/admin`** : formulaires avec listes déroulantes (organe, licence, plateformes, mesures…), upload du logo et des captures, éditeur de texte pour la description. Elle lit et écrit les mêmes fichiers Markdown que le site ; la configuration des champs est dans `public/admin/config.yml`.

**Essayer en local (sans GitHub)**

```bash
npm run cms     # terminal 1 : petit serveur qui donne à l'éditeur accès aux fichiers
npm run dev     # terminal 2
```
Ouvrir http://localhost:4321/admin/ → « Login ». Les modifications sont écrites directement dans `src/content/…` et visibles aussitôt sur http://localhost:4321.

**En ligne**

L'éditeur se connecte avec un compte GitHub (seuls les membres du dépôt peuvent publier). Le mode *editorial workflow* est activé : chaque enregistrement crée une pull request « Draft → In review → Ready », le build la vérifie, la publication la fusionne et le site se met à jour en ~1 min.

GitHub exige un petit service d'authentification (OAuth). Deux options :

1. **Hébergement Netlify** (le plus simple) : héberger le site sur Netlify (gratuit) au lieu de GitHub Pages, créer une *OAuth App* GitHub, l'enregistrer dans Netlify (Site settings → Access control → OAuth), et supprimer la ligne `base_url` de `config.yml`.
2. **Rester sur GitHub Pages** : déployer un proxy OAuth gratuit sur Cloudflare Workers (par ex. [sveltia-cms-auth](https://github.com/sveltia/sveltia-cms-auth), compatible Decap), puis renseigner son URL dans `base_url`.

Dans les deux cas : remplacer `repo` dans `public/admin/config.yml` et `SITE.repo` dans `src/config.ts`.

**À savoir**
- Le premier enregistrement d'une fiche via l'éditeur reformate son en-tête YAML (indentation, guillemets) : c'est sans effet sur le contenu.
- La liste des mesures est contrôlée ; pour en ajouter une, l'ajouter aux `options` du champ `measurements` dans `config.yml`.
- Si vous ajoutez un champ au schéma (`src/content.config.ts`), ajoutez-le aussi dans `config.yml`.

## 8. Pistes pour la suite

- Campagne de vérification des 177 outils (statut, dépôt de code, dernière version) — scriptable via l'API GitHub / Software Heritage.
- Ajouter les outils récents (deep learning : PlantCV v4, RootPainter, Cellpose, SAM-based pipelines, ChronoRoot…).
- Lien croisé avec bio.tools / BIII (identifiants), et export RO-Crate.
- Page « Benchmarks » reliant datasets avec vérité terrain et outils.
- Archivage annuel du catalogue sur Zenodo (DOI citable par version).
