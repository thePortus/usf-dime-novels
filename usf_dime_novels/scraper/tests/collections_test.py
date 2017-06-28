# -*- coding: utf-8 -*-
"""scraper/tests/collections_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains unit tests for the parent HTML, XML, and KML scraper objects
"""
import os
import unittest

from bs4 import BeautifulSoup

from ..collections import Collections
from .abstract_tests import AbstractSeleniumTester
from ...common import settings


class TestCollections(AbstractSeleniumTester, unittest.TestCase):
    """
    Unit test object for the parent HTML scraper object. See
    base_test_scraper.py for setup and inherited functions
    """
    scraper_class = Collections
    url = os.path.join(settings.ROOT_PATH, settings.PROJECT_PATH)

    def test_scrape(self):
        """
        Tests scraper .scrape() method and ensures that it returns data of
        in the form of a BeautifulSoup object
        """
        scrape_data = self.scraper.scrape(silent=True, delay=False)
        return self.assertEqual(type(scrape_data), BeautifulSoup)
