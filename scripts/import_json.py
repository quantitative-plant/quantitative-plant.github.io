#!/usr/bin/env python3
"""Importe les exports JSON (data/import/{tools,datasets,models}.json) dans src/content/.

- Le JSON fait foi pour la liste des entrées et leurs champs structurés.
- Les fiches existantes sont mises à jour en conservant : description (corps Markdown), logo, captures,
  date d'ajout, citation, formats, espèces, statut « active » et last_checked.
- Les fiches existantes absentes du JSON passent en brouillon (draft: true) — rien n'est supprimé.
- Rapport détaillé : data/import/import-report.json

Usage : python3 scripts/import_json.py
"""
import json, os, re, glob, datetime
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMPORT = os.path.join(ROOT, "data", "import")
CONTENT = os.path.join(ROOT, "src", "content")
NULLS = {"", "0000", "-1", "-", "na", "n/a", "none", "no", "unknown"}

# Correspondances manuelles nom JSON -> dossier existant (quand le nom a changé)
ALIASES = {
    "tools": {"Assess 2.0": "assess", "Deep Plant Phenomics": "deep-plant-phenotyping"},
    "datasets": {}, "models": {},
}

# Slugs imposés pour les noms difficiles à convertir
SLUGS = {"Pl@ntNet": "plantnet", "Plant 3D (P3D)": "plant-3d", "Visual Grain Analyzer (VGA)": "visual-grain-analyzer"}

def slugify(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")

def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())

def val(x):
    x = ("" if x is None else str(x)).strip()
    return None if x.lower() in NULLS else x

def split(x):
    return [t.strip() for t in str(x or "").split(",") if t.strip() and t.strip().lower() not in NULLS]

def mapped(values, mapping, lower=True):
    out = []
    for v in values:
        k = v.lower() if lower else v
        m = mapping.get(k, k) if mapping is not None else k
        for x in (m if isinstance(m, list) else [m]):
            if x and x not in out:
                out.append(x)
    return out

def url(x):
    x = val(x)
    if not x: return None
    if "Expires=" in x and "Signature=" in x:      # liens signés temporaires (déjà expirés)
        REPORT["dropped_expiring_links"].append(x[:90] + "…")
        return None
    return x if re.match(r"https?://", x) else "http://" + x

def doi(x):
    x = val(x)
    if not x: return None
    x = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", x.strip())
    return x if x.startswith("10.") else None

def read_md(path):
    txt = open(path, encoding="utf-8").read()
    _, fm, body = txt.split("---", 2)
    return yaml.safe_load(fm) or {}, body.strip()

def write_md(path, fm, body):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fm = {k: v for k, v in fm.items() if v not in (None, [], "")}
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=1000) + "---\n\n" + (body or "").strip() + "\n")

ORGAN = {"any": "general", "all": "general", "leaves": "leaf", "whole_plant": "plant", "whole-plant": "plant",
         "root": "root-system", "cells": "cell", "basal stem": "stem"}
PLATFORM = {"windows": "windows", "mac": "macos", "macos": "macos", "maco": "macos", "apple": "macos", "linux": "linux",
            "ios": "ios", "android": "android", "web-service": "web", "online": "web",
            "any": ["windows", "macos", "linux"]}
REQUIRES = {"matlab": "matlab", "python": "python", "opencv": "opencv", "rasberry pi": "raspberry-pi"}
LICENSE = {"open-source": "open-source", "open source": "open-source", "open_source": "open-source",
           "freeware": "freeware", "commercial": "commercial", "on-demand": "on-request", "upon_request": "on-request",
           "gplv3+": "open-source", "gpl3": "open-source", "gpl v3+": "open-source", "lgpl": "open-source",
           "cecill-c": "open-source", "creative-common attribution-sharealike 2.0": "open-source"}
LICENSE_NAME = {"gplv3+": "GPL-3.0-or-later", "gpl v3+": "GPL-3.0-or-later", "gpl3": "GPL-3.0", "lgpl": "LGPL",
                "cecill-c": "CeCILL-C", "creative-common attribution-sharealike 2.0": "CC BY-SA 2.0"}
MEASURE = {"network structure": "topology", "area": "surface"}
AUTOMATION = {"automated", "semi-automated", "manual"}
CATEGORY = {"ordinary differential equations / partial differential equations": ["ODE", "PDE"],
            "ordinary differential equations": "ODE", "partial differential equations": "PDE",
            "fspm": "FSPM", "csm": "CSM", "spm": "SPM", "gbcsm": "gbCSM", "ode": "ODE", "fpm": "FPM", "fsm": "FSM",
            "stoichiometric model": "Stoichiometric", "process-based model": "Process-based",
            "statistical": "Statistical", "geometric algorithms": "Geometric"}
SCALE = {"field": "field", "whole_field": "field", "whole_plant": "whole-plant", "plant": "whole-plant",
         "organs": "organ", "organ": "organ", "regional": "regional", "global": "global", "cells": "cell",
         "cell": "cell", "python": None, "any": None}
LANG = {"cpp": "C++", "c++": "C++", "c-sharp": "C#", "net": ".NET", "f90": "Fortran", "no-language-identified": None,
        "xml input file": None}

def licenses(raw):
    vals = [v.lower() for v in split(raw)]
    lic = mapped(vals, {k: v for k, v in LICENSE.items()})
    lic = [l for l in lic if l in {"open-source", "freeware", "commercial", "on-request"}]
    names = [LICENSE_NAME[v] for v in vals if v in LICENSE_NAME]
    return lic, (", ".join(names) or None), ("matlab" in vals)

def existing(coll):
    ex = {}
    for p in glob.glob(os.path.join(CONTENT, coll, "*", "index.md")):
        fm, body = read_md(p)
        ex[p.split(os.sep)[-2]] = (fm, body)
    return ex

def matcher(coll, ex):
    byt = {norm(fm.get("title", "")): k for k, (fm, _) in ex.items()}
    bys = {norm(k): k for k in ex}
    claimed = set()
    def find(name):
        if name in ALIASES[coll]: return ALIASES[coll][name]
        n = norm(re.sub(r"\[.*?\]", "", name))
        return byt.get(n) or bys.get(n)
    return find

KEEP = ["added", "logo", "gallery", "citation", "description_source", "input_formats", "export_formats",
        "species", "last_checked", "source_code", "legacy_url", "website", "download"]

def merge(coll, records, build):
    ex = existing(coll)
    find = matcher(coll, ex)
    seen = set()
    rep = {"updated": [], "created": [], "drafted": [], "collisions": []}
    for name, rec in records.items():
        k = find(name)
        if k and k in seen:
            rep["collisions"].append(f"{name} → {k} déjà utilisé, créé séparément"); k = None
        slug = k or SLUGS.get(name) or slugify(clean_title(name))
        if slug in seen:
            slug = slug + "-2"
        seen.add(slug)
        old_fm, body = ex.get(slug, ({}, ""))
        new = build(name, rec)
        fm = {"title": new.pop("title"), "slug": slug}
        if old_fm.get("added"): fm["added"] = old_fm["added"]
        fm.update(new)
        for key in KEEP:                       # conserver ce que le JSON ne fournit pas
            if old_fm.get(key) and not fm.get(key):
                fm[key] = old_fm[key]
        if old_fm.get("status") == "active" and fm.get("status") != "deprecated":
            fm["status"] = "active"
        fm["draft"] = False
        fm.setdefault("legacy_url", None)
        write_md(os.path.join(CONTENT, coll, slug, "index.md"), fm, body)
        rep["updated" if slug in ex else "created"].append(slug)
    for k, (fm, body) in ex.items():
        if k not in seen and not fm.get("draft"):
            fm["draft"] = True
            write_md(os.path.join(CONTENT, coll, k, "index.md"), fm, body)
            rep["drafted"].append(k)
    return rep

def deprecated(name):
    return bool(re.search(r"\[(deprecated|deptricated)\]", name, re.I))

def clean_title(name):
    name = re.sub(r"<[^>]+>", "", name)                 # balises HTML dans certains noms
    return re.sub(r"\s+", " ", re.sub(r"\s*\[.*?\]\s*", " ", name)).strip()

def build_tool(name, r):
    os_vals = [v.lower() for v in split(r.get("os"))]
    lic, lic_name, lic_matlab = licenses(r.get("licence"))
    requires = mapped([v for v in os_vals if v in REQUIRES], REQUIRES)
    if lic_matlab and "matlab" not in requires: requires.append("matlab")
    pm = val(r.get("pmid"))
    return {
        "title": clean_title(name),
        "status": "deprecated" if ("deprecated" in os_vals or deprecated(name)) else "unverified",
        "organs": mapped(split(r.get("organ")), ORGAN),
        "measurements": mapped(split(r.get("measurement")), MEASURE),
        "automation": [a for a in mapped(split(r.get("automation")), {}) if a in AUTOMATION],
        "platforms": mapped([v for v in os_vals if v in PLATFORM], PLATFORM),
        "requires": requires,
        "license": lic, "license_name": lic_name,
        "developer": val(r.get("developer")),
        "website": url(r.get("home_link")),
        "download": url(r.get("download_link")),
        "doi": doi(r.get("doi")),
        "pmid": pm if pm and pm.isdigit() else None,
    }

def build_dataset(name, r):
    n = (r.get("numimages") or "").strip()
    digits = re.sub(r"[\s,]", "", n)
    pm = val(r.get("pmid"))
    d = doi(r.get("doi"))
    return {
        "title": clean_title(name),
        "status": "deprecated" if deprecated(name) else "unverified",
        "organs": mapped(split(r.get("organ")), ORGAN),
        "n_images": int(digits) if digits.isdigit() else None,
        "n_images_text": n if n and not digits.isdigit() else None,
        "ground_truth": (r.get("groundtruth") or "").strip().lower() == "yes",
        "developer": val(r.get("developer")),
        "website": url(r.get("home_link")),
        "download": url(r.get("download_link")),
        "doi": d,
        "pmid": pm if pm and pm.isdigit() else None,
        "paper_url": pm if pm and pm.startswith("http") else (val(r.get("doi")) if not d and (r.get("doi") or "").startswith("http") else None),
    }

def build_model(name, r):
    lic, lic_name, _ = licenses(r.get("Licence"))
    raw_doi = val(r.get("Doi"))
    d = doi(raw_doi)
    integ = [v for v in split(r.get("Platform_Integration")) if v.lower() != "no"]
    return {
        "title": clean_title(name),
        "status": "deprecated" if deprecated(name) else "unverified",
        "category": mapped(split(r.get("Model_category")), CATEGORY),
        "organs": mapped(split(r.get("PlantPart")), ORGAN),
        "scales": mapped(split(r.get("Scale")), SCALE),
        "predictions": mapped([v.replace("-", " ") for v in split(r.get("Prediction"))], None),
        "species": mapped([v.replace("-", " ").replace("Perenial", "Perennial") for v in split(r.get("Species"))], None),
        "languages": mapped(split(r.get("Language")), LANG, lower=True) and
                     [LANG.get(v.lower(), v) for v in split(r.get("Language")) if LANG.get(v.lower(), v)],
        "platforms": mapped([v.lower() for v in split(r.get("Systems")) if v.lower() in PLATFORM], PLATFORM),
        "license": lic, "license_name": lic_name,
        "integration": integ,
        "doi": d,
        "website": raw_doi if raw_doi and not d and raw_doi.startswith("http") else None,
    }

REPORT = {"dropped_expiring_links": []}
if __name__ == "__main__":
    load = lambda f, k: json.load(open(os.path.join(IMPORT, f), encoding="utf-8"))["json"][k]
    REPORT["tools"] = merge("tools", load("tools.json", "tools"), build_tool)
    REPORT["datasets"] = merge("datasets", load("datasets.json", "datasets"), build_dataset)
    REPORT["models"] = merge("models", load("models.json", "models"), build_model)
    REPORT["date"] = datetime.date.today().isoformat()
    json.dump(REPORT, open(os.path.join(IMPORT, "import-report.json"), "w"), indent=1, ensure_ascii=False)
    for k in ("tools", "datasets", "models"):
        r = REPORT[k]
        print(f"{k}: {len(r['updated'])} mises à jour, {len(r['created'])} créées, {len(r['drafted'])} passées en brouillon {r['drafted']}, collisions {r['collisions']}")
    print("liens expirés supprimés :", len(REPORT["dropped_expiring_links"]))
