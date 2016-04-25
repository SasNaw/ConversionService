# ConversionService
The purpose of this service is to convert images into [deep zoom images](https://msdn.microsoft.com/en-us/library/cc645077(v=vs.95).aspx) (dzi). Valid input formats for this service are:
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

[Deepzoom.py](https://github.com/openzoom/deepzoom.py) is used for the actual conversion into dzi.

## Installation
    git clone https://github.com/SasNaw/ConversionService.git

## Example
For help:

    python ConversionService -h

To run:

    python ConversionService -i <input folder>

## Dependencies
- [deepzoom.py](https://github.com/openzoom/deepzoom.py)

    git clone https://github.com/openzoom/deepzoom.py.git<br>
    cd deepzoom.py<br>
    python setup.py install

