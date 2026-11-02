orders = []

juice = {"juice": "Mango", "size": "Large", "price": 8.00}
orders.append(juice)

juice = {"juice": "Apple", "size": "Small", "price": 4.50}
orders.append(juice)

print(orders[0]["juice"])          # prints Mango
print(orders[1]["price"])          # prints 4.5

total = 0
for juice in orders:
    print(f"{juice['juice']}, {juice['size']}: ${juice['price']:.2f}")
    total = total + juice["price"]
print(f"Total: ${total:.2f}")      # prints Total: $12.50
