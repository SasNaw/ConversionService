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
* .vmu<br>
Deepzoom.py is used for the actual conversion (see https://github.com/openzoom/deepzoom.py) into dzi.

## Installation
<code>
git clone https://github.com/SasNaw/ConversionService.git
</code>

## Example
For help:<br>
<code>
python ConversionService -h
</code>

To run:<br>
<code>
python ConversionService -i &lsaquo;input folder&rsaquo;
</code>

## Dependencies
* deepzoom

<code>
git clone https://github.com/openzoom/deepzoom.py.git<br>
cd deepzoom.py<br>
python setup.py install
</code>
