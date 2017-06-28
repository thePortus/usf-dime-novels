# -*- coding: utf-8 -*-
"""common/settings.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The global settings file
"""
# The URL of the hosting domain
ROOT_PATH = 'http://digital.lib.usf.edu/'

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

# Fixture directory filepath for running automated tests on local file scrapers
TEST_FIXTURES_DIR = 'tests/fixtures'

# Build the absolute path to the database directory
DB_DIR = 'db/files'
# Set the live and testing database names
LIVE_DB = 'dimenovels.db'
TESTING_DB = 'testing.db'
