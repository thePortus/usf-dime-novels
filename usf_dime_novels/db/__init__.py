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
    if mode == 'testing':
        return sql.SqliteDatabase(settings.TESTING_DB)
    else:
        return sql.SqliteDatabase(settings.LIVE_DB)


def init_db(mode='live'):
    table_list = [
        # List each table model here
    ]
    db = database(mode=mode)
    db.connect()
    missing_tables = []
    for table in table_list:
        if not table.table_exists():
            missing_tables.append(table)
    if len(missing_tables):
        Printer('Building database...')
        for table in missing_tables:
            table.create_table()
        Printer('Database built')
    db.close()
    return True
