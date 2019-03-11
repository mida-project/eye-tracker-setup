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

global_gaze_data = None

def gaze_data_callback(gaze_data):
  global global_gaze_data
  global_gaze_data = gaze_data

# def gaze_data_callback(gaze_data):
#   # Print gaze points of left and right eye
#   print("Left eye: ({gaze_left_eye}) \t Right eye: ({gaze_right_eye})".format(
#     gaze_left_eye=gaze_data['left_gaze_point_on_display_area'],
#     gaze_right_eye=gaze_data['right_gaze_point_on_display_area']))

def gaze_data(eyetracker):
  global global_gaze_data

  print("Subscribing to gaze data for eye tracker with serial number {0}.".format(eyetracker.serial_number))
  eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

  # Wait while some gaze data is collected.
  time.sleep(5)

  eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
  print("Unsubscribed from gaze data.")

  print("Last received gaze package:")
  print(global_gaze_data)
