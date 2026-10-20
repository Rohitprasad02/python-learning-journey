# Smart Expense Tracker

A simple, database-backed expense tracking web application built with Python and Flask. Track daily spending, organize expenses by category, and review monthly spending from a clean web interface.

## Features

- **Add Expenses** — Record an amount, category, description, and date.
- **View Expenses** — See saved expenses in one place.
- **Edit Expenses** — Update an expense's amount, category, or description.
- **Delete Expenses** — Remove an expense when it is no longer needed.
- **Spending Summary** — View total spending and transaction count.
- **Category Breakdown** — Calculate spending totals for each category.
- **Monthly Filter** — Filter expenses by month.
- **Persistent Storage** — Store expense records in an SQLite database.
- **Responsive Interface** — Use the application on desktop or mobile screens.

## Tech Stack

- **Language:** Python
- **Backend:** Flask
- **Frontend:** HTML5, CSS3, Jinja2
- **Database:** SQLite
- **Tools:** Visual Studio Code, Git, GitHub

## Project Structure

```text
smart_expense_tracker/
├── main.py
├── expenses.db
├── templates/
│   ├── index.html
│   └── edit.html
├── static/
│   └── style.css
└── README.md
```

`expenses.db` is generated locally when the application initializes its database. It does not need to be committed to GitHub.

## Getting Started

### Prerequisites

- Python 3.13 or a compatible Python 3 version
- pip
- Git (optional, for version control)

### 1. Clone the repository

Replace the placeholder with your GitHub repository URL.

```bash
git clone YOUR_REPOSITORY_URL
cd smart_expense_tracker
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this for the current terminal session and activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### 3. Install Flask

```bash
python -m pip install Flask
```

### 4. Run the application

```bash
python main.py
```

Open this address in your browser:

http://127.0.0.1:5000/

The SQLite database and its table are initialized when the application starts.

## Expense Categories

The application supports these categories:

- Food
- Travel
- Shopping
- Bills
- Other

## Learning Outcomes

This project demonstrates practical use of:

- Python functions and data structures
- Flask routes and HTTP methods
- HTML forms and server-side form handling
- Jinja2 templates
- SQL queries and SQLite database operations
- CRUD operations: Create, Read, Update, and Delete
- Basic input validation
- HTML and CSS integration

## Future Improvements

- Edit the expense date from the edit page
- Add charts and visual spending reports
- Improve validation and error messages
- Add automated tests
- Add CSV export functionality
- Introduce user accounts and authentication

## Author

**Rohit**

Built as a Python learning project to practise web development, database operations, and application design.
