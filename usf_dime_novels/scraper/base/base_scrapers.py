# -*- coding: utf-8 -*-
"""scraper/base_scrapers.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains all the base scrapers to be inherited by custom scraper classes.
HTML, XML, KML, JSON, and PDF scrapers all come in two flavors, a 'web' base,
for making remote requests to obtain data, and a 'file' base, for scraping
files on the local system. The Selenium scraper does not have a 'file' base,
as it is used solely for controlling a web browser. Base scrapers are created
by comining abstract base scrapers and a variety of mixin classes."""
from .abstract_mixins import (
    AbstractBaseScraper,
    TextWebMixin,
    TextFileMixin,
    BinaryWebMixin,
    BinaryFileMixin,
    SoupMixin,
    JSONMixin,
    PDFMixin,
    SeleniumMixin
)


class BaseHTMLWebScraper(
    AbstractBaseScraper,
    TextWebMixin,
    SoupMixin
):
    """Base class for any custom HTML scrapers making web requests."""
    pass


class BaseHTMLFileScraper(
    AbstractBaseScraper,
    TextFileMixin,
    SoupMixin
):
    """Base class for any custom HTML scrapers for local files."""
    pass


class BaseXMLWebScraper(
    AbstractBaseScraper,
    TextWebMixin,
    SoupMixin
):
    """Base class for any custom XML scrapers making web requests."""
    pass


class BaseXMLFileScraper(
    AbstractBaseScraper,
    TextFileMixin,
    SoupMixin
):
    """Base class for any custom XML scrapers for local files."""
    pass


class BaseKMLWebScraper(
    AbstractBaseScraper,
    TextWebMixin,
    SoupMixin
):
    """Base class for any custom KML scrapers making web requests."""
    pass


class BaseKMLFileScraper(
    AbstractBaseScraper,
    TextFileMixin,
    SoupMixin
):
    """Base class for any custom KML scrapers for local files."""
    pass


class BaseJSONWebScraper(
    AbstractBaseScraper,
    TextWebMixin,
    JSONMixin
):
    """Base class for any custom JSON scrapers making web requests."""
    pass


class BaseJSONFileScraper(
    AbstractBaseScraper,
    TextFileMixin,
    JSONMixin
):
    """Base class for any custom JSON scrapers for local files."""
    pass


class BasePDFWebScraper(
    AbstractBaseScraper,
    BinaryWebMixin,
    PDFMixin
):
    """Base class for any custom PDF scrapers making web requests."""
    pass


class BasePDFFileScraper(
    AbstractBaseScraper,
    BinaryFileMixin,
    PDFMixin
):
    """Base class for any custom PDF scrapers for local files."""
    pass


class BaseSeleniumScraper(
    AbstractBaseScraper,
    SoupMixin,
    SeleniumMixin
):
    """Base class for any scrapers using Selenium"""
    pass
