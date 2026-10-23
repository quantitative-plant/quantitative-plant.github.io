---
title: Maize Kernel-Ear-Cob Analysis
slug: maize-kernel-ear-cob-analysis
added: '2016-09-07'
status: unverified
organs:
- fruit
measurements:
- length
- width
- shape
- count
automation:
- automated
platforms:
- macos
- linux
- windows
license:
- open-source
- freeware
developer: Phytomorph lab @ University of Wisconsin
website: https://bitbucket.org/uwphytomorph/phytomorph/src/master/
download: https://bitbucket.org/uwphytomorph/phytomorph/get/public.zip
doi: 10.1111/tpj.13320
pmid: '27585732'
logo: ./logo.webp
gallery:
- src: ./screen-shot-2016-09-07-at-11.10.50.webp
  caption: 'Source: The Plant Journal'
- src: ./screen-shot-2016-09-07-at-11.10.58.webp
  caption: 'Source: The Plant Journal'
- src: ./screen-shot-2016-09-07-at-11.11.12.webp
  caption: 'Source: The Plant Journal'
description_source: The Plant Journal
input_formats:
- any
export_formats:
- csv
species:
- maize
legacy_url: /software/maize-kernel-ear-cob-analysis
draft: false
---

Grain yield of the maize plant depends on the sizes, shapes, and numbers of ears and the kernels they bear. An automated pipeline that can measure these components of yield from easily-obtained digital images is needed to advance our understanding of this globally important crop. Here we present three custom algorithms designed to compute such yield components automatically from digital images acquired by a low-cost platform. One algorithm determines the average space each kernel occupies along the cob axis using a sliding-window Fourier transform analysis of image intensity features. A second counts individual kernels removed from ears, including those in clusters. A third measures each kernel’s major and minor axis after a Bayesian analysis of contour points identifies the kernel tip. Dimensionless ear and kernel shape traits that may interrelate yield components are measured by principal components analysis of contour point sets. Increased objectivity and speed compared to typical manual methods are achieved without loss of accuracy as evidenced by high correlations with ground truth measurements and simulated data.

## Notes

Run on Cyverse (formerly iPlant)
