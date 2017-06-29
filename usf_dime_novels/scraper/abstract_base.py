# -*- coding: utf-8 -*-
"""scraper/base_abstract.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The abstract base classes inherited by all scraper objects in the module.
Ensures specification of the .path property and a few other essentials. Mostly
contains placeholder functions overridden by all child classes.
"""
import time

import requests
from bs4 import BeautifulSoup

from ..common import settings, Printer


class AbstractBaseScraper:
    """
    Parent scraper object inherited by all scraper classes. Several methods
    are placeholders, but are used by all child classes and so are listed here
    for ease of reference. The .fetch() method is used to request data located
    at the address specified in self.path.
    """
    # Path of data to be scraped
    path = None
    # Storage for data retrieved (and sometimes converted by child classes)
    data = None
    # Method of data acquisition (request or file)
    method = 'request'
    # Character encoding (only matters for the 'file' method)
    encoding = 'utf-8'
    # Delay enforced during web scraping
    delay = settings.PAGE_LOAD_DELAY
    # The root path of the domain hosting the data (e.g. https://github.com)
    root_path = settings.ROOT_PATH

    def __init__(self, path, method=None, encoding=None):
        """
        Stores the path passed sent during object instantiation at .path
        and establishes whether item will be acquired via web request or local
        file.
        """
        self.path = path
        # Storing request method, if specified
        if method:
            if method == 'request' or method == 'file':
                self.method = method
            else:
                raise Exception(
                    'Unknown acquisition method sent to scraper, must be'
                    'request or file.'
                )
        if encoding:
            self.encoding = encoding

    def wait(self):
        """
        This method is called during child classes' .fetch() method. It forces
        a pause before each page is scraped, to avoid over-taxing the server
        and encourage good ettiquette in web scraping.
        """
        time.sleep(self.delay)

    def fetch(self, delay=True):
        """
        Uses requests module to get data from location specified in .path,
        or if specified in self.method, Python's open() function to read file.
        As with other base scraper classes, it enforces a delay by calling
        self.wait, unless overridden by the delay argument. Returns data
        in plaintext format. If any problem is encountered when requesting the
        data (e.g. a timeout), .fetch() will call itself recursively until a
        successfull request is made. This method may be overridden in some
        child classes (BaseJSONScraper, for instance).

        arguments
        delay           bool        whether to enforce delay in scraping
        """
        # If web request is specified
        if self.method == 'request':
            # Enforce scraping delay
            if delay:
                self.wait()
            # Attempt to request data
            try:
                return requests.get(self.path)
            # If any error encountered, call .fetch() recursively
            except:
                print('Retrying', self.path)
                return self.fetch()
        # Otherwise, assume local file request is specified
        else:
            # If scraper is a PDF, file must be opened in binary
            if self.mode == 'pdf':
                with open(self.path, 'rb') as read_file:
                    content = read_file.read()
                    return content
            # Otherwise return file object as list of text lines
            with open(self.path, 'r+', encoding=self.encoding) as read_file:
                return read_file.readlines()

    def scrape(self, silent=False, delay=True):
        """
        Called by child class .scrape() function, which passes the silent
        option to it. If not silent, it prints the path being scraped. child
        .scape() function will then call .fetch() to grab web data,
        and then parses it with BeautifulSoup if HTML or XML or KML, or,
        returns a JSON object, depending on the child scaper object used.

        kwargs
        silent          bool        specifies if path scraped prints to screen
        """
        if not silent:
            Printer('Scraping', self.path + '...')
        # If silent is specified, print a '.' without newline to show progress
        else:
            Printer('.', newline=False)

    def mine(self):
        """
        This method calls the .scrape() method, and then looks for particular
        information within the returned data. This method is usually specified
        in those classes which are themselves children of classes which
        inherit this abstract base class. That is, those that are designed
        to scrape specific kinds of pages (e.g. a scraper which inherits
        the BaseHTMLScraper to gather all the links in a table)
        """
        pass


class AbstractBaseSoupScraper(AbstractBaseScraper):
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
            for line in html_data:
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
