#!/usr/bin/env python
#coding=utf-8

"""
.py: 
"""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "1.0.3"
__status__      = "Development"
__copyright__   = "Copyright 2019, Instituto Superior Técnico (IST)"
__credits__     = [
  "Bruno Oliveira",
  "Carlos Santiago",
  "Jacinto C. Nascimento",
  "Pedro Miraldo",
  "Nuno Nunes"
]

import os
import sys

from os import path

# The current folder path.
basePath = os.path.dirname(__file__)

# The path to the repository "src" folder.
joinPath = os.path.join(basePath, '..')
pathAbsPath = os.path.abspath(joinPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(pathAbsPath)

# Appending libs path.
libsPath = os.path.join(joinPath, 'libs')
libsAbsPath = os.path.abspath(libsPath)
sys.path.append(libsAbsPath)
sys.path.insert(0, libsAbsPath)

# Import available libs
from libs import tobii_pro_wrapper as tpw

# Create a TobiiHelper object
thobj = tpw.TobiiHelper()

# Idenfity and define the experimental monitor
thobj.setMonitor(nameString = None, dimensions = None)

# Find eyetrackers and connect
thobj.findTracker(serialString = None)

# Determine the coordinates for the eyetracker's 
# tracking spaces (trackbox and active display area)
thobj.getTrackerSpace()

# Run a full 5 point calibration routing
# thobj.runFullCalibration(numCalibPoints = 5)

# start the eyetracker
thobj.startGazeData()

# thobj.getAvgGazePos()

# # to get real time gaze data, place this command within a "while" loop 
# # during each trial run
# while True:
# 	toPrint = thobj.getCurrentData()
# 	print(toPrint)

# stop the eyetracker
thobj.stopGazeData()

# ==================== END File ==================== #