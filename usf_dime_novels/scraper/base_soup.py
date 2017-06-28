# -*- coding: utf-8 -*-
"""scraper/base_soup.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The base scraper classes inherited by all scrapers designed to mine data
from specific HTML, XML, or KML pages. At this time, HTML, XML, and KML
scrapers are identical, but specialized functions will be added in the future.
"""
from bs4 import BeautifulSoup

from .base_abstract import BaseAbstractScraper


class BaseSoupScraper(BaseAbstractScraper):
    """
    Most commonly used parent class to specific page scrapers. See
    base_abstract_scraper.py for documentation about parent class methods
    and properties. The .fetch() method
    """
    mode = None

    def fetch(self, delay=True):
        """
        Calls parent class .fetch() and returns result. If .method is 'request'
        then it returns the .text property of the response object.
        """
        html_data = super().fetch(delay=delay)
        if self.method == 'request':
            return html_data.text
        # If .method was a file, convert file to large text string and return
        else:
            html_string = ''
            # Loop through lines in file, add endline char and append
            for line in html_data.readlines():
                html_string += line + '\n'
            return html_string

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
        self.data = BeautifulSoup(self.fetch(delay=delay), 'html.parser')
        return self.data


class BaseHTMLScraper(BaseSoupScraper):
    """
    Most commonly used parent class to specific page scrapers. See
    base_abstract_scraper.py for documentation about parent class methods
    and properties. The .fetch() method
    """
    mode = 'html'


class BaseXMLScraper(BaseSoupScraper):
    """
    Base class for all scrapers of XML pages. See BaseHTMLScraper and
    base_abstract_scraper.py for documentation about parent classes' methods
    and properties.
    """
    mode = 'xml'


class BaseKMLScraper(BaseSoupScraper):
    """
    Base class for all scrapers of Google Earth's KML pages. See
    BaseHTMLScraper and base_abstract_scraper.py for documentation about parent
    classes' methods and properties.
    """
    mode = 'kml'
