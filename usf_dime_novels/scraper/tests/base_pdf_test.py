# -*- coding: utf-8 -*-
"""scraper/tests/base_pdf_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains the unit tests for the base PDF scraper object
"""
import unittest

import PyPDF2
from ..base_pdf import BasePDFScraper
from .abstract_tests import AbstractBaseTester, AbstractFileMixinTester
from ...common import settings


class TestBasePDFFileScraper(
    AbstractBaseTester,
    AbstractFileMixinTester,
    unittest.TestCase
):
    """
    Unit test object for the parent PDF scraper object. Uses layer fixtures
    for a sample file.
    """
    scraper_class = BasePDFScraper
    path = settings.TEST_FIXTURES['pdf']
    method = 'file'

    def test_scrape(self):
        """
        Tests scraper .scrape() method and ensures that it returns the PDF
        converted into a text string
        """
        return self.assertEqual(
            type(
                self.scraper.scrape(silent=True, delay=False)
            ),
            PyPDF2.PdfFileReader
        )
