class Transaction:
    def __init__(self, type, amount,category):
        self.type = type
        self.amount = amount
        self.category = category

    def display(self):
        print(f"Type: {self.type}")
        print(f"Amount: {self.amount}")
        print(f"Category: {self.category}")

class BudgetManager:
    def __init__(self):
        self.transaction = []

    def Add_transaction(self):
        try:

            type = input("Enter type (income/expense): ").strip().lower()
            if type not in ("income", "expense"):
                print("Enter type in (income/expense): ")
                return
            amount = int(input("Enter Amount: "))
            if amount <= 0:
                print("Enter a valid amount: ")
                return
            category = input("Enter Category: ").strip().lower()
            if not category:
                print("Category cannot be empty.")
                return
            t = Transaction(type,amount,category)
            self.transaction.append(t)
            print("Added Successfully")
        except ValueError:
            print("Enter a valid input.")
            return

    def View_transaction(self):
        if not self.transaction:
            print("Transaction is empty.")
            return
        for transaction in self.transaction:
            transaction.display()

    def Calculate_balance(self):
        balance = 0

        for transaction in self.transaction:
            if transaction.type == "income":
                balance += transaction.amount
            elif transaction.type == "expense":
                balance -= transaction.amount
        print(balance)

    def Summary(self):
        total_income = 0
        total_expenses = 0

        for transaction in self.transaction:
            if transaction.type == "income":
                total_income += transaction.amount
            elif transaction.type == "expense":
                total_expenses += transaction.amount

        print(f"Total Income: {total_income}")
        print(f"Total Expense: {total_expenses}")

        balance = total_income - total_expenses
        print(f"Balance: {balance}")
    
def menu():
    print("\n--- PERSONAL BUDGET MANAGER ---")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Calculate Balance")
    print("4. Financial Summary")
    print("5. Exit")


manager = BudgetManager()

while True:
    menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        manager.Add_transaction()

    elif choice == "2":
        manager.View_transaction()

    elif choice == "3":
        manager.Calculate_balance()

    elif choice == "4":
        manager.Summary()

    elif choice == "5":
        print("Exiting Budget Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-5.")

