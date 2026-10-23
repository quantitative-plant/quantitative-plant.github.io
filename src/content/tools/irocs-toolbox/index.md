---
title: iRoCS Toolbox
slug: irocs-toolbox
added: '2014-01-13'
status: unverified
organs:
- single-root
- cell
measurements:
- 3d-reconstruction
- localisation
- diameter
- volume
automation:
- automated
- semi-automated
platforms:
- windows
- linux
license:
- open-source
- freeware
developer: Computer Vision Group @ University of Freiburg
website: http://lmb.informatik.uni-freiburg.de/lmbsoft/iRoCS
download: http://lmb.informatik.uni-freiburg.de/lmbsoft/iRoCS
doi: 10.1111/tpj.12429
pmid: '24417645'
logo: ./logo.webp
gallery:
- src: ./irocs-1.webp
  caption: 'Source: iRoCS webiste'
- src: ./irocs-2.webp
  caption: 'Source: iRoCS webiste'
description_source: iRoCS website
input_formats:
- 3d-stack
species:
- arabidopsis
legacy_url: /software/irocs-toolbox
draft: false
---

The iRoCS Toolbox is an interactive Qt4 analysis tool for attaching the intrinsic Root Coordinate System (iRoCS) to 3-D confocal recordings of the Arabidopsis root apical meristem (RAM). This allows quantitative comparative studies of root populations in a sound and intuitive context.
Main features are:

- 3-D Visualization of the volume in an orthographic view.
- Manual annotation of anatomical reference structures (QC, nuclei)
- Automatic detection and annotation of cells and/or nuclei with several meaningful properties, like position, radius, tissue, cell file, cell cycle state, volume.
- Full control. Any step can be manually corrected and re-fed into the modeling.
- Retrieval and localization of key events like cell divisions
