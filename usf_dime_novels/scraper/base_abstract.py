# -*- coding: utf-8 -*-
"""scraper/base_abstract.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The abstract base class inherited by all scraper objects in the module.
Ensures specification of the .path property and a few other essentials. Mostly
contains placeholder functions overridden by all child classes.
"""
import time

import requests

from ..common import settings, Printer


class BaseAbstractScraper:
    """
    Parent scraper object inherited by all scraper classes. Several methods
    are placeholders, but are used by all child classes and so are listed here
    for ease of reference. The .fetch() method is used to request data located
    at the address specified in self.path.
    """
    # Path of data to be scraped
    path = None
    # Method of data acquisition (request or file)
    method = 'request'
    # Character encoding (only matters for the 'file' method)
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
            file_data = ''
            # Open file
            with open(self.path, 'r+', encoding=self.encoding) as read_file:
                # Loop through each line and build a large string
                for file_line in read_file.readlines():
                    # Make sure to re-add the endline char
                    file_data += file_line + '\n'
            return file_data

    def scrape(self, silent=False):
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
