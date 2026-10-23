---
title: Callose Measurer
slug: callose-measurer
added: '2013-04-22'
status: unverified
organs:
- cell
measurements:
- callose-deposition
automation:
- automated
platforms:
- windows
license:
- freeware
developer: Robatzek lab @ Sainsbury Laboratory
website: https://sourceforge.net/projects/bioimage/files/Callose/
download: http://sourceforge.net/projects/bioimage/files/Callose/
doi: 10.1186/1746-4811-8-49
pmid: '23244621'
logo: ./logo.webp
gallery:
- src: ./callosemeasurer-1.webp
  caption: 'Source: BMC Plant Methods'
- src: ./callosemeasurer-2.webp
  caption: 'Source: BMC Plant Methods'
- src: ./callosemeasurer-3.webp
  caption: 'Source: BMC Plant Methods'
description_source: Zhou et al. (2012) Plant methods , 8(1), 49
input_formats:
- microscopy
species:
- any
legacy_url: /software/callose-measurer
draft: false
---

CalloseMeasurer is a new software solution for batch-processing large image data sets to quantify callose deposition in plants, a plant immune response triggered by potentially pathogenic microbes. Additionally, by tracking identified callose deposits between multiple images, the software can recognise patterns of how a given filamentous pathogen grows in plant leaves. 

The software has been evaluated with typical noisy experimental images and can be automatically executed without the need for user intervention. The automated analysis is achieved by using standard image analysis functions such as image enhancement, adaptive thresholding, and object segmentation, supplemented by several novel methods which filter background noise, split fused signals, perform edge-based detection, and construct networks and skeletons for extracting pathogen growth patterns. 

To efficiently batch process callose images, we implemented the algorithm in C/C++ within the Acapella™ framework. Using the tool we can robustly score significant differences between different plant genotypes when activating the immune response. We also provide examples for measuring the in planta hyphal growth of filamentous pathogens.

 
The software is an easy-to-use protocol which is executed within the Acapella software system without requiring any additional libraries.

## Notes

Requires Acapella software
