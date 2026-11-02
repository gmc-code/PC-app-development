orders = [
    {"taco": "Beef", "extra": "Cheese", "price": 5.00},
    {"taco": "Fish", "extra": "No extra", "price": 5.50},
]

total = 0
for taco in orders:
    print(f"{taco['taco']}, {taco['extra']}: ${taco['price']:.2f}")
    total = total + taco["price"]
print(f"Total: ${total:.2f}")
