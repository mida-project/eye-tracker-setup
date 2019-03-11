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
from getters import *

def apply_licenses(eyetracker):
  license_file_path = "../licenses/se_internal_license_for_system_tests"
  import tobii_research as tr
  print("Applying license from {0}.".format(license_file_path))
  with open(license_file_path, "rb") as f:
    license = f.read()
  failed_licenses_applied_as_list_of_keys = eyetracker.apply_licenses([tr.LicenseKey(license)])
  failed_licenses_applied_as_list_of_bytes = eyetracker.apply_licenses([license])
  failed_licenses_applied_as_key = eyetracker.apply_licenses(tr.LicenseKey(license))
  failed_licenses_applied_as_bytes = eyetracker.apply_licenses(license)
  if len(failed_licenses_applied_as_list_of_keys) == 0:
    print("Successfully applied license from list of keys.")
  else:
    print("Failed to apply license from list of keys. Validation result: {0}.".
      format(failed_licenses_applied_as_list_of_keys[0].validation_result))
  if len(failed_licenses_applied_as_list_of_bytes) == 0:
    print("Successfully applied license from list of bytes.")
  else:
    print("Failed to apply license from list of bytes. Validation result: {0}.".
      format(failed_licenses_applied_as_list_of_bytes[0].validation_result))
  if len(failed_licenses_applied_as_key) == 0:
    print("Successfully applied license from single key.")
  else:
    print("Failed to apply license from single key. Validation result: {0}.".
      format(failed_licenses_applied_as_key[0].validation_result))
  if len(failed_licenses_applied_as_bytes) == 0:
      print("Successfully applied license from bytes object.")
  else:
    print("Failed to apply license from bytes object. Validation result: {0}.".
      format(failed_licenses_applied_as_bytes[0].validation_result))

def main():
  eyetracker = find_eyetrackers_meta()
  apply_licenses(eyetracker)
  gaze_data(eyetracker)
  # new_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
  # time.sleep(5)
  # new_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
  gaze_output_frequencies(eyetracker)
  get_and_set_display_area(eyetracker)

if __name__ == '__main__':
  main()

# ==================== END File ==================== #
