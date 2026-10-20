
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from datetime import date

app = Flask(__name__)

DATABASE = "expenses.db"

CATEGORIES = ["Food", "Travel", "Shopping", "Bills", "Other"]


# Database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Create database and update existing table
def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)

    columns = conn.execute(
        "PRAGMA table_info(expenses)"
    ).fetchall()

    column_names = [column["name"] for column in columns]

    if "expense_date" not in column_names:
        conn.execute(
            "ALTER TABLE expenses ADD COLUMN expense_date TEXT"
        )

    conn.commit()
    conn.close()


# Home page and monthly filter
@app.route("/")
def home():
    selected_month = request.args.get("month", "").strip()

    conn = get_db_connection()

    if selected_month:
        try:
            date.fromisoformat(selected_month + "-01")
        except ValueError:
            selected_month = ""

    if selected_month:
        expenses = conn.execute(
            """
            SELECT * FROM expenses
            WHERE expense_date LIKE ?
            ORDER BY expense_date DESC, id DESC
            """,
            (selected_month + "%",)
        ).fetchall()
    else:
        expenses = conn.execute(
            "SELECT * FROM expenses ORDER BY id DESC"
        ).fetchall()

    if selected_month:
        category_totals = conn.execute(
            """
            SELECT category, SUM(amount) AS total
            FROM expenses
            WHERE expense_date LIKE ?
            GROUP BY category
            ORDER BY category
            """,
            (selected_month + "%",)
        ).fetchall()
    else:
        category_totals = conn.execute(
            """
            SELECT category, SUM(amount) AS total
            FROM expenses
            GROUP BY category
            ORDER BY category
            """
        ).fetchall()

    conn.close()

    total = sum(float(expense["amount"]) for expense in expenses)
    count = len(expenses)

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        count=count,
        category_totals=category_totals,
        selected_month=selected_month
    )


# Add a new expense
@app.route("/add", methods=["POST"])
def add_expense():
    amount = request.form.get("amount", type=float)
    category = request.form.get("category", "")
    description = request.form.get("description", "").strip()
    expense_date = request.form.get("expense_date", "")

    if (
        amount is None
        or amount <= 0
        or category not in CATEGORIES
        or not description
        or len(description) > 100
    ):
        return "Invalid expense details", 400

    try:
        date.fromisoformat(expense_date)
    except (ValueError, TypeError):
        return "Please enter a valid expense date", 400

    conn = get_db_connection()

    conn.execute(
        """
        INSERT INTO expenses
        (amount, category, description, expense_date)
        VALUES (?, ?, ?, ?)
        """,
        (amount, category, description, expense_date)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("home"))


# Delete an expense
@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id):
    conn = get_db_connection()

    conn.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("home"))


# Show the edit page
@app.route("/edit/<int:expense_id>")
def edit_expense(expense_id):
    conn = get_db_connection()

    expense = conn.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    ).fetchone()

    conn.close()

    if expense is None:
        return "Expense not found", 404

    return render_template("edit.html", expense=expense)


# Save edited expense details
@app.route("/update/<int:expense_id>", methods=["POST"])
def update_expense(expense_id):
    amount = request.form.get("amount", type=float)
    category = request.form.get("category", "")
    description = request.form.get("description", "").strip()

    if (
        amount is None
        or amount <= 0
        or category not in CATEGORIES
        or not description
        or len(description) > 100
    ):
        return "Invalid expense details", 400

    conn = get_db_connection()

    existing_expense = conn.execute(
        "SELECT id FROM expenses WHERE id = ?",
        (expense_id,)
    ).fetchone()

    if existing_expense is None:
        conn.close()
        return "Expense not found", 404

    conn.execute(
        """
        UPDATE expenses
        SET amount = ?, category = ?, description = ?
        WHERE id = ?
        """,
        (amount, category, description, expense_id)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("home"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)