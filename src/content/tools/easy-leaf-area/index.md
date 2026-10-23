---
title: Easy Leaf Area
slug: easy-leaf-area
added: '2014-07-15'
status: unverified
organs:
- leaf
measurements:
- surface
automation:
- automated
platforms:
- windows
license:
- open-source
- freeware
developer: Department of Plant Sciences @ University of California
website: https://github.com/heaslon/Easy-Leaf-Area
download: https://play.google.com/store/apps/details?id=com.heaslon.EasyLeafArea&hl=en-US
doi: 10.3732/apps.1400033
logo: ./logo.webp
gallery:
- src: ./easyleafarea-1.webp
  caption: 'Source: Applications in Plant Sciences, BioOne'
- src: ./easyleafarea-2.webp
  caption: 'Source: Applications in Plant Sciences, BioOne'
citation: 'Easy Leaf Area: Automated Digital Image Analysis for Rapid and Accurate Measurement of Leaf Area — Hsien Ming Easlon and Arnold J. Bloom — Applications in Plant Sciences, 2(7) 2014.'
description_source: Easy Leaf Area website
input_formats:
- tiff
- jpg
export_formats:
- csv
species:
- any
legacy_url: /software/easy-leaf-area
draft: false
---

Easy leaf area is free, open source, software that rapidly measures leaf area in digital images (photographs or scanner images). Easy leaf area uses the RGB value of each pixel to identify leaf and scale regions in each image. After analysis, each highlighted image is written in tiff format to the 'write folder'. A file named 'leafarea.csv' with image names, leaf pixel counts, scale pixel counts, and leaf area in cm^2 is also written to the 'write folder'. Multiple leaves can be measured in the same image
