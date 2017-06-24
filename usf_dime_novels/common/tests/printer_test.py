# -*- coding: utf-8 -*-
"""common/tests/printer_test.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The unit test file for the common module's Printer object
"""
import unittest

from .. import Printer


class TestPrinter(unittest.TestCase):

    def test_print(self):
        first_part = 'This is a test of the'
        second_part = 'Printer() object'
        Printer(first_part, second_part)
        return True

    def test_mixed_args(self):
        first_part = 'Testing Printer mixed with integers like'
        second_part = 123
        Printer(first_part, second_part)
        return True
