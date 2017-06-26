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
import peewee as sql

from usf_dime_novels.common import settings, Printer


def database(mode='live'):
    """
    Returns the sqlite database object depending on live or testing mode.
    Currently redundant, since live & testing databases are the same.
    """
    # Return testing dB is specified, otherwise, live dB
    if mode == 'testing':
        return sql.SqliteDatabase(settings.TESTING_DB)
    return sql.SqliteDatabase(settings.LIVE_DB)


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
