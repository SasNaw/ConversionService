# ConversionService
The purpose of this service is to convert images into deep zoom images (dzi, see https://msdn.microsoft.com/en-us/library/cc645077(v=vs.95).aspx for further information). Valid input formats for this service are:
* .bif
* .mrxs
* .npdi
* .scn
* .svs
* .svslide
* .tif
* .tiff
* .vms
* .vmu
Deepzoom.py is used for the actual conversion (see https://github.com/openzoom/deepzoom.py) into dzi.

## Installation
<code>
https://github.com/SasNaw/ConversionService.git
</code>

## Example
For help:
<code>
python ConversionService -h
</code>
To run:
<code>
python ConversionService -i <input folder>
</code>

## Dependencies
* deepzoom
<code>
git clone https://github.com/openzoom/deepzoom.py.git
cd deepzoom.py
python setup.py install
</code>
