# -*- coding: utf-8 -*-
"""scraper/base_json.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The parent class inherited by all JSON scraper objects.
"""
import json

import requests

from .base_abstract import BaseAbstractScraper


class BaseJSONScraper(BaseAbstractScraper):
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
        Uses requests module to get data from location specified in .url.
        As with other base scraper classes, it enforces a delay by calling
        self.wait, unless overridden by the delay argument. Returns data
        in plaintext format. If truncate argument is True, it will truncate
        the last comma in the JSON (this is found on some sites, and
        will cause a problem for Python's internal json module unless removed).
        If any problem is encountered when requesting the data
        (e.g. a timeout), .fetch() will call itself recursively until a
        successfull request is made.

        kwargs
        delay           bool        whether to enforce delay in scraping
        truncate        bool        truncate ultimate comma in JSON data
        """
        # Enforce scraping delay
        if delay:
            self.wait()
        # Attempt to request data
        try:
            webdata = requests.get(self.url).text
            # Splice extraneous ending comma and readding bracket
            if truncate:
                return webdata.text[:-3] + ']'
            # Else, return JSON as is
            return webdata
        # If any error encountered, retry request by calling method recursively
        except:
            print('Retrying', self.url)
            return self.fetch()

    def scrape(self, silent=False, delay=True, truncate=True):
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
