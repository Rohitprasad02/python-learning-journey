from abc import ABC, abstractmethod

Expenses = []


class Input(ABC):
    @abstractmethod
    def get_title(self, prompt="Enter Title: "):
        """Return a valid non-empty title."""

    @abstractmethod
    def get_amount(self, prompt="Enter Amount: "):
        """Return a valid positive numeric amount."""

    @abstractmethod
    def get_category(self, prompt="Enter category: "):
        """Return a valid non-empty category."""

    @abstractmethod
    def get_date(self, prompt="Enter date: "):
        """Return a valid non-empty date."""

    @abstractmethod
    def get_choice(self, prompt="Enter your choice: "):
        """Return a valid choice number."""


class ConsoleInput(Input):
    def get_title(self, prompt="Enter Title: "):
        while True:
            title = input(prompt).strip()
            if title:
                return title
            print("Title cannot be empty.")

    def get_amount(self, prompt="Enter Amount: "):
        while True:
            try:
                amount = int(input(prompt))
            except ValueError:
                print("Enter a valid amount.")
                continue
            if amount <= 0:
                print("Enter a valid amount.")
                continue
            return amount

    def get_category(self, prompt="Enter category: "):
        while True:
            category = input(prompt).strip()
            if category:
                return category
            print("Category cannot be empty.")

    def get_date(self, prompt="Enter date: "):
        while True:
            date = input(prompt).strip()
            if date:
                return date
            print("Date cannot be empty.")

    def get_choice(self, prompt="Enter your choice: "):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Enter a valid input.")


console_input = ConsoleInput()


def Add_expense():
    title = console_input.get_title()
    amount = console_input.get_amount()
    category = console_input.get_category()
    date = console_input.get_date()
    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": date,
    }
    Expenses.append(expense)
    print("Added successfully.")


def View_expenses():
    if not Expenses:
        print("Expenses not available.")
        return
    for number, expense in enumerate(Expenses, start=1):
        print(number, expense["title"], expense["amount"], expense["category"], expense["date"])


def search_expenses():
    if not Expenses:
        print("Expenses not available")
        return
    title = console_input.get_title()
    for expense in Expenses:
        if expense["title"] == title:
            print(expense)
            return
    print("Expense not found.")


def delete_expenses():
    if not Expenses:
        print("Expenses not available.")
        return
    title = console_input.get_title()
    for expense in Expenses:
        if expense["title"] == title:
            confirmation = input("Are you sure? y/n: ").lower()

            if confirmation == "y":
                Expenses.remove(expense)
                print("Expense deleted successfully.")
                return
            elif confirmation == "n":
                return
            else:
                print("Enter a valid input.")
                return

    print("Expense not found.")


def Total_expense():
    total = 0

    for expense in Expenses:
        total += expense["amount"]

    print("Total expense:", total)


def menu():
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Total Expense")
    print("6. Exit")
    return console_input.get_choice()


while True:
    choice = menu()

    if choice == 1:
        Add_expense()
    elif choice == 2:
        View_expenses()
    elif choice == 3:
        search_expenses()
    elif choice == 4:
        delete_expenses()
    elif choice == 5:
        Total_expense()
    elif choice == 6:
        print("Exiting the program...")
        break
    else:
        print("Enter a valid input")