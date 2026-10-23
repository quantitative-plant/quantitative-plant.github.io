---
title: RootTrace
slug: roottrace
added: '2011-06-18'
status: unverified
organs:
- root-system
- single-root
measurements:
- length
- curvature
- n-branches
automation:
- automated
platforms:
- windows
license:
- open-source
- freeware
developer: Center for Plant Integrative Biology @ University of Nottingham
website: https://www.nottingham.ac.uk/research/groups/cvl/software/roottrace.aspx
download: http://sourceforge.net/projects/roottrace/
doi: 10.1093/bioinformatics/btr126
logo: ./logo.webp
gallery:
- src: ./roottrace-1.webp
  caption: 'Source: CPIB, www.cpib.ac.uk'
- src: ./roottrace-2.webp
  caption: 'Source: CPIB, www.cpib.ac.uk'
description_source: RootTrace website (CPIB)
input_formats:
- time-series
export_formats:
- csv
species:
- arabidopsis
- seedling
legacy_url: /software/roottrace
draft: false
---

RootTrace is a software tool being developed at CPIB to allow the automatic and high throughput measure of root length, and extra associated measures such as curvature.

The user must supply start points for each root, and exemplar patches of nearby background. The software will then trace the main root to the tip, in every image in a timeseries, and record the results.

The original RootTrace tool has proved successful in measuring primary root lengths across time series image data. Biologists have shown interest in using the tool to address further problems, namely counting lateral roots to use as parameters in screening studies, and measuring highly curved roots. To address this, the software has been extended to count emerged lateral roots, and the tracking model extended so that strongly curved and agravitropic roots can be now be recovered.
