import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "expenses.db")


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()

    conn.execute("""
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


def table_monthly_creation():
    conn = get_connection()

    conn.execute('''
            CREATE TABLE IF NOT EXISTS "Monthly Expenses" (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount INTEGER NOT NULL,
                month TEXT NOT NULL
            )
        ''')
    conn.commit()
    conn.close()


    rows = get_all_expenses()
    months = []
    for row in rows:
        if row[3][0:7] not in  months:
            months.append(row[3][0:7])
    monthly_cost = {}
    print(months)
    for month in months:

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute (f"""
                SELECT amount 
                FROM expenses
                WHERE date like '{month}%'
            """)
        monthly_expense  = cursor.fetchall()
        print(monthly_expense)
        monthly_cost[month] = monthly_expense
    return monthly_cost
