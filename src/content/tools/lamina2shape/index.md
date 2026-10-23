---
title: Lamina2Shape
slug: lamina2shape
added: '2013-04-17'
status: unverified
organs:
- leaf
measurements:
- length
- shape
- surface
automation:
- automated
platforms:
- windows
- macos
requires:
- matlab
developer: INRA
doi: 10.1016/j.compag.2009.10.009
logo: ./logo.webp
gallery:
- src: ./lamina2shape.webp
  caption: 'Source: Computers and Electronics in Agriculture @ Elsevier'
citation: Lamina2Shape—an image process- ing tool for an explicit description of lamina shape tested on winter wheat (Triticum aestivumL.). — Dornbusch T, Andrieu B — 2010, Computers and Electronics in Agriculture, 70:217–224
description_source: Dornbusch and Andrieu (2010) Computers and Electronics in Agriculture, 70:217–224
species:
- monocot
legacy_url: /software/lamina2shape
draft: false
---

Measurement of dimensions, area and shape of individual laminae is required in many agronomic studies, especially in spite of the increasing use of 3D crop models. To assess variation in lamina shape quantitatively, usually a large number of samples are required and methods to analyze leaf shape are often laborious and time-consuming.

Lamina2Shape is an algorithm that allows an efficient processing of lamina images to analyze their shape. The software was tested on winter wheat (Triticum aestivum L. cv. Soissons). There, images of laminae were obtained using a flat-bed scanner. Using these images, laminae were discriminated from a unicolored background based on thresholds for the ratio of pixel values (0 ≤ I ≤ 255) in the red, green and blue channels (Iblue/Ired ≤ 1.23 and Iblue/Igreen/ ≤ 1.10). Following, a numerical lamina width function w(l) is computed for each lamina in the image as an explicit description of their dimensions (length, width, and area) and shape.

The accuracy of the algorithm was assessed by tests performed for the two main steps of the procedure: background discrimination and computation of w(l). The accuracy of background discrimination was tested by comparing values for area measured by manual cropping of laminae to the corresponding values computed with Lamina2Shape. Both yielded almost the same results. The accuracy of computation of w(l) was tested using images of predefined shape simulated with a lamina shape model. The algorithm was able to re-compute the predefined shape with high accuracy.
