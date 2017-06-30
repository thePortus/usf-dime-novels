# -*- coding: utf-8 -*-
"""common/tests/settings_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The unit test file for the common module's global settings
"""
import unittest

from .. import settings


class TestSettings(unittest.TestCase):

    def test_settings(self):
        if (
            settings.ROOT_PATH and
            settings.PROJECT_PATH and
            settings.PAGE_LOAD_DELAY
        ):
            return True
