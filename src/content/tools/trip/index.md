---
title: TRiP
slug: trip
added: '2015-05-04'
status: unverified
organs:
- shoot
measurements:
- movement
automation:
- automated
platforms:
- macos
- windows
- linux
requires:
- matlab
license:
- open-source
- freeware
developer: Departement of Biological Sciences @ Dartmouth College
website: https://github.com/KTgreenham/TRiP
download: https://github.com/KTgreenham/TRiP/archive/master.zip
doi: 10.1186/s13007-015-0075-5
logo: ./logo.webp
gallery:
- src: ./trip-1.webp
  caption: 'Source: Plant Methods'
- src: ./trip-2.webp
  caption: 'Source: Plant Methods'
citation: 'TRiP: Tracking Rhythms in Plants, an automated leaf movement analysis program for circadian period estimation — Kathleen Greenham, Ping Lou, Sara E Remsen, Hany Farid and Robertson McClung — Plant Methods 2015, 11:33'
description_source: TRiP GitHub page
input_formats:
- jpg
export_formats:
- txt
- png
species:
- dicot
legacy_url: /software/trip
draft: false
---

TRiP is a matlab-based program for estimating circadian period from whole plant image data. TRiP includes a grid-based cropping function that takes each image stack as input and crops the images using grid coordinates to output image stacks for each plant. A motion estimation algorithm is applied to the image stacks and outputs a motion vector for each image over time. The motion vectors are used to estimate circadian period using a single frequency FFT-NLLS method.
