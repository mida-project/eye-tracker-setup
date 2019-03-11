#!/usr/bin/env python
#coding=utf-8

"""
.py:
"""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "1.0.1"
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

import tobii_research as tr
import time

# The current folder path.
basePath = os.path.dirname(__file__)

# The path to the repository "src" folder.
joinPath = os.path.join(basePath, '..')
pathAbsPath = os.path.abspath(joinPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(pathAbsPath)

def find_eyetrackers_meta():
  found_eyetrackers = tr.find_all_eyetrackers()
  # available_eyetracker = found_eyetrackers[0]

  for available_eyetracker in found_eyetrackers:
    print("Address: " + available_eyetracker.address)
    print("Model: " + available_eyetracker.model)
    print("Name (It's OK if this is empty): " + available_eyetracker.device_name)
    print("Serial number: " + available_eyetracker.serial_number)

    if tr.CAPABILITY_CAN_SET_DISPLAY_AREA in available_eyetracker.device_capabilities:
      print("The display area can be set on the eye tracker.")
    else:
      print("The display area can not be set on the eye tracker.")
    if tr.CAPABILITY_HAS_EXTERNAL_SIGNAL in available_eyetracker.device_capabilities:
      print("The eye tracker can deliver an external signal stream.")
    else:
      print("The eye tracker can not deliver an external signal stream.")
    if tr.CAPABILITY_HAS_EYE_IMAGES in available_eyetracker.device_capabilities:
      print("The eye tracker can deliver an eye image stream.")
    else:
      print("The eye tracker can not deliver an eye image stream.")
    if tr.CAPABILITY_HAS_GAZE_DATA in available_eyetracker.device_capabilities:
      print("The eye tracker can deliver a gaze data stream.")
    else:
      print("The eye tracker can not deliver a gaze data stream.")
    if tr.CAPABILITY_HAS_HMD_GAZE_DATA in available_eyetracker.device_capabilities:
      print("The eye tracker can deliver a HMD gaze data stream.")
    else:
      print("The eye tracker can not deliver a HMD gaze data stream.")
    if tr.CAPABILITY_CAN_DO_SCREEN_BASED_CALIBRATION in available_eyetracker.device_capabilities:
      print("The eye tracker can do a screen based calibration.")
    else:
      print("The eye tracker can not do a screen based calibration.")
    if tr.CAPABILITY_CAN_DO_MONOCULAR_CALIBRATION in available_eyetracker.device_capabilities:
      print("The eye tracker can do a monocular calibration.")
    else:
      print("The eye tracker can not do a monocular calibration.")
    if tr.CAPABILITY_CAN_DO_HMD_BASED_CALIBRATION in available_eyetracker.device_capabilities:
      print("The eye tracker can do a HMD screen based calibration.")
    else:
      print("The eye tracker can not do a HMD screen based calibration.")
    if tr.CAPABILITY_HAS_HMD_LENS_CONFIG in available_eyetracker.device_capabilities:
      print("The eye tracker can get/set the HMD lens configuration.")
    else:
      print("The eye tracker can not get/set the HMD lens configuration.")

    return available_eyetracker

# ==================== END File ==================== #
