
import unittest
from expense_logic import validate_expense


class TestExpenseValidation(unittest.TestCase):
    def test_valid_expense(self):
        self.assertTrue(
            validate_expense(100, "Food", "2026-02-30", "Lunch")
        )

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            validate_expense(-50, "Food", "2026-02-26", "Lunch")

    def test_non_integer_amount(self):
        with self.assertRaises(ValueError):
            validate_expense("100", "Food", "2026-02-26", "Lunch")

    def test_no_category_selected(self):
        with self.assertRaises(ValueError):
            validate_expense(100, "select an option", "2026-02-26", "Lunch")

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            validate_expense(100, "Food", "26-02-2026", "Lunch")

    def test_note_contains_numbers(self):
        with self.assertRaises(ValueError):
            validate_expense(100, "Food", "2026-02-26", "Lunch123")


if __name__ == "__main__":
    unittest.main()
