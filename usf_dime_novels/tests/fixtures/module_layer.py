# -*- coding: utf-8 -*-
"""tests/fixtures/module_layer.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains the nose2 module-wide fixture layer
"""
from usf_dime_novels import init_db


class ModuleLayer:

    @classmethod
    def setUp(cls):
        init_db(mode='testing')
