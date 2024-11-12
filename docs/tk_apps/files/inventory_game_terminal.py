import random

# Define the shops with more diverse items
blacksmith = {
    'name': 'Blacksmith',
    'items': {
        'sword': 150,
        'shield': 100,
        'armor': 300,
        'helmet': 75,
        'boots': 50
    }
}

alchemy_shop = {
    'name': 'Alchemy Shop',
    'items': {
        'health potion': 50,
        'mana potion': 60,
        'strength potion': 120,
        'invisibility potion': 200,
        'antidote': 30
    }
}

general_store = {
    'name': 'General Store',
    'items': {
        'rope': 10,
        'torch': 5,
        'rations': 20,
        'water flask': 15,
        'map': 25
    }
}

stores = [blacksmith, alchemy_shop, general_store]

# Create an empty shopping cart and set initial gold
cart = {}
purse = 1000

# Function to display the inventory of a store with item numbers
def display_inventory(store):
    items = [f"{i+1} {item} ({price} gold)" for i, (item, price) in enumerate(store['items'].items())]
    return '\n'.join(items)

# Print initial inventory
print("Initial Inventory:")
for store in stores:
    print(f"{store['name']}:\n{display_inventory(store)}\n")

# Loop through stores
for store in stores:
    while True:
        # Input box to show what you can buy
        print(f"Welcome to {store['name']}! What do you want to buy (type 'exit' to leave):")
        print(display_inventory(store))
        buy_item = input().lower()
        if buy_item == 'exit':
            break
        if buy_item.isdigit() and 1 <= int(buy_item) <= len(store['items']):
            item_name = list(store['items'].keys())[int(buy_item) - 1]
            if purse >= store['items'][item_name]:
                purse -= store['items'][item_name]
                cart[item_name] = store['items'].pop(item_name)
                print(f"You bought {item_name} for {cart[item_name]} gold. You have {purse} gold left.")
                break
            else:
                print("You don't have enough gold for that item.")
        else:
            print("Invalid selection. Exiting store.")
            break

# Print final inventory and purchases
print("\nFinal Inventory:")
for store in stores:
    print(f"{store['name']}:\n{display_inventory(store)}\n")

print("\nItems Purchased:")
for item, price in cart.items():
    print(f"{item}: {price} gold")

print(f"\nTotal cost: {sum(cart.values())} gold")
print(f"Gold left: {purse} gold")
