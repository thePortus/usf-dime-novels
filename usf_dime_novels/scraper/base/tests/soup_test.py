# -*- coding: utf-8 -*-
"""scraper/tests/html_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The unit tests for the soup scrapers, both for web requests and local files."""
import unittest

from bs4 import BeautifulSoup

from .abstract_mixins import AbstractTestMixin
from ..base_scrapers import (
    BaseHTMLWebScraper,
    BaseHTMLFileScraper,
    BaseXMLWebScraper,
    BaseXMLFileScraper,
    BaseKMLWebScraper,
    BaseKMLFileScraper
)
from ....common import settings


class SoupScraperMixin(AbstractTestMixin):
    """Mixin for all non-Selenium soup scrapers"""

    def test_scrape(self):
        return self.assertEqual(
            type(self.scraper.scrape()),
            BeautifulSoup
        )


class TestHTMLWeb(SoupScraperMixin, unittest.TestCase):
    """Unit test for web request of HTML using BeautifulSoup parser"""
    path = settings.TEST_URLS['html']
    scraper_class = BaseHTMLWebScraper


class TestHTMLFile(SoupScraperMixin, unittest.TestCase):
    """Unit test for local HTML file using BeautifulSoup parser"""
    path = settings.TEST_FIXTURES['html']
    scraper_class = BaseHTMLFileScraper


class TestXMLWeb(SoupScraperMixin, unittest.TestCase):
    """Unit test for web request of XML using BeautifulSoup parser"""
    path = settings.TEST_URLS['xml']
    scraper_class = BaseXMLWebScraper


class TestXMLFile(SoupScraperMixin, unittest.TestCase):
    """Unit test for local XML file using BeautifulSoup parser"""
    path = settings.TEST_FIXTURES['xml']
    scraper_class = BaseXMLFileScraper


class TestKMLWeb(SoupScraperMixin, unittest.TestCase):
    """Unit test for web request of KML using BeautifulSoup parser"""
    path = settings.TEST_URLS['kml']
    scraper_class = BaseKMLWebScraper


class TestKMLFile(SoupScraperMixin, unittest.TestCase):
    """Unit test for local KML file using BeautifulSoup parser"""
    path = settings.TEST_FIXTURES['kml']
    scraper_class = BaseKMLFileScraper
