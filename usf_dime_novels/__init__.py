# -*- coding: utf-8 -*-
"""__init__.py

===============================================================================
================================ Dime Novels ==================================
===============================================================================

For scraping and saving data from the University of South Florida's Dime
Novel Digital Collection

By David Jason Thomas (thePortus.com, dave.a.base@gmail.com)

For more information, see
https://github.com/thePortus/dimenovels
"""

import sys
import os
# For use with Travis CI and Coveralls testing suites
# from pkg_resources import get_distribution
from .db import init_db
from .common import Printer


def get_db():
    """
    Checks for an environment variable. If TESTING_DB=true has been set, loads
    returns the testing database, otherwise the live database.
    """
    if os.getenv('USF_DIME_NOVEL_DB'):
        Printer('Testing Database in Use')
        return init_db(mode='testing')
    return init_db(mode='live')


# Loads the database, all other modules should call this to interact with dB
database = get_db()

if sys.version_info[0] != 3:
    raise ImportError('Python Version 3 or above is required for this module.')

__author__ = 'David J. Thomas'

__copyright__ = 'Copyright (c) 2017 David J. Thomas. Distributed and Licensed under the MIT License.'

__description__ = __doc__

__license__ = 'MIT'

__url__ = 'http://github.com/thePortus/dimenovels'

# For use with Travis CI and Coveralls testing suites
# __version__ = get_distribution('dimenovels').version

# For use with manual testing
__version__ = '0.0.1'


# Cleaning up namespaces
# del get_distribution
del sys
