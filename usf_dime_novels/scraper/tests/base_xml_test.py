# -*- coding: utf-8 -*-
"""scraper/tests/base_xml_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains unit tests for the parent XML scrapers, for web and local files
"""
import unittest

from ..base_xml import BaseXMLScraper
from .abstract_tests import (
    AbstractBaseTester,
    AbstractWebMixinTester,
    AbstractFileMixinTester,
    AbstractSoupMixinTester
)
from ...common import settings


class TestXMLScraper(
    AbstractBaseTester,
    AbstractWebMixinTester,
    AbstractSoupMixinTester,
    unittest.TestCase
):
    """
    Unit test object for the parent XML scraper object. See
    base_test_scraper.py for setup and inherited functions
    """
    scraper_class = BaseXMLScraper
    path = settings.TEST_URLS['xml']


class TestBaseXMLFileScraper(
    AbstractBaseTester,
    AbstractFileMixinTester,
    AbstractSoupMixinTester,
    unittest.TestCase
):
    """
    Unit test object for the parent HTML scraper object via file method. See
    base_test_scraper.py for setup and inherited functions
    """
    scraper_class = BaseXMLScraper
    path = settings.TEST_FIXTURES['xml']
    method = 'file'
    encoding = 'utf-8'
