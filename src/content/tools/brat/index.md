---
title: BRAT
slug: brat
added: '2014-06-19'
status: unverified
organs:
- single-root
measurements:
- length
- diameter
- orientation
automation:
- automated
platforms:
- windows
- macos
- linux
license:
- open-source
- freeware
developer: Busch lab @ Gregor Mendel Institute
website: https://busch.salk.edu/tools/
download: https://busch.salk.edu/tools/
doi: 10.1105/tpc.114.124032
pmid: '24920330'
logo: ./logo.webp
gallery:
- src: ./brat1.webp
  caption: 'Source: BRAT manual'
- src: ./brat2.webp
  caption: 'Source: BRAT manual'
- src: ./brat3.webp
  caption: 'Source: BRAT user guide'
description_source: BRAT Manual
input_formats:
- any
export_formats:
- txt
species:
- arabidopsis
legacy_url: /software/brat
draft: false
---

The BRAT pipeline is streamlined towards high-throughput quantification of primary root traits in early root growth. The segmentation plugin of the BRAT pipeline reads a set of input images containing multiple plants and tries to detect the objects of interest (plants) in the image. It measures multiple basic traits of the primary root (e. g. root length, root width, root topology and growth direction) and writes the results into a file. Summary statistics for multiple individuals of one genotype are created too.  The plugin is able to process both, independent images and time series images (in this case root growth rates are calculated automatically). The detection of roots is not dependent on their growth direction (i.e. it works for a gravitropic roots as well).  There are only very few parameters, the user has to provide, before the plugin starts its work and the segmentation doesn’t require user interaction. Plug-ins for quality control of the results are included. 

The plugins are developed for the platform independent and freely available Fiji image processing software that can be run on Windows, Linux and Mac OS. The image-processing can be alternatively performed on a compute cluster to decrease processing times and the authors can provide help installing the software on a cluster.
