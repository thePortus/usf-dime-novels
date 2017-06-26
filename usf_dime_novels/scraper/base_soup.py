# -*- coding: utf-8 -*-
"""scraper/base_soup.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The base scraper classes inherited by all scrapers designed to mine data
from specific HTML, XML, or KML pages. At this time, HTML, XML, and KML
scrapers are identical, but specialized functions will be added in the future.
"""
import requests
from bs4 import BeautifulSoup

from .base_abstract import BaseAbstractScraper


class BaseHTMLScraper(BaseAbstractScraper):
    """
    Most commonly used parent class to specific page scrapers. See
    base_abstract_scraper.py for documentation about parent class methods
    and properties. The .fetch() method
    """
    mode = 'html'
    soup = None

    def fetch(self, delay=True):
        """
        Uses requests module to get data from location specified in .url.
        As with other base scraper classes, it enforces a delay by calling
        self.wait, unless overridden by the delay argument. Returns data
        in plaintext format. If any problem is encountered when requesting the
        data (e.g. a timeout), .fetch() will call itself recursively until a
        successfull request is made.

        arguments
        delay           bool        whether to enforce delay in scraping
        """
        # Enforce scraping delay
        if delay:
            self.wait()
        # Attempt to request data
        try:
            return requests.get(self.url).text
        # If any error encountered, call .fetch() recursively
        except:
            print('Retrying', self.url)
            return self.fetch()

    def scrape(self, silent=False, delay=True):
        """
        Calls .fetch(), converts the plaintext data into a BeautifulSoup object

        arguments
        silent          bool        whether to print the url during scraping
        delay           bool        whether to enforce delay in scraping
        """
        # Calling parent class .scrape() method, which only prints url or not
        super().scrape(silent=silent)
        # Convert result of .fetch() to a BeautifulSoup object and return
        self.soup = BeautifulSoup(self.fetch(delay=delay), 'html.parser')
        return self.soup


class BaseXMLScraper(BaseHTMLScraper):
    """
    Base class for all scrapers of XML pages. See BaseHTMLScraper and
    base_abstract_scraper.py for documentation about parent classes' methods
    and properties.
    """
    mode = 'xml'


class BaseKMLScraper(BaseHTMLScraper):
    """
    Base class for all scrapers of Google Earth's KML pages. See
    BaseHTMLScraper and base_abstract_scraper.py for documentation about parent
    classes' methods and properties.
    """
    mode = 'kml'
