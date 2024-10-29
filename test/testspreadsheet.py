from unittest import TestCase

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

    def test_formula_evaluate_with_string(self):
        pspreadsheet = SpreadSheet()
        pspreadsheet.set("A1", "='Apple'")
        self.assertEqual("Apple", pspreadsheet.evaluate("A1"))
    def test_formula_evaluate_with_integer(self):
        pspreadsheet = SpreadSheet()
        pspreadsheet.set("A1", "=1")
        self.assertEqual("1", pspreadsheet.evaluate("A1"))

    def test_formula_evaluate_with_invalid_string(self):
        pspreadsheet = SpreadSheet()
        pspreadsheet.set("A1", "='Apple")
        self.assertEqual("#Error", pspreadsheet.evaluate("A1"))


    def test_formula_with_ref_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B2")
        spreadsheet.set("B2", "=42")
        self.assertEqual("42", spreadsheet.evaluate("A1"))
    def test_formula_with_ref_invalid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B2")
        spreadsheet.set("B2", "=42.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))
    def test_formula_with_ref_invalid_reference(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B2")
        spreadsheet.set("B2", "=A1")
        self.assertEqual("#Circular", spreadsheet.evaluate("A1"))

    def test_formula_evaluate_with_arithmatic_operation_valid_addition(self):
        pspreadsheet = SpreadSheet()
        pspreadsheet.set("A1", "=1+3")
        self.assertEqual("4", pspreadsheet.evaluate("A1"))
    def test_formula_evaluate_with_arithmatic_operation_invalid_addition(self):
        pspreadsheet = SpreadSheet()
        pspreadsheet.set("A1", "=1+3.5")
        self.assertEqual("#Error", pspreadsheet.evaluate("A1"))

    def test_formula_evaluate_with_arithmatic_operation_with_devision_by_zero(self):
        pspreadsheet = SpreadSheet()
        pspreadsheet.set("A1", "=1/0")
        self.assertEqual("#Error", pspreadsheet.evaluate("A1"))

    def test_formula_evaluate_with_arithmatic_operation_add_multiplication(self):
        pspreadsheet = SpreadSheet()
        pspreadsheet.set("A1", "=1+3*2")
        self.assertEqual("9", pspreadsheet.evaluate("A1"))