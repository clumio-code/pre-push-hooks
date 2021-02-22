#
# Copyright 2021. Clumio, Inc.
#

# SHELL ensures more consistent behavior between macOS and Linux.
SHELL=/bin/bash

PYTHON:=$(shell which python3)

pip3:
	$(PYTHON) -m pip install -r requirements.txt
