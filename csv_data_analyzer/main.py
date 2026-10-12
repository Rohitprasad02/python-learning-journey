import csv

def calculate_revenue(price, quantity):
    return price * quantity
def calculate_profit(revenue, total_cost):
    return revenue - total_cost

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    best_product = ""
    highest_revenue = 0
    total_revenue = 0
    total_profit = 0
    count = 0
    category_revenue = {}
    for row in reader:
        count += 1
        price = int(row["price"])
        quantity = int(row["quantity"])
        cost_price = int(row["cost_price"])


        revenue = calculate_revenue(price, quantity)
        total_cost = cost_price * quantity
        profit = calculate_profit(revenue, total_cost)
        total_profit += profit
        total_revenue += revenue
        print(f"{row['product']} - Profit: ₹{profit}")

        if revenue > highest_revenue:
            highest_revenue = revenue
            best_product = row["product"]

        category = row["category"]

        if category not in category_revenue:
            category_revenue[category] = 0

        category_revenue[category] += revenue

        print(f"{row['product']} - Revenue: {revenue}")

    print("Category-wise Revenue:")

    for category, amount in category_revenue.items():
        print(f"{category}: {amount}")
    if count > 0:
        average = total_revenue / count
        print(f"Average Revenue: ₹{average:.2f}")
    else:
        print("No sales data available.")

    print("Profit:", profit)
    print(f"Total Revenue: {total_revenue}")
    print(f"Best Product: {best_product}")
    print(f"Highest Revenue: {highest_revenue}")