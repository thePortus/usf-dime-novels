# -*- coding: utf-8 -*-
"""scraper/tests/base_selenium_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains the unit tests for selenium using Firefox
"""
import unittest

from .abstract_tests import AbstractBaseSeleniumTester
from ..base_selenium import BaseSeleniumScraper
from ...common import settings


class TestBaseSeleniumScraper(AbstractBaseSeleniumTester, unittest.TestCase):
    """
    Unit test for the selenium scraper using Firefox
    """
    scraper_class = BaseSeleniumScraper
    path = settings.TEST_URLS['html']
