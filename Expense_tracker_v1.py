Expenses = []

def Add_expense():
    title = input("Enter Title: ")
    if not title:
        print("Title cannot be empty.")
        return
    amount = int(input("Enter Amount: "))
    if amount <= 0:
        print("Enter a valid amount. ")
        return
    category = input("Enter category: ")
    if not category:
        print("Category cannot be empty.")
        return
    date = input("Enter date: ")
    if not date:
        print("Date cannot be empty.")
        return
    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": date
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
    title = input("Enter Title: ")
    for expense in Expenses:
        if expense["title"] == title:
            print(expense)
            return
    print("Expense not found.")

def delete_expenses():
    if not Expenses:
        print("Expenses not available.")
        return
    title = input("Enter Title: ")
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

    print("Total expense:",total)

def menu():
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Total Expense")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    return choice

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