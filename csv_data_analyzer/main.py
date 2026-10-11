import csv

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    best_product = ""
    highest_revenue = 0
    total_revenue = 0
    count = 0
    category_revenue = {}
    for row in reader:
        count += 1
        price = int(row["price"])
        quantity = int(row["quantity"])


        revenue = price * quantity
        total_revenue += revenue

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
    average  = total_revenue / count
    
    print(f"Total Revenue: {total_revenue}")
    print(f"Best Product: {best_product}")
    print(f"Highest Revenue: {highest_revenue}")
    print(f"Average: {average}")