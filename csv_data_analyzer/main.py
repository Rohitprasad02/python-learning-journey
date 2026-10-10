import csv

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    total_revenue = 0
    for row in reader:
        price = int(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity
        total_revenue += revenue
        print(f"{row['product']} - Revenue: {revenue}")
    print(f"Total Revenue: {total_revenue}")