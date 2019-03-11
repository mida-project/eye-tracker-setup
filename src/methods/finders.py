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
  my_eyetracker = found_eyetrackers[0]
  print("Address: " + my_eyetracker.address)
  print("Model: " + my_eyetracker.model)
  print("Name (It's OK if this is empty): " + my_eyetracker.device_name)
  print("Serial number: " + my_eyetracker.serial_number)
