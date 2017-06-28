# -*- coding: utf-8 -*-
"""scraper/tests/abstract_tests.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains the parent unit test inherited by all scraper unit tests
"""
from bs4 import BeautifulSoup

from ..base_selenium import BaseSeleniumScraper
from ...common import settings


class AbstractBaseTester:
    """
    Parent object which is to be inherited by all actual scraper test objects.
    Prior to running the unit test, it will use its .path on its .scraper_class
    to instantiate the scraper object to be tested. All child classes must
    specify these properties
    """
    # CHILDREN MUST SPECIFY, URL to test the scraper on
    path = None
    # CHILDREN MUST SPECIFY, Specific scraper class to test by sending the URL
    scraper_class = None
    # Scraper object, instantiated by the .ready_scraper() method
    scraper = None
    # Data from success scrape operation
    data = None
    # Whether data come from web or local file
    method = 'request'

    def setUp(self):
        """
        Unit test setup function, called before any tests are run. Assuming
        that .url and .scraper_class are correctly specified, this function
        ensures that there is a working scraper instance at .scraper before
        any tests are run by child classes.
        """
        self.scraper = self.scraper_class(self.path, method=self.method)
        return True


class AbstractSeleniumTester(AbstractBaseTester):
    """
    Unit test object for the parent HTML scraper object. See
    base_test_scraper.py for setup and inherited functions
    """
    scraper_class = BaseSeleniumScraper
    url = settings.TEST_URLS['html']

    def setUp(self):
        """
        Unit test setup function, will be overridden by child classes which
        specify browser to test
        """
        self.scraper = self.scraper_class(self.path)
        return True

    def tearDown(self):
        """
        Closes the browser window to free memory and reduce clutter.
        """
        self.scraper.close()

    def test_scrape(self):
        """
        Tests scraper .scrape() method in Firefox and ensures it returns the
        result as a BeautifulSoup object
        """
        return self.assertEqual(
            type(
                self.scraper.scrape(silent=True, delay=False)
            ),
            BeautifulSoup
        )
