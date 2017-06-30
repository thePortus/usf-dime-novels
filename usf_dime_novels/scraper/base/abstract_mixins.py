# -*- coding: utf-8 -*-
"""scraper/base_abstract.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The abstract base classes inherited by all scraper objects in the module.
Ensures specification of the .path property and a few other essentials. Mostly
contains placeholder functions overridden by all child classes."""
import time
import io
import json

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import PyPDF2

from ...common import settings, Printer


class AbstractBaseScraper:
    """Parent scraper object inherited by all scraper classes. Several methods
    are placeholders, but are used by all child classes and so are listed here
    for ease of reference. The .fetch() method is used to request data located
    at the address specified in self.path."""
    # Path of data to be scraped
    path = None
    # Storage for data retrieved (and sometimes converted by child classes)
    data = None
    # Delay enforced during web scraping
    delay = settings.PAGE_LOAD_DELAY

    def __init__(self, path):
        """Stores the path passed sent during object instantiation at .path
        and establishes whether item will be acquired via web request or local
        file."""
        self.path = path

    def wait(self):
        """This method is called during child classes' .fetch() method. It
        forces a pause before each page is scraped, to avoid over-taxing the
        server and encourage good ettiquette in web scraping."""
        time.sleep(self.delay)


class BaseWebMixin:
    """Mixin class used for scrapers that need to load web files."""

    def fetch(self):
        """Makes web request to .path, if there is an error, calls itself
        recursively until successfull"""
        try:
            # Enforcing scraping delay
            self.wait()
            return requests.get(self.path)
        except:
            Printer('Error scraping', self.path, 'retrying...')
            return self.fetch()


class TextWebMixin(BaseWebMixin):
    """Mixin class used for scrapers that need to load web files in plaintext
    format."""

    def fetch(self):
        """Returns the .text property of the web request"""
        return super().fetch().text


class BinaryWebMixin(BaseWebMixin):
    """Mixin class used for scrapers that need to load a binary web request
    (like PDFs)"""

    def fetch(self):
        """Returns the .content property of the web request"""
        return super().fetch().content


class BinaryFileMixin:
    """Mixin class used for scrapers that need to load a binary file
    (like PDFs)"""

    def fetch(self):
        """Opens the file and converts to in-memory binary stream"""
        with open(self.path, 'rb') as binary_file:
            return binary_file.read()


class TextFileMixin:
    """Mixin class used for scrapers that need to load local files in plaintext
    format."""

    def fetch(self):
        """Opens filed specified at .path and returns builds a string representing
        the file."""
        file_string = ''
        with open(self.path, 'r+') as text_file:
            for line in text_file.readlines():
                file_string += line + '\n'
        return file_string


class PDFMixin:
    """Parent class for PDF scrapers making web requests. See abstract_mixins.py
    for documentation."""

    def scrape(self):
        """Calls .fetch(), converts and stores the result"""
        # Convert binary PDF to readable stream
        content = io.BytesIO(self.fetch())
        self.data = PyPDF2.PdfFileReader(content)
        return self.data

    def mine(self):
        """May be overridden by child classes. By default, turns PDF pages into
        a list of strings."""
        pdf_texts = []
        # Loop through range of page numbers
        for page_num in range(0, self.data.numPages):
            # Get the individual page
            pdf_page = self.data.getPage(page_num)
            pdf_texts.append(pdf_page.extractText())
        return pdf_texts


class JSONMixin:
    """Mixin class for all JSON scraper."""

    def scrape(self):
        """Calls .fetch(), converts the plaintext data into a native Python JSON
        object, and returns the result"""
        return json.loads(self.fetch())


class SoupMixin:
    """Most commonly used parent class to specific page scrapers. See
    base_abstract_scraper.py for documentation about parent class methods
    and properties."""
    mode = None

    def scrape(self):
        """Calls .fetch(), converts the plaintext data into soup"""
        # Convert result of .fetch() to a BeautifulSoup object and return
        self.data = BeautifulSoup(self.fetch(), 'html.parser')
        return self.data


class SeleniumMixin:
    """Mixin class for all Selenium scrapers. Creates the webdriver object,
    and ensures that when fetch is called, a Selenium request is made,
    rather than using the requests module. This mixin only comes in a
    'web' request flavor. Must be used in combination with the SoupMixin
    class."""
    # Creates the webdriver
    driver = webdriver.Firefox

    def fetch(self):
        """
        Uses selenium module to open window of location specified in .path. As
        with other base scraper classes, it enforces a delay by calling
        self.wait, unless overruled by the delay argument. Returns data in
        plaintext format. If any problem is encountered when requesting the
        data (e.g. a timeout), .fetch() will call itself recursively until a
        successfull request is made."""
        # Enforcing scraping delay
        self.wait()
        # Opens a browser window
        self.driver = self.driver()
        # Attempt to load the page in selenium
        try:
            self.driver.get(self.path)
        # If any error encountered, call .fetch() recursively
        except:
            Printer('Error scraping', self.path, 'retrying...')
            return self.fetch()
        # Return initial HTML of page
        return self.driver.page_source

    def close(self):
        """Closes, if already open, the Browser window controlled by .driver"""
        self.driver.quit()

    def refresh_soup(self):
        """Soups the data located at .driver.page_source. Called during initial
        scrape, but can also be called again in .mine() or other custom methods
        to get a BeautifulSoup object loaded with the updated HTML"""
        # Use current driver page soup to re-soup, then return value
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        return self.soup
