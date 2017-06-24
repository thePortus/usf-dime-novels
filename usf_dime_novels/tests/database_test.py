# -*- coding: utf-8 -*-
"""common/__init__.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Module-wide functional test for the testing database
"""
import unittest

from usf_dime_novels import init_db
from .fixtures import ModuleLayer


class TestDataBase(unittest.TestCase):
    layer = ModuleLayer
