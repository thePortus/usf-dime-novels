# -*- coding: utf-8 -*-
"""scraper/tests/base/abstract_mixins.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Contains mixin classes for the scraper unit tests"""


class AbstractTestMixin:
    """Parent Mixin for all scraper unit tests. Expects children to provide
    .scraper_class and .path for the setUp function to instantiate .scraper."""
    path = None
    scraper_class = None
    scraper = None

    def setUp(self):
        """ Creates an instance of scraper_class using path specified by child
        """
        self.scraper = self.scraper_class(self.path)

    def tearDown(self):
        """
        Frees memory by eliminating scraper
        """
        del self.scraper
