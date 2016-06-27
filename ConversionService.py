#!/usr/bin/env python

import sys, getopt
import os
from gi.repository import Vips
import subprocess
from subprocess import call

global OUTPUT
OUTPUT = "dzi/"
global TILESIZE
TILESIZE = 256
global OVERLAP
OVERLAP = 0


# check if input parameters are valid
# return input folder if valid, exit otherwise
def checkParams():
	global OUTPUT
	if(len(sys.argv) != 3):
		print("Error: wrong number of parameters!")
		print("Try: python ConversionService.py <input dir> <output dir>")
		sys.exit(2)
	else:
		path = str(sys.argv[1])
		if not(path.endswith("/")):
			path += "/"
		OUTPUT = OUTPUT + str(sys.argv[2])
		if not(OUTPUT.endswith("/")):
			OUTPUT += "/"
		if(os.path.exists(path)):
			print("Input folder is " + path)
			createOutputDir();
			return path
		else:
			print("Input folder " + path + " doesn't exist")
			sys.exit(2)


# get length of file extension for later replacement with .dzi
# param file: file to check
# return: length of file extension, 0 if not valid
def getFileExt(file):
	extLen = 0
	print("checking file extension for " + file + "...")
	#todo: delete, just for testing purposes
	if file.lower().endswith(".jpg"):
		extLen = -3
	elif file.lower().endswith(".bif"):
		extLen = -3
	elif file.lower().endswith(".mrxs"):
		extLen = -4
	elif file.lower().endswith(".ndpi"):
		extLen = -4
	elif file.lower().endswith(".scn"):
		extLen = -3
	elif file.lower().endswith(".svs"):
		extLen = -3
	elif file.lower().endswith(".svslide"):
		extLen = -7
	elif file.lower().endswith(".tif"):
		extLen = -3
	elif file.lower().endswith(".tiff"):
		extLen = -4
	elif file.lower().endswith(".vms"):
		extLen = -3
	elif file.lower().endswith(".vmu"):
		extLen = -3
	if(extLen == 0):
		print("...file extension not found")
	else:
		print("...file extension (" + file[extLen:] + ") found")
	return extLen


# check if output dir exists and create it if necessary
def createOutputDir():
	if os.path.exists(OUTPUT):
		print("found output directory (" + OUTPUT + ")")
	else:
	    print("created output directory (" + OUTPUT + ")")
	    os.makedirs(OUTPUT)


# convert image source into .dzi format and copies all header information
# into [img]_files dir as metadata.txt
# param path: directory of param file
# param file: file to be converted
# param extLen: length of file extension
def convert(path, file, extLen):
	dzi = OUTPUT + file[:extLen] + "dzi"
	im = Vips.Image.new_from_file(path + file)
	# get image header and save to metadata file
	#im.dzsave(dzi, overlap=OVERLAP, tile_size=TILESIZE)
	# create file for header
	headerOutput = OUTPUT + file[:extLen-1] + "_files/metadata.txt"
	bashCommand = "touch " + headerOutput
	call(bashCommand.split())
	# get header information
	bashCommand = "vipsheader -a " + path + file
	p = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	# write header information to file
	text_file = open(headerOutput, "w")
	text_file.write(out)
	text_file.close()
	

# main function
def main():
	path = checkParams()
	files = os.listdir(path)
	for file in files:
		print("-----------------------------------------")
		extLen = getFileExt(file)
		if(extLen != 0):
			print("converting " + file + "...")
			convert(path, file, extLen)
			print("done!")


# start script:
main()
