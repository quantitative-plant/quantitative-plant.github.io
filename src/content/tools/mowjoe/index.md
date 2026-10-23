---
title: MowJoe
slug: mowjoe
added: '2018-03-28'
status: unverified
organs:
- leaf
measurements:
- length
- count
- shape
automation:
- automated
platforms:
- windows
- macos
license:
- freeware
- open-source
developer: Max Planck Institute for Plant Breeding Research
website: https://github.com/Henrik86/Mow_Joe/tree/v1.4
download: https://github.com/Henrik86/Mow_Joe/tree/v1.4
doi: 10.1186/s13007-018-0290-y
logo: ./logo.webp
gallery:
- src: ./screen-shot-2018-03-28-at-13.26.49.webp
- src: ./screen-shot-2018-03-28-at-13.27.04.webp
description_source: Plant Methods article
input_formats:
- any
export_formats:
- csv
species:
- any
legacy_url: /software/mowjoe
draft: false
---

MowJoe is an image processing algorithm that dissects a dissected leaf into leaflets, petiolule, rachis and petioles. It employs image skeletonization to convert leaves into graphs, and thereafter applies algorithms operating on graph structures. This partitioning of a leaf allows the derivation of morphological features such as leaf size, or eccentricity of leaflets. Furthermore, MowJoe automatically places landmarks onto the terminal leaflet that can be used for further leaf shape analysis. It generates specific output files that can directly be imported into downstream shape analysis tools.

## Notes

Runs on MatLab
