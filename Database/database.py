import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "expenses.db")


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount INTEGER NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            note TEXT
        )
    """)

    conn.commit()
    conn.close()

def get_expenses_by_date(date):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, amount, category, date, note
        FROM expenses
        WHERE date = ?
        ORDER BY id DESC
    """, (date,))

    rows = cursor.fetchall()
    conn.close()
    return rows

def add_expense(amount, category, date, note):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses (amount, category, date, note)
        VALUES (?, ?, ?, ?)
    """, (amount, category, date, note))

    conn.commit()
    conn.close()


def get_all_expenses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, amount, category, date, note
        FROM expenses
        ORDER BY date DESC, id DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows