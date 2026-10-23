---
title: IJ_Rhizo
slug: ij-rhizo
added: '2013-07-01'
status: unverified
organs:
- root-system
measurements:
- length
- diameter
automation:
- automated
platforms:
- windows
- macos
- linux
license:
- open-source
developer: Alain Pierret @ Institut de Recherche pour le Developpement
website: https://sites.google.com/site/apierret02/
download: https://www.dropbox.com/s/78ag97gdc99iel3/IJ_Rhizo_v0beta.txt
doi: 10.1007/s11104-013-1795-9
logo: ./logo-2.webp
gallery:
- src: ./ijrhizo-1.webp
- src: ./ijrhizo-2.webp
citation: 'IJ_Rhizo: an open-source software to measure scanned images of root samples — Alain Pierret & Santimaitree Gonkhamdee & Christophe Jourdan & Jean-Luc Maeght — 2013 Plant Soil'
input_formats:
- jpg
export_formats:
- txt
species:
- any
legacy_url: /software/ij-rhizo
draft: false
---

IJ_Rhizo is an ImageJ macro for the batch processing of scanned images of root samples physically separated from soil by washing. IJ_Rhizo automatically generates root length and radius measurements. Being based on a public domain, Java image processing package, IJ_Rhizo is free of charge and platform-independent. IJ_Rhizo offers a simple GUI so that it can be used by end-users with limited computer literacy. This GUI allows to customize: image resolution; the size of image border to be excluded from processing; background particle cleaning; root length correction including the Kimura estimator; and the choice of automatic versus user-defined thresholding. In addition, the macro is also fully modifiable to accommodate the specific needs of more advanced users. IJ_Rhizo generates, in addition to the main “ResultAll.txt” output file and for each image analyzed, a root radius distribution file, stored as a text file and named using the input image name exclusive of the original extension.

## Installation & usage

ImageJ must be installed prior to running the script as a macro.  Morphological Operators for ImageJ must be installed (download as a single zip file from: <a href="http://www.dentistry.bham.ac.uk/landinig/">http://www.dentistry.bham.ac.uk/landinig/</a> and copy to ImageJ's "plugins" directory)
