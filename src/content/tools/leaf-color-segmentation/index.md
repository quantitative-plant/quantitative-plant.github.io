---
title: Leaf Color Segmentation
slug: leaf-color-segmentation
added: '2013-06-03'
status: unverified
organs:
- rosette
measurements:
- surface
- convex-hull
automation:
- automated
platforms:
- windows
- macos
requires:
- matlab
license:
- freeware
developer: Scientific Computing Research Unit @ Helmholtz Zentrum München
website: http://www.helmholtz-muenchen.de/en/ibb/isp/
download: http://www.helmholtz-muenchen.de/en/ibb/isp/colorsegmentation_0.2.zip
doi: 10.1071/FP12323
logo: ./logo.webp
gallery:
- src: ./leafcolor-1.webp
  caption: 'Source: software webpage'
- src: ./leafcolor-2.webp
  caption: 'Source: software webpage'
citation: A segmentation procedure using colour features applied to images of Arabidopsis thaliana — Ruben Ispiryan, Igor Grigoriev, Wolfgang zu Castell, and Anton R Schäffner — 2013, Functional Plant Biology
description_source: Software webpage
input_formats:
- any
export_formats:
- xlsx
species:
- arabidopsis
legacy_url: /software/leaf-color-segmentation
draft: false
---

The library ‘colorsegmentation’ is designed to separate objects in series of images. It is based on the color features of objects. For each object type (flower, leaf, soil, etc) user should specify few pixels by clicking on the training image on the corresponding object. In an excel file (version 2003) the regions for each color feature are determined based on the visual inspection. Using this configuration excel file, images are segmented and the objects are separated.
