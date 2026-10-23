---
title: PaCeQuant
slug: pacequant
added: '2017-09-21'
status: unverified
organs:
- leaf
measurements:
- shape
- size
- count
- growth
automation:
- automated
platforms:
- linux
- macos
- windows
license:
- open-source
developer: MLU Halle-Wittenberg, iDiv Halle-Jena-Leipzig, IPB Halle
website: http://mitobo.informatik.uni-halle.de/index.php/Applications/PaCeQuant
download: http://mitobo.informatik.uni-halle.de/index.php/Downloads
doi: 10.1104/pp.17.00961
logo: ./logo.webp
gallery:
- src: ./analysis.webp
  caption: 'Source: Related article'
- src: ./characteristics.webp
  caption: 'Source: Related article'
- src: ./comparison.webp
  caption: 'Source: Related article'
- src: ./definitaion-methods.webp
  caption: 'Source: Related article'
- src: ./evaluation.webp
  caption: 'Source: Related article'
- src: ./pacequant-workflow.webp
  caption: 'Source: Related article'
- src: ./phenotypic-analysis.webp
  caption: 'Source: Related article'
citation: 'PaCeQuant: A Tool for High-Throughput Quantification of Pavement Cell Shape Characteristics — Birgit Möller, Yvonne Poeschl, Romina Plötner, Katharina Bürstenbinder — Plant Physiology 2017.'
description_source: 'Source: , et al. "PaCeQuant: A Tool for High-Throughput Quantification of Pavement Cell Shape Characteristics." Plant Physiology Vol. 175, Issue 1 Sep 2017'
input_formats:
- roi or labeled
export_formats:
- jpg
- png
species:
- any
- arabidopsis
legacy_url: /software/pacequant
draft: false
---

PaCeQuant, an ImageJ-based tool, which provides a fully automatic image analysis workflow for PC shape quantification. PaCeQuant automatically detects cell boundaries of PCs from confocal input images, and enables manual correction of automatic segmentation results or direct import of manually segmented cells. PaCeQuant simultaneously extracts 27 shape features that include global, contour-based, skeleton-based and PC-specific object descriptors. 

In addition, the developers included a method for classification and analysis of lobes at two-cell-junctions and three-cell-junctions, respectively. They provide an R script for graphical visualization and statistical analysis. They validated PaCeQuant by extensive comparative analysis to manual segmentation and existing quantification tools, and demonstrated its usability to analyze PC shape characteristics during development and between different genotypes. 

PaCeQuant thus provides a platform for robust, efficient and reproducible quantitative analysis of PC shape characteristics that can easily be applied to study PC development in large data sets.

## Notes

Package of ImageJ/MiToBo
