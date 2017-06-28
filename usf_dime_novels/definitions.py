# -*- coding: utf-8 -*-
"""db/definitions.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains the most essential constants. Unlike settings, these are generated
during start up, rather than pre-configured.
"""
import os


# The absolute filepath to the project directory, to be called by child modules
MODULE_DIRPATH = os.path.dirname(os.path.abspath(__file__))
