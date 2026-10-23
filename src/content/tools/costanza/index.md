---
title: Costanza
slug: costanza
added: '2013-06-04'
status: unverified
organs:
- cell
measurements:
- localisation
- surface
- color
automation:
- automated
platforms:
- windows
- linux
- macos
license:
- freeware
developer: Computational Biology & Biological Physics @ Lund University
website: https://mybiosoftware.com/costanza-1-0-imagej-plugin-image-segmentation-analyzing-stacks.html
download: http://home.thep.lu.se/~henrik/Costanza/
logo: ./logo.webp
gallery:
- src: ./costanza-1.webp
  caption: 'Source: Costanza user guide'
- src: ./costanza-2.webp
  caption: 'Source: Costanza user guide'
description_source: Computable Plant website
input_formats:
- 3d-stack
export_formats:
- jpg
- xlsx
- csv
species:
- any
legacy_url: /software/costanza
draft: false
---

COnfocal STack ANalyZer Application (Costanza), an ImageJ[1] plugin for segmentation and analyzing stacks of image data. Such data come very often from ﬂuorescent microscopy and this is where Costanza should prove to be most useful. The main purpose of Costanza is to segment nuclei marked cells in three dimensions, making available quantitative measures such as positions, sizes, and average intensities of GFP markers for the segmented compartments. However since a user is given the control on the parameters used by Costanza ﬁlters and image processors, they may be tweaked and combined freely to give good results also for other image processing tasks. The main algorithm is independent of intensity thresholds, allowing for segmentation of data of varying intensity. Costanza assumes a greyscale stack of images as input, and return the result both as cells/intensities marked in images and as an ImageJ data list.

## Notes

ImageJ plugin
