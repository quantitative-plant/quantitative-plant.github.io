---
title: CellArchitect
slug: cellarchitect
added: '2017-08-28'
status: unverified
organs:
- cell
- leaf
measurements:
- size
- shape
- count
automation:
- automated
platforms:
- windows
license:
- freeware
developer: Robatzek Group @ The Sainsbury Laboratory
website: https://github.com/TeamMacLean/CellArchitect
download: https://github.com/TeamMacLean/CellArchitect
doi: 10.1111/tra.12505
pmid: '28746801'
logo: ./logo.webp
gallery:
- src: ./charts.webp
  caption: 'Source: Traffic article'
- src: ./microtubule-pattern.webp
  caption: 'Source: Traffic article'
- src: ./workflow.webp
  caption: 'Source: Traffic article'
description_source: Faulkner, Christine, et al. "An automated quantitative image analysis tool for the identification of microtubule patterns in plants." Traffic (2017).
input_formats:
- microscopy
export_formats:
- csv
species:
- arabidopsis
legacy_url: /software/cellarchitect
draft: false
---

CellArchitect is an Acapella-based automated image analysis tool that batch processes images from high throughput confocal microscopy of genetically encoded microtubule markers expressed in Arabidopsis. In particular, CellArchitect is designed to recognise microtubule (MT) and measure MT pattern changes induced by different chemicals. The algorithm is capable of detecting other microfilament structure such as actin as well. Output fields (in a variety of CSV files) quantify features such as size, shape, fluorescent signal intensity, and MT patterns (e.g. MT lengths).

CellArchitect can detect subcellular patterns tagged by actin and endoplasmic reticulum markers. Thus, the platform developed here can be used to automate image analysis of complex subcellular patterns for purposes such as herbicide discovery and mode of action characterisation. The capacity to use this tool to quantitatively characterise cellular responses lends itself to application across many areas of biology.

This software solution performs traditional image analysis functions such as image enhancement, object segmentation, denoise, edge-based measurements, and skeletonisation. When adding new functions to CellArchitect, please add them as external procedures or internal functions to maintain software architecture.

## Notes

Requires Acapella software
