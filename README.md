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

[VIPS](http://www.vips.ecs.soton.ac.uk/index.php?title=VIPS) is used for the conversion into dzi.

## Installation
    git clone https://github.com/SasNaw/ConversionService.git

## Example
To run:

    python ConversionService <input dir> <output dir>
    
The newly converted dzi will be saved in the same folder as the ConversionService operates from, plus "/dzi/<output dir>/".

## Dependencies
- [libvips](https://github.com/jcupitt/libvips)
