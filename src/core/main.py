#!/usr/bin/env python
#coding=utf-8

"""
main.py: When creating a Python module, it is common to make
         the module execute some functionality (usually contained
         in a main function) when run as the entry point of
         the program.
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

# Appending variables path.
varsPath = os.path.join(joinPath, 'variables')
varsAbsPath = os.path.abspath(varsPath)
sys.path.append(varsAbsPath)
sys.path.insert(0, varsAbsPath)

# Appending methods path.
methodsPath = os.path.join(joinPath, 'methods')
methodsAbsPath = os.path.abspath(methodsPath)
sys.path.append(methodsAbsPath)
sys.path.insert(0, methodsAbsPath)

# Importing available methods
from finders import *
from gazers import *

def main():
  eyetracker = find_eyetrackers_meta()
  gaze_data(eyetracker)
  # new_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
  # time.sleep(5)
  # new_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
  gaze_output_frequencies(eyetracker)

if __name__ == '__main__':
  main()

# ==================== END File ==================== #
