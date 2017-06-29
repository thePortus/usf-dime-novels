# -*- coding: utf-8 -*-
"""scraper/base_selenium.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains the base class inherited by all selenium scraper objects.
"""
from selenium import webdriver
from bs4 import BeautifulSoup

from .abstract_base import AbstractBaseScraper
from ..common import Printer


class BaseSeleniumScraper(AbstractBaseScraper):
    """
    The base class for all Selenium scrapers. See base_abstract_scraper.py for
    further information about this object's parent class. The .fetch() method
    opens a window of the web browser specified by .driver
    """
    # Webdriver specified during __init__()
    driver = None

    def __init__(self, path, browser='firefox'):
        """
        Calls parent .__init__() method and passes it the url specified. Then
        uses the browser argument to instantiate and store the selenium
        webdriver object at .driver. The browser must be either Firefox,
        Chrome, Safari, or Edge, otherwise an exception is raised. Unlike some
        other scrapers, this only opens via web requests, and cannot load
        local files.

        arguments
        url             str             address of page to load with webdriver
        browser         store           which browser to use with selenium
        """
        # Calling BaseAbstractScraper's .__init__() method and passing url
        super().__init__(path=path)
        if browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'safari':
            self.driver = webdriver.Safari()
        elif browser.lower() == 'edge':
            self.driver = webdriver.Edge()
        else:
            raise Exception(
                'Unknown browser specified for selenium scraper (url:' +
                self.url + '). Options are firefox, chrome, safari, or edge.' +
                ' Make sure you have installed the necessary webdriver first.'
            )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Upon destruction, close browser window and free memory
        self.close
        super().__exit__(
            exc_type=exc_type,
            exc_value=exc_value,
            traceback=traceback
        )

    def fetch(self, delay=True):
        """
        Overrides parent .fetch(). Uses selenium module to open window of
        location specified in .url. As with other base scraper classes, it
        enforces a delay by calling self.wait, unless overruled by the delay
        argument. Returns data in plaintext format. If any problem is
        encountered when requesting the data (e.g. a timeout), .fetch() will
        call itself recursively until a successfull request is made.

        kwargs
        delay           bool        whether to enforce delay in scraping
        """
        # Enforcing scraping delay
        if delay:
            self.wait()
        # Attempt to load the page in selenium
        try:
            self.driver.get(self.path)
        # If any error encountered, call .fetch() recursively
        except:
            Printer('Error occured in selenium fetch for', self.path)
            return self.fetch()
        # Return initial HTML of page
        return self.driver.page_source

    def close(self):
        """
        Closes, if already open, the Browser window controlled by .driver
        """
        self.driver.quit()

    def refresh_soup(self):
        """
        Soups the data located at .driver.page_source. Called during initial
        scrape, but can also be called again in .mine() or other custom methods
        to get a BeautifulSoup object loaded with the updated HTML
        """
        # Use current driver page soup to re-soup, then return value
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        return self.soup

    def scrape(self, silent=False, delay=True):
        """
        Calls .fetch(), converts the plaintext data into a BeautifulSoup object

        arguments
        silent          bool        whether to print the url during scraping
        delay           bool        whether to enforce delay in scraping
        """
        # Calling parent class .scrape() method, which only prints url or not
        super().scrape(silent=silent)
        # Store result of .fetch() as a BeautifulSoup object
        self.soup = BeautifulSoup(self.fetch(), 'html.parser')
        # Return soup
        return self.soup
