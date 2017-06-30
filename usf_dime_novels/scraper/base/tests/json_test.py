# -*- coding: utf-8 -*-
"""scraper/tests/json_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The unit tests for the JSON scrapers, both for web requests and local files."""
import unittest

from .abstract_mixins import AbstractTestMixin
from ..base_scrapers import (
    BaseJSONWebScraper,
    BaseJSONFileScraper
)
from ....common import settings


class JSONTestMixin(AbstractTestMixin):
    """Mixin for all non-Selenium soup scrapers"""

    def test_scrape(self):
        return self.assertEqual(
            type(self.scraper.scrape()),
            dict
        )


class TestJSONWeb(JSONTestMixin, unittest.TestCase):
    """Unit test for web request of HTML using BeautifulSoup parser"""
    path = settings.TEST_URLS['json']
    scraper_class = BaseJSONWebScraper


class TestJSONFile(JSONTestMixin, unittest.TestCase):
    """Unit test for local HTML file using BeautifulSoup parser"""
    path = settings.TEST_FIXTURES['json']
    scraper_class = BaseJSONFileScraper
