# -*- coding: utf-8 -*-
"""scraper/controller.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

This file contains the main object for interacting with the various scrapers.

You should rewrite this object according to the particulars of your project.

In some projects, such as the one for which the scraper module was built
(the USF Dime Novel collection), this is simple as only one scraper needs to be
called, which itself calls subsequent scrapers for other pages. In other
projects, however in others a series of calls may need to be made. You may
need to use one scraper to mine a series of URLs that are stored in the
database, and then use another series of scrapers to mine each URL, for
example.
"""
import os

from ..common import settings
from .collections import Collections


class Controller:

    def __init__(self):
        """
        Unless you wish it otherwise, all scraping actions will begin during
        the __init__ function, so that simple instantiating Controller is all
        that is needed to perform the entire scrape. If other methods are
        needed, you may still call them from __init__
        """
        # Build full URL from the settings file
        path = os.path.join(settings.ROOT_PATH, settings.PROJECT_PATH)
        # Create root scraper object
        root_collections = Collections(path=path)
        # Begin scrape
        root_collections.scrape()
