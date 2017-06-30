# -*- coding: utf-8 -*-
"""scraper/tests/selenium_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The unit tests for the Selenium scraper."""
import unittest


from .abstract_mixins import AbstractTestMixin
from .soup_test import SoupScraperMixin
from ..base_scrapers import BaseSeleniumScraper
from ....common import settings


class SeleniumScraperMixin(AbstractTestMixin):
    """Mixin for Selenium web tests. Overrides parent tearDown method in order
    to close the web browser window opened by Selenium"""

    def tearDown(self):
        """Close browser window and call parent tearDown to free scraper memory
        """
        self.scraper.close()
        super().tearDown()


class TestSeleniumScraper(
    SeleniumScraperMixin,
    SoupScraperMixin,
    unittest.TestCase
):
    """Test for the base selenium scraper."""
    path = settings.TEST_URLS['html']
    scraper_class = BaseSeleniumScraper
