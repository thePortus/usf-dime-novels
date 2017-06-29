# -*- coding: utf-8 -*-
"""scraper/tests/collections_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains unit tests for the parent HTML, XML, and KML scraper objects
"""
import os
import unittest

from ..collections import Collections
from .abstract_tests import AbstractBaseSeleniumTester
from ...common import settings


class TestCollections(AbstractBaseSeleniumTester, unittest.TestCase):
    """
    Unit test object for the parent HTML scraper object. See
    base_test_scraper.py for setup and inherited functions
    """
    scraper_class = Collections
    path = os.path.join(settings.ROOT_PATH, settings.PROJECT_PATH)
