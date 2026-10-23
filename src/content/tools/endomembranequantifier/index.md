---
title: Endomembrane Quantifier
slug: endomembranequantifier
added: '2013-04-23'
status: unverified
organs:
- cell
measurements:
- localisation
- width
- length
- n-spots
- shape
automation:
- automated
platforms:
- windows
license:
- freeware
developer: Robatzek lab @ Sainsbury Laboratory
website: https://sourceforge.net/projects/bioimage/
download: http://sourceforge.net/projects/bioimage/files/Endosome%20Detection/
doi: 10.1104/pp.110.160325
logo: ./logo.webp
gallery:
- src: ./edomembrane-2.webp
  caption: Copyrighted by the American Society of Plant Biologists. Reprinted with permission
- src: ./endomembrane-1.webp
  caption: Copyrighted by the American Society of Plant Biologists. Reprinted with permission
input_formats:
- microscopy
- flex files
species:
- arabidopsis
legacy_url: /software/endomembranequantifier
draft: false
---

EndomembraneQuantifier and EndomembranetCoLocQuantifier are two algorithms and software implementations for quantifying and identifying colocalized spot-like objects.

Images taken by high content and high-throughput confocal microscopy were analyzed with the image processing software Acapella (version 2.0; Perkin-Elmer). Based on an earlier developed algorithm referred to as the Endomembrane script, we designed an algorithm to robustly detect and quantify spots in one channel (GFP), which can subtract background autofluorescence signals in the same channel. In particular, spots were initially detected and then filtered based on their roundness, intensity, area, length, and width.

Additionally, EndomembraneCoLocQuantifier detects vesicles labeled with two different flourophores (e.g. GFP and RFP) and determines the amount of co-localization between these differentially labeled vesicles.

## Notes

Require Acapella to run
