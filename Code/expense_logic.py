from datetime import datetime


def validate_expense(amount, category, date_string, note):
    if not isinstance(amount, int):
        raise ValueError("Amount must be an integer")

    if amount <= 0:
        raise ValueError("Amount must be positive")

    if category == "select an option" or not category:
        raise ValueError("Please select a category")

    try:
        datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

    if any(char.isdigit() for char in note):
        raise ValueError("Note must not contain numbers")

    return True
