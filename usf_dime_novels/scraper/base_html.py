# -*- coding: utf-8 -*-
"""scraper/base_html.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The base scraper class for all scrapers using BeautifulSoup to scrape HTML,
except for those using the Selenium web driver.
"""
from .abstract_base import AbstractBaseSoupScraper


class BaseHTMLScraper(AbstractBaseSoupScraper):
    """
    Most commonly used parent class to specific page scrapers. See
    base_abstract_scraper.py for documentation about parent class methods
    and properties. The .fetch() method
    """
    mode = 'html'
