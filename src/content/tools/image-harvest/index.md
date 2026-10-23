---
title: Image Harvest
slug: image-harvest
added: '2016-05-09'
status: unverified
organs:
- shoot
measurements:
- surface
- convex-hull
- width
- height
- diameter
automation:
- automated
platforms:
- macos
- windows
- linux
license:
- open-source
- freeware
developer: University of Nebraska-Lincoln
website: https://git.unl.edu/aknecht2/ih/
download: http://cropstressgenomics.org/data/html/index.html
doi: 10.1093/jxb/erw176
pmid: '27141917'
logo: ./logo.webp
gallery:
- src: ./screen-shot-2016-05-09-at-10.33.16.webp
  caption: 'Source: Journal of Experimental Botany'
- src: ./screen-shot-2016-05-09-at-10.33.19.webp
  caption: 'Source: Journal of Experimental Botany'
description_source: Image Harvest webpage
input_formats:
- any
export_formats:
- csv
species:
- any
legacy_url: /software/image-harvest
draft: false
---

Image Harvest (ih) is an open-source Python library for processing and analyzing plant images. The software uses OpenCV for image processing, and SciPy for statistics. Besides inclusion of stand-alone scripts to access processing and statistics functions, ih is integrated with Pegasus to create and submit workflows to super computers.

Many software tools already exist to perform image analysis. The ability to create distributed computing workflows is one of the features that makes ih distinct. Workflow generation is completely adaptable to any input, and can be customized using many different modular processing components.
