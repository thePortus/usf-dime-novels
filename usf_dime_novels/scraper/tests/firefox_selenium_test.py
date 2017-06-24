# -*- coding: utf-8 -*-
"""scraper/tests/firefox_selenium_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains the unit tests for selenium using Firefox
"""
import unittest

from .abstract_tests import AbstractSeleniumTester


class TestFirefoxScraper(AbstractSeleniumTester, unittest.TestCase):
    """
    Unit test for the selenium scraper using Firefox
    """

    def setUp(self):
        """
        Overrides the parent class setUp function, specifying FireFox
        """
        self.scraper = self.scraper_class(self.url, browser='firefox')
        return True
