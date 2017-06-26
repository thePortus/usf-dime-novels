# -*- coding: utf-8 -*-
"""scraper/root_collections.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The scraper for the starting page of the University of South Florida Digital
Collection's Dime Novel Archive. The page allows users to browse the different
collections, which dynamically load metadata and item collections. This scraper
Is the only one that needs to be called to initiate a scrape of the entire
site, as it will call subsequent scrapers upon finding links to subcollections.
"""
from .base_selenium import BaseSeleniumScraper


class RootCollections(BaseSeleniumScraper):
    """
    Scrapes the starting page for the USF Digital Collection's 'Dime Novel'
    collection. Gathers any links on the page, then looks for the link to the
    next page. If link to the next page is found, it keeps calling new
    instances of itself recursively for each new page. Once the end of the
    browse menu is reached, all the links are returned back to the original
    RootCollections instance. Then, it calls the scrapers for each collection.
    """

    def get_collection_elements(self):
        """
        Drills into .soup looking for the wrapper containing the list of
        collections. Then finds the <section> tag for each collection in the
        list, returning them as a list of BeautifulSoup objects.
        """
        wrapper = self.soup.find('div', id='main-content')
        return wrapper.find_all('section', class_='sbkBrv_SingleResult')

    def mine(self):
        """
        Calls .scrape(), storing raw HTML in .webdriver.page_source, and a
        parsed BeautifulSoup object in data. Then uses the object to
        locate data on subcollections, both metadata, and links to items in the
        collection by clicking on the object and calling .soup() to get the
        updated results. Stores information in a sqlite dB for later
        exportation using models from the schema module.
        """
        self.scrape()
        collections = self.get_collection_elements()
