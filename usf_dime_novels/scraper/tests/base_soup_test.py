# -*- coding: utf-8 -*-
"""scraper/tests/base_soup_tests.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains unit tests for the parent HTML, XML, and KML scraper objects
"""
import unittest

from bs4 import BeautifulSoup

from ..base_soup import (
    BaseHTMLScraper,
    BaseXMLScraper,
    BaseKMLScraper
)
from .abstract_tests import AbstractBaseTester
from ...common import settings


class TestBaseHTMLScraper(AbstractBaseTester, unittest.TestCase):
    """
    Unit test object for the parent HTML scraper object. See
    base_test_scraper.py for setup and inherited functions
    """
    scraper_class = BaseHTMLScraper
    path = settings.TEST_URLS['html']

    def test_scrape(self):
        """
        Tests scraper .scrape() method and ensures that it returns data of
        in the form of a BeautifulSoup object
        """
        return self.assertEqual(
            type(
                self.scraper.scrape(silent=True, delay=False)
            ),
            BeautifulSoup
        )


class TestXMLScraper(AbstractBaseTester, unittest.TestCase):
    """
    Unit test object for the parent XML scraper object. See
    base_test_scraper.py for setup and inherited functions
    """
    scraper_class = BaseXMLScraper
    path = settings.TEST_URLS['xml']

    def test_scrape(self):
        """
        Tests scraper .scrape() method and ensures that it returns data of
        in the form of a BeautifulSoup object
        """
        return self.assertEqual(
            type(
                self.scraper.scrape(silent=True, delay=False)
            ),
            BeautifulSoup
        )


class TestKMLScraper(AbstractBaseTester, unittest.TestCase):
    """
    Unit test object for the parent KML scraper object. See
    base_test_scraper.py for setup and inherited functions
    """
    scraper_class = BaseKMLScraper
    path = settings.TEST_URLS['kml']

    def test_scrape(self):
        """
        Tests scraper .scrape() method and ensures that it returns data of
        in the form of a BeautifulSoup object
        """
        return self.assertEqual(
            type(
                self.scraper.scrape(silent=True, delay=False)
            ),
            BeautifulSoup
        )
