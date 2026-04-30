# Data Processing Examples
Example Scripts for processing satellite data

Python environment included using uv as pyproject.toml and uv.lock.

---

## SWOT
**Notebook** `SWOT_LR_Height.ipynb`  
Local download and plotting of LR Sea Surface Height data over the Canadian Arctic Archipelago.

**Notebook** `SWOT_PIXC_AmbiguityCorrection.ipynb`  
Manual ambiguity correction of SWOT HR PIXC data using a Gaussian Mixture Model. Based on [this](https://podaac.github.io/tutorials/notebooks/datasets/SWOT_PIXC_PhaseUnwrap_localmachine.html) tutorial.

**Notebook** `SWOT_Backscatter.ipynb`  
Backscatter detection of surface water on Amery Ice Shelf and comparison to Sentinel-2, despite cloudy weather.

**Notebook** `SWOT_PlotCycle.ipynb`  
Local download and plotting of HR data over Amery Ice Shelf for one cycle of SWOT.

## ICESat-2
**Notebook** `EarthaccessEx.ipynb`  
Downloading and plotting ICESat-2 data on David Glacier using earthaccess.

**Notebook** `IcepyxEx.ipynb`  
Downloading and plotting ICESat-2 data using icepyx

**Notebook** `SlideruleEx.ipynb`  
Downloading and plotting ICESat-2 data using sliderule

## GNSS

**Notebook** `GNSS_WhillansEvent_Kriging.ipynb`  
Using RMagic and the [Fields](10.32614/CRAN.package.fields) package to Krig velocity during a Whillans Ice Plain stick slip event.

## Seismic

**Notebook** `Obspy_IRIS_Download.ipynb`  
Use Obspy's FDSN massdownloader to download and make a dayplot of Whillans local station XS 1001.

## WhillansSeismic

**Notebook** `WhillansSeismic_Ex.ipynb`  
Use Obspy's FDSN module to get and calculate the envelope of a Whillans Stick Slip event recorded on VNDA.

