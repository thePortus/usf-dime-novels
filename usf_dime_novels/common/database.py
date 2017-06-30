# -*- coding: utf-8 -*-
"""common/database.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Calls the database object (which all other modules will use) into existence.
Database object is either the 'live' database, or 'testing', depending on
an environmental variable.
"""
import os

import peewee as sql

from usf_dime_novels.common import settings, Printer
from usf_dime_novels import definitions


def config_db():
    """
    Returns the sqlite database object depending on live or testing mode.
    Checks for an environment variable named USF_DIME_NOVEL_DB and if it is
    set to 'testing', uses the test database. Builds the filepath to the
    database and returns the peewee object. If testing is active, any previous
    testing dB will be deleted so that testing can have a clean run.
    """
    # Is dB in live or testing mode
    mode = None
    # Path to database file
    db_path = None
    if os.getenv('USF_DIME_NOVEL_DB'):
        Printer('Testing Database in Use')
        mode = 'testing'
    else:
        mode = 'live'
    # Build dB path from module dir, using the subdir specified in settings
    database_dir = os.path.join(
        definitions.MODULE_DIRPATH,
        settings.DB_DIR
    )
    # Check if the database directory exists, if not, create it
    if not os.path.exists(database_dir):
        os.makedirs(database_dir)
    # Build the dB path, either with live or testing database
    if mode == 'testing':
        db_path = os.path.join(database_dir, settings.TESTING_DB)
        # If a previous test database exists, delete it
        if os.path.exists(db_path):
            os.remove(db_path)
    else:
        db_path = os.path.join(database_dir, settings.LIVE_DB)
    return sql.SqliteDatabase(db_path)


# Loads the database, all other modules should call this to interact with dB
database = config_db()
