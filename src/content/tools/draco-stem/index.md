---
title: DRACO-STEM
slug: draco-stem
added: '2017-03-01'
status: unverified
organs:
- cell
measurements:
- 3d-reconstruction
- topology
automation:
- automated
platforms:
- macos
- windows
- linux
license:
- open-source
developer: Virtual Plant @ Inria
website: https://github.com/VirtualPlants/draco_stem
download: https://github.com/VirtualPlants/draco_stem
doi: 10.3389/fpls.2017.00353
logo: ./logo.webp
gallery:
- src: ./screen-shot-2017-03-01-at-12.52.59.webp
  caption: 'Source: Frontiers in Plant Sciences'
- src: ./screen-shot-2017-03-01-at-12.53.13.webp
  caption: 'Source: Frontiers in Plant Sciences'
- src: ./screen-shot-2017-03-01-at-12.53.35.webp
  caption: 'Source: Frontiers in Plant Sciences'
citation: 'DRACO-STEM : an automatic tool to generate high-quality 3D meshes of meristem tissue at cell resolution. — Cerutti, G., Ali, O., and Godin, C. (2017). — Front. Plant Sci. 8.'
input_formats:
- any
export_formats:
- mtg
species:
- any
legacy_url: /software/draco-stem
draft: false
---

DRACO-STEM  is a two-stage computational pipeline that generates a complete 3D triangular mesh of the tissue volume based on a segmented tissue image stack. DRACO (Dual Reconstruction by Adjacency Complex Optimization) is designed to retrieve the underlying 3D topological structure of the tissue and compute its dual geometry, while STEM (SAM Tissue Enhanced Mesh) returns a faithful triangular mesh optimized along several quality criteria (intrinsic quality, tissue reconstruction, visual adequacy). Quantitative evaluation tools measuring the performance of the method along those different dimensions are also provided. The resulting meshes can be used as input and validation for biomechanical simulations.

<lr>

Source: Frontiers in Plant Science article

## Notes

Work within the OpenAlea pipeline
