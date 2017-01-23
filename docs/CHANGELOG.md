#Change Log
All notable changes will be tracked in this file

##[Unreleased]
###Changed
- Restructured all files into docs, src, and build folders

##[0.7] - 2017-01-20
###Added
- MirrorBoxInfo class to generate Mirror boxes of various radii
- MirrorBox item is accessible through Add (INFO_MT_add) menu
- MirrorBox creates Keymap to affect Radius after creation

###Changed
- Return versioning numbers to X.Y[.Z] format

##[0.6] - 2017-01-16
###Added
- build directory
	- contains zip folders of full addons located in repo

###Changed
- Cursor location add to Mirror Box

##[0.5] - 2017-01-15
###Added
- Mirror-Box Add-on
	- Generate a cube shaped mesh with Mirror modifier already active

###Changed
- Bounding Box Script made easier to edit
	- Utilizing lambda function for corner calculation
- Updates to Readme

##[0.4] - 2016-12-27
###Added
- Script that determines the global center of a bounding box
	- Operates on all selected objects in a scene and determines min and max corners and midpoint 

###Changed
- Release numbering shifted to simple increment. 
	- Scripts will not be considered "officially released" at any point.

##[0.3]
###Moved
- Automatic Turntable was requiring a lot of upkeep and will be moved to its own repository

##[0.2]
###Changed
- Automatic Turntable script setup for operator use
- Orbital object generated to contain variables
- Abstracted camera use in functions, can eventually take any bpy.camera object
- Operator can successfully perform front-side-rear rendering of selected object

##[0.1] - 2016-12-07
###Added
- This Changelog
- Script for an Automatic Turntable rendering

###Changed
- Top level folder is now each script individually

###Removed
- Build file folder

##[Prehistoric] - 2016-11-22
###Added
- Leftover script from (defunct) Renderwatch
- Select All Children script
