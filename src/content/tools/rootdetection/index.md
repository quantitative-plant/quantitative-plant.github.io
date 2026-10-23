---
title: RootDetection
slug: rootdetection
added: '2012-07-04'
status: unverified
organs:
- root-system
measurements:
- length
automation:
- automated
- semi-automated
- manual
platforms:
- windows
- macos
- linux
license:
- freeware
developer: Labutils
website: http://www.labutils.de/rd.html
download: http://www.labutils.de/download/rootdetection-0.1.2.zip
logo: ./logo.webp
gallery:
- src: ./rootdetection1.webp
  caption: 'Source: Labutils'
- src: ./rootdetection2.webp
  caption: 'Source: Labutils'
- src: ./rootdetection3.webp
  caption: 'Source: Labutils'
description_source: LabUtils website
input_formats:
- any
export_formats:
- csv
- xlsx
- sqlite
species:
- arabidopsis
- seedling
legacy_url: /software/rootdetection
draft: false
---

RootDetection is an automated tool for evaluating photographs of plant roots. It detects single strand roots, traces their paths and measures the resulting lengths - completely automatic.All results are written to an embedded database and can be exported as MS Excel or CSV files.RootDetection also provides tools for manually tracing features like hypocotyls or side roots.RootDetection generated data is stored in an SQLite database, which can also be accessed by our additional R-package for data visualization.
