# -*- coding: utf-8 -*-
"""scraper/tests/pdf_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The unit tests for the PDF scrapers, both for web requests and local files."""
import unittest

import PyPDF2

from .abstract_mixins import AbstractTestMixin
from ..base_scrapers import (
    BasePDFWebScraper,
    BasePDFFileScraper
)
from ....common import settings


class PDFTestMixin(AbstractTestMixin):
    """Mixin for all non-Selenium soup scrapers"""

    def test_scrape(self):
        return self.assertEqual(
            type(self.scraper.scrape()),
            PyPDF2.PdfFileReader
        )


class TestPDFWeb(PDFTestMixin, unittest.TestCase):
    """Unit test for web request of HTML using BeautifulSoup parser"""
    path = settings.TEST_URLS['pdf']
    scraper_class = BasePDFWebScraper


class TestPDFFile(PDFTestMixin, unittest.TestCase):
    """Unit test for local HTML file using BeautifulSoup parser"""
    path = settings.TEST_FIXTURES['pdf']
    scraper_class = BasePDFFileScraper
