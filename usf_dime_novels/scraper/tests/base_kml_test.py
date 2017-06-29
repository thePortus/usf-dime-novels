# -*- coding: utf-8 -*-
"""scraper/tests/base_xml_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains unit tests for the parent XML scrapers, for web and local files
"""
import unittest

from ..base_kml import BaseKMLScraper
from .abstract_tests import (
    AbstractBaseTester,
    AbstractWebMixinTester,
    AbstractFileMixinTester,
    AbstractSoupMixinTester
)
from ...common import settings


class TestBaseKMLWebScraper(
    AbstractBaseTester,
    AbstractWebMixinTester,
    AbstractSoupMixinTester,
    unittest.TestCase
):
    """
    Unit test object for the parent KML scraper object. See
    base_test_scraper.py for setup and inherited functions
    """
    scraper_class = BaseKMLScraper
    path = settings.TEST_URLS['kml']


class TestBaseKMLFileScraper(
    AbstractBaseTester,
    AbstractFileMixinTester,
    AbstractSoupMixinTester,
    unittest.TestCase
):
    """
    Unit test object for the parent HTML scraper object via file method. See
    base_test_scraper.py for setup and inherited functions
    """
    scraper_class = BaseKMLScraper
    path = settings.TEST_FIXTURES['kml']
    method = 'file'
    encoding = 'utf-8'
