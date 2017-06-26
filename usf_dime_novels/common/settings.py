# -*- coding: utf-8 -*-
"""common/settings.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The global settings file
"""
# import os

# The URL of the hosting domain
ROOT_URL = 'http://digital.lib.usf.edu/'

# The subpath to the project home
PROJECT_PATH = 'dimenovels/all'

# The automatic delay imposed on scraper objects
PAGE_LOAD_DELAY = 0.5

# URLs for running automated tests on the scrapers
TEST_URLS = {
    'html': 'http://digital.lib.usf.edu/dimenovels/all',
    'xml': 'https://www.w3schools.com/xml/note.xml',
    'kml': 'https://developers.google.com/kml/documentation/KML_Samples.kml',
    'json': 'http://ip.jsontest.com/'
}

# Build the absolute path to the database directory
# DB_DIR = os.path.join(
# Get path of current file
# os.path.abspath(os.path.dirname(__file__)),
# Move up one directory
# '..',
# Move into the db and then files subdirectories
# 'db',
# 'files'
# )
# Set the live and testing database names
LIVE_DB = 'dimenovels.db'
TESTING_DB = 'dimenovels.db'
