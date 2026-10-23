#!/usr/bin/env python3
"""Migre le contenu Kirby 2 (content/*) vers des collections Astro (Markdown + YAML).

Usage : python3 scripts/migrate_kirby.py <dossier_kirby_content> <dossier_src_content>
Idempotent : réécrit les dossiers de sortie à chaque exécution.
"""
import os, re, sys, shutil, json, html
import yaml

SRC, DST = sys.argv[1], sys.argv[2]
SKIP = {"test", "test2", "test-2", "test23", "dummy", "testsoftware", "dan", "dan-ahsnfguiltopne", "feed", "feed2"}
NULLS = {"", "0000", "-1", "-", "unknown", "none", "n/a"}

def parse(path):
    t = open(path, encoding="utf-8-sig", errors="replace").read()
    d = {}
    for blk in re.split(r"\n-{4,}\s*\n", t):
        m = re.match(r"\s*([A-Za-z_ ]+?)\s*:\s*(.*)", blk, re.S)
        if m:
            d[m.group(1).strip().lower()] = m.group(2).strip()
    return d

def val(x):
    x = (x or "").strip()
    return None if x.lower() in NULLS else x

def lst(x, mapping=None, lower=True):
    out = []
    for v in (x or "").split(","):
        v = v.strip()
        if lower: v = v.lower()
        if v.lower() in NULLS: continue
        if mapping: v = mapping.get(v, v)
        if v and v not in out: out.append(v)
    return out

def kirbytext_to_md(s):
    if not s: return ""
    s = re.sub(r"\(link:\s*(\S+)\s+text:\s*([^)]+)\)", r"[\2](\1)", s)
    s = re.sub(r"\(link:\s*(\S+)\s*\)", r"<\1>", s)
    s = re.sub(r"\(email:\s*(\S+)\s*\)", r"<\1>", s)
    s = re.sub(r"</br>|<br\s*/?>", "  \n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()

def split_source(details):
    """Le champ Details finit souvent par '<hr> Source: xxx' : on le sépare."""
    m = re.search(r"\s*<hr\s*/?>\s*Source\s*:\s*(.*)$", details, re.S | re.I)
    if m:
        return details[:m.start()].strip(), m.group(1).strip()
    return details.strip(), None

def norm_doi(x):
    x = val(x)
    if not x: return None
    x = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", x.strip())
    return x if x.startswith("10.") else None

def norm_pmid(x):
    x = val(x)
    return x if x and x.isdigit() else None

def url(x):
    x = val(x)
    if not x: return None
    if not re.match(r"https?://", x): x = "http://" + x
    return x

def citation(x):
    x = val(x)
    if not x: return None
    x = re.sub(r"<[^>]+>", " ", x)
    x = x.replace("**", "")
    x = re.sub(r"[ \t]+", " ", x)
    x = re.sub(r"\s*\n\s*", " — ", x.strip())
    return html.unescape(x).strip(" —")

PLATFORM = {"mac": "macos", "ios": "ios", "android": "android", "windows": "windows", "linux": "linux"}
LICENCE = {"open-source": "open-source", "freeware": "freeware", "commercial": "commercial", "on-demand": "on-request"}
EXPORT = {"excell": "xlsx", "xls": "xlsx", "sql database": "sql", "sqllite": "sqlite", ".mat": "mat",
          "matlab": "mat", ".rr2dat (modified xml)": "xml", "open alea": "mtg", "any type you want": "any"}
PLANT = {"any plant": "any", "corn": "maize", "seedings": "seedling", "grape": "grapevine", "grape vines": "grapevine",
         "grapes only": "grapevine", "an": None, "dicot": "dicot", "seeds": "seed"}
IMAGE = {"jpeg": "jpg", "tif": "tiff", "stereo images": "stereo", "3d-stack": "3d-stack", "3d image stack": "3d-stack",
         "mri 3d image stacks": "3d-stack", "stack": "3d-stack"}
ORGAN = {"any": "general", "whole-plant": "plant"}
MEASURE = {"network structure": "topology", "leaf shape": "shape", "n-seeds": "n-seeds"}

def collect_images(folder, outdir, slug):
    imgs, logo = [], None
    for f in sorted(os.listdir(folder)):
        if not re.search(r"\.(png|jpe?g|gif|webp)$", f, re.I): continue
        clean = re.sub(r"[^a-z0-9.\-]+", "-", f.lower()).strip("-")
        shutil.copy2(os.path.join(folder, f), os.path.join(outdir, clean))
        cap = None
        meta = os.path.join(folder, f + ".txt")
        if os.path.exists(meta):
            cap = val(parse(meta).get("caption"))
        entry = {"src": "./" + clean}
        if cap: entry["caption"] = cap
        if "logo" in clean and not logo:
            logo = "./" + clean
        else:
            imgs.append(entry)
    return logo, imgs

def write(outdir, fm, body):
    os.makedirs(outdir, exist_ok=True)
    fm = {k: v for k, v in fm.items() if v not in (None, [], "")}
    with open(os.path.join(outdir, "index.md"), "w", encoding="utf-8") as fh:
        fh.write("---\n")
        fh.write(yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=1000))
        fh.write("---\n\n")
        fh.write(body.strip() + "\n")

def migrate(section, filename, coll, kind):
    root = os.path.join(SRC, section)
    outroot = os.path.join(DST, coll)
    if not os.path.isdir(root):                          # section absente de cette version du site : on garde l'existant
        return {"migrated": 0, "drafts": [], "duplicates": [], "issues": [], "skipped": True}
    shutil.rmtree(outroot, ignore_errors=True)
    os.makedirs(outroot)
    report = {"migrated": 0, "drafts": [], "duplicates": [], "issues": []}
    seen = {}
    for e in sorted(os.listdir(root)):
        folder = os.path.join(root, e)
        p = os.path.join(folder, filename)
        if not os.path.exists(p): continue
        if e in SKIP: continue                           # pages de test du panel Kirby
        visible = bool(re.match(r"^\d+-", e))           # convention Kirby : préfixe numérique = page visible
        slug = re.sub(r"^\d+-", "", e).lower().replace("_", "-")
        if slug in seen:                                  # doublons dans l'ancien site (ex. 011- et 151-image-harvest)
            report["duplicates"].append(f"{e} (doublon de {seen[slug]})"); continue
        seen[slug] = e
        d = parse(p)
        out = os.path.join(outroot, slug)
        os.makedirs(out, exist_ok=True)
        logo, imgs = collect_images(folder, out, slug)
        details, src2 = split_source(d.get("details", ""))
        fm = {"title": d.get("title", slug).strip(), "slug": slug}
        if kind in ("tool", "model"):
            systems = lst(d.get("systems"))
            requires = []
            if "matlab" in systems or "matlab" in lst(d.get("licence")): requires.append("matlab")
            other = val(d.get("other"))
            if other and re.search(r"imagej|fiji", other, re.I): requires.append("imagej")
            if other and re.search(r"web browser|online|cyverse|web", other, re.I): systems.append("web")
            fm.update({
                "added": val(d.get("date")),
                "status": "deprecated" if "deprecated" in systems else "unverified",
                "organs": lst(d.get("organ"), ORGAN),
                "measurements": lst(d.get("measurement"), MEASURE),
                "automation": lst(d.get("automation")),
                "platforms": [PLATFORM.get(s, s) for s in systems if s in PLATFORM or s == "web"],
                "requires": requires,
                "license": [LICENCE[l] for l in lst(d.get("licence")) if l in LICENCE],
                "input_formats": [v for v in lst(d.get("image"), IMAGE) if v and len(v) < 25],
                "export_formats": [v for v in lst(d.get("export"), EXPORT) if v],
                "species": [v for v in lst(d.get("plant"), PLANT) if v and len(v) < 25],
            })
        else:
            n = val(d.get("numimages"))
            fm.update({
                "added": val(d.get("date")),
                "organs": lst(d.get("organ"), ORGAN),
                "species": [v for v in lst(d.get("plant"), PLANT) if v],
                "n_images": int(n) if n and n.isdigit() else None,
                "ground_truth": (d.get("groundtruth", "").strip().lower() == "yes"),
            })
        fm.update({
            "developer": val(d.get("developer")),
            "website": url(d.get("webpage")),
            "download": url(d.get("download")),
            "doi": norm_doi(d.get("doi")),
            "pmid": norm_pmid(d.get("pmid")),
            "citation": citation(d.get("article")),
            "description_source": val(d.get("source")) or src2,
            "logo": logo,
            "gallery": imgs,
            "draft": not visible,
            "legacy_url": f"/{ {'tool':'software','dataset':'dataset','model':'model'}[kind] }/{slug}",
        })
        body = kirbytext_to_md(details)
        add = val(d.get("additional"))
        if kind != "dataset" and other and other not in ("-",):
            body += "\n\n## Notes\n\n" + kirbytext_to_md(other)
        if add:
            body += "\n\n## Installation & usage\n\n" + kirbytext_to_md(add)
        write(out, fm, body)
        report["migrated"] += 1
        if not visible: report["drafts"].append(slug)
        if not fm.get("website") and not fm.get("download"): report["issues"].append(f"{slug}: aucun lien")
        if not logo: report["issues"].append(f"{slug}: pas de logo")
    return report

if __name__ == "__main__":
    rep = {
        "tools": migrate("1-software", "softwarearticle.txt", "tools", "tool"),
        "datasets": migrate("2-dataset", "datasetarticle.txt", "datasets", "dataset"),
        "models": migrate("3-model", "modelarticle.txt", "models", "model"),  # absent de quantitative_plant
    }
    print(json.dumps({k: {"migrated": v["migrated"], "drafts": v["drafts"], "duplicates": v["duplicates"], "n_issues": len(v["issues"])} for k, v in rep.items()}, indent=1))
    json.dump(rep, open(os.path.join(DST, "..", "..", "migration-report.json"), "w"), indent=1, ensure_ascii=False)
