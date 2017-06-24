# -*- coding: utf-8 -*-
"""scraper/base_abstract.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The abstract base class inherited by all scraper objects in the module.
Ensures specification of the .url property and a few other essentials. Mostly
contains placeholder functions overridden by all child classes.
"""
import time

from ..common import settings, Printer


class BaseAbstractScraper:
    """
    Parent scraper object inherited by all scraper classes. Several methods
    are placeholders, but are used by all child classes and so are listed here
    for ease of reference. The .fetch() method is used to request data located
    at the address specified in self.url.
    """
    # URL of data to be scraped
    url = None
    # Delay enforced during web scraping
    delay = settings.PAGE_LOAD_DELAY
    # The root url of the domain hosting the data (e.g. https://github.com)
    root_url = settings.ROOT_URL

    def __init__(self, url):
        """
        Stores the url passed sent during object instantiation at .url
        """
        self.url = url

    def wait(self):
        """
        This method is called during child classes' .fetch() method. It forces
        a pause before each page is scraped, to avoid over-taxing the server
        and encourage good ettiquette in web scraping.
        """
        time.sleep(self.delay)

    def fetch(self):
        """
        Placeholder function to be overridden by child classes. Is the function
        that grabs data (usually using the requests module). This method is
        usually called by the .scrape() method of child scraper objects.
        """

    def scrape(self, silent=False):
        """
        Called by child class .scrape() function, which passes the silent
        option to it. If not silent, it prints the URL being scraped. child
        .scape() function will then call .fetch() to grab web data,
        and then parses it with BeautifulSoup if HTML or XML or KML, or,
        returns a JSON object, depending on the child scaper object used.

        kwargs
        silent          bool        specifies if url scraped prints to screen
        """
        if not silent:
            Printer('Scraping', self.url + '...')
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
