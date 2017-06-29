# -*- coding: utf-8 -*-
"""scraper/tests/abstract_tests.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains the parent unit test inherited by all scraper unit tests, abstract
classes meant to be inherited by actual tests come in three main flavors,
'soup', 'pdf', and 'selenium'. With the exception of selenium, each of these
abstract classes comes in two types, those meant for testing from web requests,
and those meant for testing local files.
"""
from bs4 import BeautifulSoup


class AbstractBaseTester:
    """
    Parent object which is to be inherited by all actual scraper test objects.
    Prior to running the unit test, it will use its .path on its .scraper_class
    to instantiate the scraper object to be tested. All child classes must
    specify these properties
    """
    # CHILDREN MUST SPECIFY, path to test the scraper on
    path = None
    # CHILDREN MUST SPECIFY, Specific scraper class to test by sending the URL
    scraper_class = None
    # Scraper object, instantiated by the .ready_scraper() method
    scraper = None


class AbstractWebMixinTester:
    """
    Mix-in class for testing all web request test classes
    """
    method = 'request'

    def setUp(self):
        """
        Unit test setup function, called before any tests are run. Assuming
        that .url and .scraper_class are correctly specified, this function
        ensures that there is a working scraper instance at .scraper before
        any tests are run by child classes.
        """
        self.scraper = self.scraper_class(
            self.path,
            method=self.method
        )


class AbstractFileMixinTester:
    """
    Mix-in class for testing all web request test classes
    """
    method = 'file'
    encoding = 'utf-8'

    def setUp(self):
        """
        Unit test setup function, called before any tests are run. Assuming
        that .url and .scraper_class are correctly specified, this function
        ensures that there is a working scraper instance at .scraper before
        any tests are run by child classes.
        """
        self.scraper = self.scraper_class(
            self.path,
            method=self.method,
            encoding=self.encoding
        )


class AbstractSoupMixinTester:
    """
    Mix-in class for testing all BeautifulSoup test classes
    """

    def test_soup(self):
        """
        Tests scraper .scrape() method and ensures that it returns data of
        in the form of a BeautifulSoup object
        """
        return self.assertEqual(
            type(
                self.scraper.scrape(silent=True, delay=False)
            ),
            BeautifulSoup
        )


class AbstractBaseSeleniumTester(AbstractBaseTester):
    """
    Unit test object for the parent HTML scraper object. See
    base_test_scraper.py for setup and inherited functions
    """

    def setUp(self):
        """
        Unit test setup function, will be overridden by child classes which
        specify browser to test
        """
        self.scraper = self.scraper_class(self.path, browser='Firefox')
        return True

    def tearDown(self):
        """
        Closes the browser window to free memory and reduce clutter.
        """
        self.scraper.close()
