# -*- coding: utf-8 -*-
"""scraper/base_kml.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The base scraper class for all scrapers using BeautifulSoup to scrape KML,
except for those using the Selenium web driver.
"""
from .abstract_base import AbstractBaseSoupScraper


class BaseKMLScraper(AbstractBaseSoupScraper):
    """
    Base class for all scrapers of Google Earth's KML pages. See
    BaseHTMLScraper and base_abstract_scraper.py for documentation about parent
    classes' methods and properties.
    """
    mode = 'kml'
