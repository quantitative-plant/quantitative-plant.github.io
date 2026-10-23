---
title: Balloon Plugin
slug: balloon-plugin
added: '2013-05-04'
status: unverified
organs:
- cell
measurements:
- shape
- surface
automation:
- semi-automated
platforms:
- macos
- linux
- windows
license:
- freeware
developer: Lionel Dupuy @ James Hutton Institute
website: https://imagej.net/imagej-wiki-static/Balloon
download: https://github.com/fiji/BalloonSegmentation/releases/tag/BalloonSegmentation_-3.0.1
doi: 10.1038/nmeth.1940
pmid: '22466793'
logo: ./logo.webp
gallery:
- src: ./balloon-1.webp
  caption: 'Source: Fiji website'
- src: ./balloon-2.webp
  caption: 'Source: Archiroot website'
input_formats:
- any
export_formats:
- txt
species:
- any
legacy_url: /software/balloon-plugin
draft: false
---

Balloon Plugin is a Fiji plugin that allows the segmentation off cell wall boundaries from microscopy images and to extract cell architectures . It uses a physical “balloon inflation” algorithm for finding the cell boundaries from 8bits images. Features include:

- Extraction of lists of individual cell shapes

- The determination of the cells being in contact each other

- All previous segmentation steps are automatic, but it is possible to make manual modifications at each step;

- Settings are saved in properties files for different types of images to be segmented

<hr>
Modified from: Fiji plugin website
