---
title: Leaf Processor
slug: leafprocessor
added: '2013-04-16'
status: unverified
organs:
- leaf
measurements:
- length
- width
- perimeter
- shape
- surface
automation:
- automated
platforms:
- windows
- macos
requires:
- matlab
license:
- on-request
developer: Fraunhofer Institute for Factory Operation and Automation IFF
website: https://github.com/Angelovici-Lab/HTP_Image_Analysis/blob/master/LeafProcessor.m
download: https://github.com/Angelovici-Lab/HTP_Image_Analysis/blob/master/LeafProcessor.m
doi: 10.1111/j.1469-8137.2010.03266.x
pmid: '20456045'
logo: ./logo.webp
gallery:
- src: ./leafprocessor-1.webp
  caption: 'Source: Fraunhofer Institute  IFF'
- src: ./leafprocessor-2.webp
  caption: 'Source: Fraunhofer Institute  IFF'
description_source: Leaf Processor website
input_formats:
- any
species:
- any
legacy_url: /software/leafprocessor
draft: false
---

LeafProcessor software was developed to give biologists and plant breeders a tool that evaluates different leaf geometries.

Core software functions:

- **Organization**: The software fully organizes image data generated in an experiment sorted in keeping with experimental conditions.

- **Segmentation**: Leaves in an image are segmented and marked automatically.

- **Shape attributes**: The software supplies a number of individual attributes with which shapes can be marked manually.

- **Cluster analysis**: Leaves can be automatically combined into groups with highly similar shapes.

- **Classification**: Based on the shape attributes, classification models can be generated and validated to automatically identify plant species or genotypes.

- **Regression**: Regressions models can be created to evaluate available quantitative response variables based on shape.

The software has been used by biologists to obtain important findings about the mechanisms of leaf growth, e.g. based on the distribution of cell division.
