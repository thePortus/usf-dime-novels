# -*- coding: utf-8 -*-
"""scraper/base_pdf.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The base scraper classes inherited by all scrapers designed to mine data
from specific HTML, XML, or KML pages. At this time, HTML, XML, and KML
scrapers are identical, but specialized functions will be added in the future.
"""
import io

import PyPDF2

from .base_abstract import BaseAbstractScraper


class BasePDFScraper(BaseAbstractScraper):
    """
    Most commonly used parent class to specific page scrapers. See
    base_abstract_scraper.py for documentation about parent class methods
    and properties. The .fetch() method
    """
    mode = 'pdf'

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
        content = self.fetch()
        # If a web request was made, get the .content property
        if self.method == 'request':
            content = content.content
        # Convert binary PDF to readable stream
        content = io.BytesIO(content)
        self.data = PyPDF2.PdfFileReader(content)
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
