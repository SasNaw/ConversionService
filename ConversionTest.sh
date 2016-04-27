#!/bin/bash

SUCCESS=1
echo ""
echo ""
echo "=== Conversion Service Test ==="
echo ""
mkdir csTest
echo "copying files for testing..."
cp ConversionTest.sh csTest/ConversionTest.sh
cp ConversionService.py csTest/ConversionService.py
cp -r imgTest csTest/imgTest
cd csTest/
echo "done!"
echo ""
echo "start conversion:"
echo ""
python ConversionService.py -i "imgTest/"
echo ""
if [ -d "dzi/" ]; then
	echo "SUCCESS: found output folder!"
	cd dzi/
	# check for testfolders
	# check number of levels
	# check number of files
	
	cd ..
else
	echo "ERROR: no output folder found!"
fi

cd ..
rm -r csTest

if [ $SUCCESS == 1 ]; then 
	echo ""
	echo "TEST SUCCESSFUL!"
	echo ""
	echo ""
else 
	echo ""
	echo "TEST FAILED!"
	echo ""
	echo ""
fi
