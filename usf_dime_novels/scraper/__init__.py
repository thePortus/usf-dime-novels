# -*- coding: utf-8 -*-
"""scraper/__init__.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

================================ Scraper Module ===============================

The init file for the scraper module

Designed by and for projects by David J. Thomas, but is available to all to
make complex scraping slightly less complicated for anyone who wants to use it.

The scraper module provides base objects, which can be used in any number of
web-scraping projects. This folder contains both the base scrapers designed
for a range of pages, and the scrapers designed specifically for this project.
Create a .py file inside the scraper directory named after your custom scraper.
Inside the file, declare a class which inherits from the base class of your
choice.

All scrapers have 3 essential methods...
1) .fetch(), which makes a web request and receives data of some form
2) .scrape(), which parses or somehow processes the data received by .fetch()
3) .mine(), a blank function to override, it 'does something' with .scrape()

All scrapers follow a similar sequence...
1) The scraper is instantiated and given a url to scrape, stored in .url
2) You write .mine(), somewhere you will need to call .scrape() to get data
3) .scrape() will need data to parse/process, and automatically calls .fetch()
4) .fetch() makes a web request at .url, and returns it to .scrape()
5) .scrape() then converts the data in some manner, and returns it to .mine()
6) In your .mine() you do whatever you want with it, return data or store it


The range of base scrapers available are as follows...
1) BaseHTMLScraper (base_soup.py) parses HTML as BeautifulSoup object
2) BaseXMLScraper (base_soup.py) parses XML as BeautifulSoup object
3) BaseKMLScraper (base_soup.py) parses KML as BeautifulSoup object
4) BaseJSONScraper (base_json.py) parses JSON as a Python dict
5) BaseSeleniumScraper (base_selenium.py) Selenium into BeautifulSoup

e.g.
from .base_soup_scrapers import BaseHTMLScraper


class GitRepoScraper(BaseHTMLScraper):

    def mine(self):
        # Call scrape function, getting data as a BeautifulSoup object
        repo_html = self.scrape()
        # Look for the span tag with the class of 'author'
        author_of_repo = repo_html.find(
            'span', class_='author'
        # Inside that, look for the (only) 'a' tag
        ).find(
            'a'
        # Get the text inside the 'a' tag
        ).get_text()
        # Return only the data that you want, in this example, the author
        # of the repo.
        return author_of_repo

        #Alternatively, you could return multiple values as a
        # dictionary, a tuple, a list, a list of dictionaries, a list of tuples
        # etc... Finally, you could instead to choose to store some values
        # at any properties you might wish (such as .data), for use in
        # any additional functions you might write, should you wish to.

Finally, you need to edit the controller.py file located in this directory,
which will actually call one or more scrapers in a manner you determine
when writing its functions. Then, all you need to do is call the controller
object and the scraping will begin.
"""
from .controller import Controller
