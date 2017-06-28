# -*- coding: utf-8 -*-
"""db/__init__.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

=================================== DB Module =================================

The DB module houses the schema models and other functions to interact with
the sqlite database. These models will be called from elsewhere (mostly from
the scraper and exporter modules), in order to store and retreive data. If
doing your own project by customizing the scraper module, you should change
these models to reflect the tables you wish to store.
"""
from .collection import (
    Collection,
    Publisher,
    PublisherInCollection,
    Subject,
    SubjectInCollection
)

# List containing all schema tables, for handy reference by other modules
tables = [
    Collection,
    Publisher,
    PublisherInCollection,
    Subject,
    SubjectInCollection
]
