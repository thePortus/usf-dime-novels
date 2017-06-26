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


class CollectionElement:
    """
    Object to interact with a single collection's summary metadata found on the
    main browse page. Its properties give quick access to collection info and
    it enables creating the collection with the database model object
    """
    soup = None

    def __init__(self, html_soup):
        """
        Init function receives soup of one collection and stores it in .soup

        arguments
        html_soup           BeautifulSoup           soup of a single collection
        """
        # Drilling down to the internal wrapper <div> tag
        self.soup = html_soup.find('div', class_='sbkBrv_SingleResultDesc')

    @property
    def title(self):
        """
        Returns the title of the collection
        """
        return self.soup.find(
            'span', class_='briefResultsTitle'
        ).find(
            'a'
        ).get_text()


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

    def get_info_from_collections(self, element_soups):
        """
        Converts a list of BeautifulSoup objects into a list of
        CollectionElement objects, which are designed to make the mining of
        data and storage in the database easier.
        """
        collections = []
        # Loop through each soup, make CollectionElement, store in collections
        for element_soup in element_soups:
            collections.append(CollectionElement(element_soup))
        # Return list of CollectionElements
        return collections

    def mine(self):
        """
        Calls .scrape(), storing raw HTML in .webdriver.page_source, and a
        parsed BeautifulSoup object in data. Then uses the object to
        locate data on subcollections, both metadata, and links to items in the
        collection by clicking on the object and calling .soup() to get the
        updated results. Stores information in a sqlite dB for later
        exportation using models from the schema module.
        """
        collections = []
        # Getting HTML snapshot with selenium, storing a soup object in .soup
        self.scrape()
        # Returns only the parts of the soup that surround each collection
        collection_elements = self.get_collection_elements()
        # Turns each soup element into a CollectionElement object
        collections = self.get_info_from_collections(collection_elements)
        # NOTE THE RETURN VALUE IS MERELY TO PASS TESTING< MUST BE CHANGED
        return self.soup
