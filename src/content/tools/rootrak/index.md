---
title: RooTrak
slug: rootrak
added: '2012-03-25'
status: unverified
organs:
- root-system
measurements:
- 3d-reconstruction
automation:
- semi-automated
platforms:
- windows
license:
- freeware
developer: Center for Plant Integrative Biology @ University of Nottingham
website: https://www.nottingham.ac.uk/research/groups/cvl/software/rootrak.aspx
download: http://sourceforge.net/projects/rootrak/
doi: 10.1186/1746-4811-9-8
logo: ./logo.webp
gallery:
- src: ./rootrak-2.webp
  caption: 'Source: www.cpib.ac.uk'
input_formats:
- micro-ct-image-sequence
species:
- mature
- seedling
legacy_url: /software/rootrak
draft: false
---

X-ray Micro Computed Tomography (µCT) is an invaluable tool for visualizing plant root systems within their natural soil environment. However, variations in the X-ray attenuation values of root material and the overlap in attenuation values between roots and soil caused by water and organic materials represent major challenges to data recovery. RooTrak views µCT data as a sequence of images through which root objects appear to move as the x-y cross-sections are traversed along the z-axis of the image stack. RooTrak exploits multiple, local models of root appearance, each built while tracking a specific segment, to identify new root material. It requires minimal user interaction and is able to adapt to changing root density estimates. The model-guided search for root material arising from the adoption of a visual tracking framework makes RooTrak less sensitive to the natural ambiguity of X-ray attenuation data than previous approaches. RooTrak can successfully extract a range of root architectures from the surrounding soil and promises to facilitate future root phenotyping efforts.

Modified from: Mairhofer et al. (2012) Plant Physiology 159(2) 561-569
