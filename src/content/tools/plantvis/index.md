---
title: PlantVis
slug: plantvis
added: '2013-07-01'
status: unverified
organs:
- single-root
measurements:
- velocity-profile
automation:
- automated
platforms:
- windows
- macos
- linux
license:
- on-request
developer: Phytocomp @ James Hutton Institute
website: https://www.hutton.ac.uk/sites/default/files/documents/posters/valentine/PlantVis.pdf
download: https://phytocomp.hutton.ac.uk/plantvis2D.html
doi: 10.1007/s00138-009-0207-x
logo: ./logo.webp
gallery:
- src: ./plantvis-1.webp
  caption: 'Source: PlantVis website'
citation: Estimating the motion of plant root cells from in vivo confocal laser scanning microscopy images — Timothy J. Roberts, Stephen J. McKenna, Cheng-Jin Du, Nathalie Wuyts, Tracy A. Valentine, A. Glyn Bengough — 2010, Machine Vision and Applications, 21:921–939
description_source: PlantVis website
input_formats:
- any
export_formats:
- xlsx
- txt
- csv
species:
- arabidopsis
legacy_url: /software/plantvis
draft: false
---

This software is designed to estimate the motion of patches of pixels obtained in fluorescence images from a Confocal Laser Microscope. Displacements are reported to 0.1 pixel resolution, and the confidence of these estimates is also reported.

PlantVis generates large output files containing the coordinates of tracked pixels, the estimated displacement of these pixels between images, and an estimate of the confidence that these displacements are correct.  This output needs to be analysed further – we do this using a series of scripts written in R.  This is a very flexible approach, but does require the user to obtain a reasonable degree of proficiency with using R.
