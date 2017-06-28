# -*- coding: utf-8 -*-
"""scraper/base_pdf.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The base scraper classes inherited by all scrapers designed to mine data
from specific HTML, XML, or KML pages. At this time, HTML, XML, and KML
scrapers are identical, but specialized functions will be added in the future.
"""
import requests
import PyPDF2

from .base_abstract import BaseAbstractScraper


class BasePDFScraper(BaseAbstractScraper):
    """
    Most commonly used parent class to specific page scrapers. See
    base_abstract_scraper.py for documentation about parent class methods
    and properties. The .fetch() method
    """
    mode = 'html'
    data = None

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
            return requests.get(self.url).content
        # If any error encountered, call .fetch() recursively
        except:
            print('Retrying', self.url)
            return self.fetch()

    def scrape(self, silent=False, delay=True):
        """
        Calls .fetch(), converts the stores the result

        arguments
        silent          bool        whether to print the url during scraping
        delay           bool        whether to enforce delay in scraping
        """
        # Calling parent class .scrape() method, which only prints url or not
        super().scrape(silent=silent)
        # Request PDF, create PyPDF2 reader with it and store in .data
        self.data = PyPDF2.PdfFileReader(self.fetch())
        return self.data

    def mine(self):
        """
        May be overridden by child classes. By default, turns PDF pages into
        a list of strings.
        """
        pdf_texts = []
        # Loop through range of page numbers
        for page_num in range(0, self.data.numPages):
            # Get the individual page
            pdf_page = self.data.getPage(page_num)
            pdf_texts.append(pdf_page.extractText())
        return pdf_texts
