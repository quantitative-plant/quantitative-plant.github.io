---
title: Canopy Reconstruction
slug: canopy-reconstruction
added: '2014-10-23'
status: unverified
organs:
- shoot
measurements:
- surface
- 3d-reconstruction
automation:
- automated
platforms:
- windows
license:
- freeware
- open-source
developer: Center for Plant Integrative Biology @ University of Nottingham
website: https://www.cpib.ac.uk/tools-resources/software/canopy-reconstruction/
download: https://sourceforge.net/projects/canopyreconstruction/
doi: 10.1104/pp.114.248971
pmid: '25332504'
logo: ./logo.webp
gallery:
- src: ./img1.webp
- src: ./img2.webp
description_source: CPIB webpage
input_formats:
- stereo
export_formats:
- ply
species:
- any
legacy_url: /software/canopy-reconstruction
draft: false
---

Our reconstruction work aims to produce accurate and useful models of plants in three dimensions, based on multiple colour images using a low-cost camera. Beginning with an initial point cloud, obtained using standard structure from motion tools, the scene is first filtered, and segmented into small patches that represent sections of leaf surface. Each surface is individually represented by a best-fit plane, and the boundary of each surface is adjusted to better fit the image and modelling data. This adjustment is achieved using the level set method, which optimises the smoothness of each surface, while growing or shrinking them in response to image information and neighbouring surfaces.

## Notes

Command Line tool
