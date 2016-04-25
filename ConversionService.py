#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, getopt
import deepzoom
import os


global OUTPUT
OUTPUT = "dzi/"


# check if input parameters are valid
# return input folder if valid, exit otherwise
def checkParams():
	try:
		opts, argv = getopt.getopt(sys.argv[1:],"hi:",["ifile="])
	except getopt.GetoptError:
		print("Error: parameter not found!")
		print("Try ConversionService.py -i <input folder>")
		sys.exit(2)

	if(len(opts) == 0):
		print("Error: no input folder specified!")
		print("Try ConversionService.py -i <input folder>")
		sys.exit(2)
	for opt, arg in opts:
		if opt == "-h":
			print("ConversionService.py -i <input folder>")
			sys.exit()
		elif opt in ("-i", "--ifile"):
			path = arg
	if(os.path.exists(path)):
		print("Input folder is " + path)
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
	elif file.lower().endswith(".npdi"):
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


# convert image source into .dzi format
# param path: directory of param file
# param file: file to be converted
# param extLen: length of file extension
def convert(path, file, extLen):
	if not(path.endswith("/")):
		path += "/"
	dzi = file[:extLen] + "dzi"
	# Create Deep Zoom Image creator with weird parameters
	creator = deepzoom.ImageCreator(tile_size=256, tile_overlap=0, tile_format="png",
			                        image_quality=1.0, resize_filter="bicubic")
	# Create Deep Zoom image pyramid from source
	creator.create(path + file, OUTPUT + dzi)


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
