---
title: RTipC
slug: rtipc
added: '2014-04-07'
status: unverified
organs:
- root-system
measurements:
- count
- diameter
automation:
- automated
platforms:
- windows
requires:
- matlab
license:
- freeware
developer: Phenomics and Bioinformatics Research Centre @ University of South Australia
website: http://sourceforge.net/projects/RootPhenotypingSuite/
download: http://sourceforge.net/projects/RootPhenotypingSuite/
doi: 10.1007/s11104-014-2071-3
logo: ./logo.webp
gallery:
- src: ./11-59.webp
- src: ./4-60.webp
citation: Root phenotyping by root tip detection and classification through statistical learning — Kumar, P. Huang, C. Cai, J. Miklavcic, S.J., — Plant and Soil, 380, Issue 1-2 , pp 193-209, March 2014.
input_formats:
- any
export_formats:
- txt
species:
- any
legacy_url: /software/rtipc
draft: false
---

Root tip detection is an algorithm combining the use of structural information (root tip, segments, ...) and machine learning techniques to detect, count and classify the root tips of complex root systems.

## Notes

Requires Matlab executor to run

## Installation & usage

Steps for running the executable for root tip detection

1.  Download and install [Matlab compiler runtime for R2013q](http://www.mathworks.com.au/products/compiler/mcr/index.html?s_cid=BB).

2.  Place the executable *root_tip.exe* and machine trained file *zm_gmm4.mat* and all the images in a folder together.  Images should be in *.tif* file format.  Five example files have been attached with this download.

3.  Now simply run the executable.  It will read and process all the files in the folder and generate a *result.txt* file.

4.  The *result.txt* file has the counts of primary and lateral roots.  It also has histogram of root tips as a function of root tip diameter.  The last column is the count of root tips whose diameter could not be determined reliably.

5.  Please refer to the paper for details of implementation.
