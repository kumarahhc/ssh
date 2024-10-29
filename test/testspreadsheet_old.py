from unittest import TestCase

import spreadsheet
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_valid_intiger(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","1")
        self.assertEqual(1,spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","1.5")
        self.assertEqual("#Error",spreadsheet.evaluate("A1"))

    def test_evaluate_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","'Apple'")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))


    def test_formula_evaluate_valid_string_string(self):
        preadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple'")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_formula_evaluate_valid_integer(self):
        preadsheet = SpreadSheet()
        spreadsheet.set("A1", "5")
        self.assertEqual("5", spreadsheet.evaluate("A1"))