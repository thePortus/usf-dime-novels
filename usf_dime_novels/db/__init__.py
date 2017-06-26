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
import os

import peewee as sql

from usf_dime_novels.common import settings, Printer


def database(mode='live'):
    """
    Returns the sqlite database object depending on live or testing mode.
    Currently redundant, since live & testing databases are the same.
    """
    db_path = None
    # Build dB path from current directory, using subdir specified in settings
    database_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        settings.DB_DIR
    )
    # Check if the database directory exists, if not, create it
    if not os.path.exists(database_dir):
        os.makedirs(database_dir)
    # Build the dB path, either with live or testing database
    if mode == 'testing':
        db_path = os.path.join(database_dir, settings.TESTING_DB)
    else:
        db_path = os.path.join(database_dir, settings.LIVE_DB)
    return sql.SqliteDatabase(db_path)


def init_db(mode='live'):
    """
    Performs all the initial operations to check the status of the database.
    If tables do not exist for schema models, tables will be created.
    """
    # List of dB models from the schema
    table_list = [
        # List each table model here
    ]
    db = database(mode=mode)
    db.connect()
    missing_tables = []
    # Check each model for a table, append missing to missing_tables
    for table in table_list:
        if not table.table_exists():
            missing_tables.append(table)
    # If missing tables are found, create them
    if len(missing_tables):
        Printer('Building database...')
        for table in missing_tables:
            table.create_table()
        Printer('Database built')
    # Close tb connection
    db.close()
    return True


# If the designated directory for the sqlite db doesn't exist, make it
if not os.path.exists(settings.DB_DIR):
    os.makedirs(settings.DB_DIR)
