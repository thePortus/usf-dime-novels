# -*- coding: utf-8 -*-
"""scraper/tests/base_html_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains unit tests for the parent HTML scrapers, for web and local files
"""
import unittest

from ..base_html import BaseHTMLScraper
from .abstract_tests import (
    AbstractBaseTester,
    AbstractWebMixinTester,
    AbstractFileMixinTester,
    AbstractSoupMixinTester
)
from ...common import settings


class TestBaseHTMLWebScraper(
    AbstractBaseTester,
    AbstractWebMixinTester,
    AbstractSoupMixinTester,
    unittest.TestCase
):
    """
    Unit test object for the parent HTML scraper object via request method. See
    base_test_scraper.py for setup and inherited functions
    """
    scraper_class = BaseHTMLScraper
    path = settings.TEST_URLS['html']
    method = 'request'

    def test_invalid_method(self):
        """
        Ensures that exception raised when method sent to init function isn't
        'request' or 'file'
        """
        return self.assertRaises(
            Exception,
            BaseHTMLScraper,
            path="test_path",
            method='not_a_method'
        )


class TestBaseHTMLFileScraper(
    AbstractBaseTester,
    AbstractFileMixinTester,
    AbstractSoupMixinTester,
    unittest.TestCase
):
    """
    Unit test object for the parent HTML scraper object via file method. See
    base_test_scraper.py for setup and inherited functions
    """
    scraper_class = BaseHTMLScraper
    path = settings.TEST_FIXTURES['html']
    method = 'file'
    encoding = 'utf-8'
