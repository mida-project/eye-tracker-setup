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
from tobii_research import DisplayArea
import time

# The current folder path.
basePath = os.path.dirname(__file__)

# The path to the repository "src" folder.
joinPath = os.path.join(basePath, '..')
pathAbsPath = os.path.abspath(joinPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(pathAbsPath)

def get_and_set_display_area(eyetracker):
  display_area = eyetracker.get_display_area()

  print("Got display area from tracker with serial number {0}:".format(eyetracker.serial_number))

  print("Bottom Left: {0}".format(display_area.bottom_left))
  print("Bottom Right: {0}".format(display_area.bottom_right))
  print("Height: {0}".format(display_area.height))
  print("Top Left: {0}".format(display_area.top_left))
  print("Top Right: {0}".format(display_area.top_right))
  print("Width: {0}".format(display_area.width))

  # To set the display area it is possible to either use a previously saved instance of
  # the class Display area, or create a new one as shown bellow.
  new_display_area_dict = dict()
  new_display_area_dict['top_left'] = display_area.top_left
  new_display_area_dict['top_right'] = display_area.top_right
  new_display_area_dict['bottom_left'] = display_area.bottom_left

  new_display_area = DisplayArea(new_display_area_dict)

  eyetracker.set_display_area(new_display_area)

# ==================== END File ==================== #
