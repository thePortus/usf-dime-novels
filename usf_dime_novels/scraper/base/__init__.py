# -*- coding: utf-8 -*-
"""scraper/base/__init__.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

============================= Base Scraper Module =============================

Base scrapers contain the parent classes for any custom scrapers you want to
create for HTML, XML, KML, JSON, or PDF solutions. See scraper/__init__.py
for documentation"""
from .base_scrapers import (
    BaseHTMLWebScraper,
    BaseHTMLFileScraper,
    BaseXMLWebScraper,
    BaseXMLFileScraper,
    BaseKMLWebScraper,
    BaseKMLFileScraper,
    BaseJSONWebScraper,
    BaseJSONFileScraper,
    BasePDFWebScraper,
    BasePDFFileScraper,
    BaseSeleniumScraper
)
