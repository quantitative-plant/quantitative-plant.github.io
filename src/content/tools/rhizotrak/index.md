---
title: rhizoTrak
slug: rhizotrak
added: '2019-02-13'
status: unverified
organs:
- root-system
measurements:
- length
- diameter
- topology
automation:
- manual
platforms:
- windows
- macos
- linux
license:
- open-source
- freeware
developer: Martin Luther University Halle-Wittenberg and Leipzig University
website: https://prbio-hub.github.io/rhizoTrak/
download: https://prbio-hub.github.io/rhizoTrak/pages/installation.html
doi: 10.1101/547604
logo: ./logo.webp
gallery:
- src: ./screenshot-2019-02-13-at-18.24.27.webp
- src: ./screenshot-2019-02-13-at-18.24.32.webp
- src: ./screenshot-2019-02-13-at-18.25.06.webp
input_formats:
- mini rhizotron images
export_formats:
- rsml
- csv
species:
- any
legacy_url: /software/rhizotrak
draft: false
---

rhizoTrak is:

<ul>
<li> an open source tool for flexible and efficient manual annotation of complex time-series minirhizotron images </li> 
<li> building on TrakEM2,</li>
<li> realized as a Fiji plugin available for Windows, Linux, and MacOS.</li>
</ul>

rhizoTrak supports:

<ul>
<li> import and processing of the complete set of images of a time series in one single project</li>
<li> easy browsing through time points which enables to annotate roots by simultaneously considering images of different time points</li>
<li> temporal links between roots in different images which explicitly represented identity of the same physical root via so-called connectors</li>
<li> easy transfer of annotation data of one time point to the next as initial annotation where connectors between corresponding root annotations are automatically established</li>
<li> automatic checks for inconsistencies in root typology due to merging of roots and assistance in solving them</li>
<li> the inherent representation of branching roots by modeling roots as treelines</li>
<li> an individual radius for each node of a treeline, and user-definable status labels for segments of treelines</li>
<li> a large collection of editing operations for root treelines including split and merge, where many of these operations are easily accessible via keyboard shortcuts</li>
<li> different visualization options for treelines and fast hiding and un-hiding of all annotated treelines</li>
<li> redirection of treelines which is important as the upstream and downstream of a root is often not straightforward to be identified in minirhizotron images</li>
<li> import and export of annotations from/to RSML format,</li>
<li> export of root measurements in a tab-separated format including the option to aggregate measurements within images</li>
<li> a plugin mechanism to merge results from automatic segmentation method which are to be implemented as a MiToBo operator</li>
</ul>

## Notes

Works as a FIJI plugin
