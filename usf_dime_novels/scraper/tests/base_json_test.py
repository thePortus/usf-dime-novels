# -*- coding: utf-8 -*-
"""scraper/tests/base_json_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains the unit tests for the parent JSON scraper object
"""
import unittest

from ..base_json import BaseJSONScraper
from .abstract_tests import AbstractBaseTester, AbstractWebMixinTester
from ...common import settings


class TestBaseJSONScraper(
    AbstractBaseTester,
    AbstractWebMixinTester,
    unittest.TestCase
):
    """
    Unit test object for the parent JSON scraper object. See
    base_test_scraper.py for setup and inherited functions
    """
    scraper_class = BaseJSONScraper
    path = settings.TEST_URLS['json']

    def test_scrape(self):
        """
        Tests scraper .scrape() method and ensures that it returns data in the
        form of a JSON object
        """
        return self.assertEqual(
            type(
                self.scraper.scrape(silent=True, delay=True)
            ),
            dict
        )
