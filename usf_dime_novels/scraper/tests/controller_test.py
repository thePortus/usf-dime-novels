# -*- coding: utf-8 -*-
"""scraper/tests/controller_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The unit test for the scraper controller
"""
import unittest

from ..controller import Controller


class ControllerTest(unittest.TestCase):
    """
    Tests the controller which enacts the individual scrapes, in order
    """

    def test_initialize(self):
        """
        Ensures the init function runs correctly
        """
        Controller()
        return True
