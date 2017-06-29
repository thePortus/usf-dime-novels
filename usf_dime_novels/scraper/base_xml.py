# -*- coding: utf-8 -*-
"""scraper/base_xml.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The base scraper class for all scrapers using BeautifulSoup to scrape XML,
except for those using the Selenium web driver.
"""
from .abstract_base import AbstractBaseSoupScraper


class BaseXMLScraper(AbstractBaseSoupScraper):
    """
    Base class for all scrapers of XML pages. See BaseHTMLScraper and
    base_abstract_scraper.py for documentation about parent classes' methods
    and properties.
    """
    mode = 'xml'
