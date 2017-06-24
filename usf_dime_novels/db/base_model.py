# -*- coding: utf-8 -*-
"""db/base_model.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains the base class for all database models. Specifies the database
for all child classes.
"""
import peewee as sql

from . import database


class BaseModel(sql.Model):
    name = None

    class Meta:
        database = database
