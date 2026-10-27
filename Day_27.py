sales = [
    {"product": "Keyboard", "price": 1200, "cost": 800, "quantity": 2},
    {"product": "Mouse", "price": 500, "cost": 250, "quantity": 4},
    {"product": "Monitor", "price": 8500, "cost": 7000, "quantity": 1},
    {"product": "Headphones", "price": 1800, "cost": 1100, "quantity": 3},
]

total = 0
total_profit = 0

for product in sales:
    revenue = product["price"] * product["quantity"]
    profit = (product["price"] - product["cost"]) * product["quantity"]

    total += revenue
    total_profit += profit

    print(product["product"], "Revenue:", revenue, "Profit:", profit)

top_product = max(
    sales,
    key=lambda product: product["price"] * product["quantity"]
)
average_Revenue = total / len(sales)

print("Average revenue:", average_Revenue)
print("Top product:", top_product["product"])
print("Revenue:", top_product["price"] * top_product["quantity"])