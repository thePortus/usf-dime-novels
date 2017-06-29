# -*- coding: utf-8 -*-
"""scraper/base_json.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The parent class inherited by all JSON scraper objects.
"""
import json

from .abstract_base import AbstractBaseScraper


class BaseJSONScraper(AbstractBaseScraper):
    """
    The base class for all JSON scrapers. See base_abstract_scraper.py for
    further information about this object's parent class. The .fetch() method
    returns the json output at the URL as plain text. The .scrape method calls
    .fetch() and then converts it output to a Python-native JSON object. Child
    classes will call .scrape() in their .mine() methods, which will make
    various uses of the data
    """
    mode = 'json'

    def fetch(self, delay=True, truncate=False):
        """
        Uses parent class .fetch() to get data either from the web via the
        requests module, or from a local file. If web request is made, makes
        sure to grab the .text property of the response object. If truncate
        argument is True, it will truncate the last comma in the JSON
        (this is found on some sites, and will cause a problem for Python's
        internal json module unless removed). If any problem is encountered
        when requesting the data (e.g. a timeout), .fetch() will call itself'
        recursively until a successfull request is made.

        kwargs
        delay           bool        whether to enforce delay in scraping
        truncate        bool        truncate ultimate comma in JSON data
        """
        # Get data (web request or file) from parent method
        jsondata = super().fetch(delay=delay)
        # If web request specified, get .text of response object
        if self.method == 'request':
            jsondata = jsondata.text
        # If option to truncate ultimate comma is specified, do so
        if truncate:
            jsondata = jsondata[:-3] + ']'
        return jsondata

    def scrape(self, silent=False, delay=True, truncate=False):
        """
        Calls .fetch(), converts the plaintext data into a native Python JSON
        object, and returns the result

        kwargs
        silent          bool        whether to print the url during scraping
        delay           bool        whether to enforce delay in scraping
        truncate        bool        truncate ultimate comma in JSON data
        """
        # Calling parent class .scrape() method, which only prints url or not
        super().scrape(silent=silent)
        # Convert result of .fetch() to a JSON object and return
        return json.loads(self.fetch(delay=delay, truncate=truncate))
