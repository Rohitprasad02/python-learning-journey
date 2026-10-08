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
        pass