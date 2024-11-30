import tkinter as tk

# Define the shops with items
blacksmith = {
    "name": "Blacksmith",
    "items": {
        "sword": 150,
        "shield": 100,
        "armor": 300,
        "helmet": 75,
        "boots": 50
    },
}

alchemy_shop = {
    "name": "Alchemy Shop",
    "items": {
        "health potion": 50,
        "mana potion": 60,
        "strength potion": 120,
        "invisibility potion": 200,
        "antidote": 30,
    },
}

general_store = {
    "name": "General Store",
    "items": {
        "rope": 10,
        "torch": 5,
        "rations": 20,
        "water flask": 15,
        "map": 25
    },
}

stores = [blacksmith, alchemy_shop, general_store]

# Create an empty shopping cart and set initial gold
cart = {}
purse = 1000


def deselect_others(store_name, selected_index):
    """Ensure only one item can be selected per store."""
    for i, var in enumerate(selected_items[store_name]):
        if i != selected_index:
            var.set(False)


def create_deselect_command(store_name, index):
    """Creates a command to deselect other checkboxes in the same store."""

    def deselect_others():
        for i, var in enumerate(selected_items[store_name]):
            if i != index:
                var.set(False)

    return deselect_others


def update_store():
    # Refresh the store frames
    for i in range(len(stores)):
        store = stores[i]
        frame = store_frames[i]

        # Destroy all existing widgets in the frame
        for widget in frame.winfo_children():
            widget.destroy()

        # Create store label with background color matching the frame
        store_label = tk.Label(
            frame,
            text=store["name"],
            font=("Helvetica", 16),
            bg=store_colors[store["name"]],
        )
        store_label.pack(pady=10)

        # Create checkboxes for each item in the store
        for index, (item, price) in enumerate(store["items"].items()):
            var = tk.BooleanVar(value=False)
            selected_items[store["name"]][index] = var

            # Call function to deselect other checkboxes in the store
            deselect_command = create_deselect_command(store["name"], index)

            item_check = tk.Checkbutton(
                frame,
                text=f"{item} ({price} gold)",
                variable=var,
                font=("Helvetica", 12),
                command=deselect_command,  # Use the deselect function
                bg=store_colors[store[
                    "name"]],  # Set background color to match store frame
            )
            item_check.pack(anchor="w", pady=5)


def update_inventory_display():
    """Update the inventory display to show the current cart and remaining gold."""
    inventory_text.delete(1.0, tk.END)  # Clear the existing content

    # Display purchased items
    inventory_text.insert(tk.END, "Purchased Items:\n")
    for item, price in cart.items():
        inventory_text.insert(tk.END, f"{item}: {price} gold\n")

    # Display remaining gold
    inventory_text.insert(tk.END, f"\nRemaining Gold: {purse} gold")


def buy_items():
    global purse
    for store in stores:
        store_name = store["name"]
        items_to_remove = []  # Track items to remove after purchase
        for i, (item, price) in enumerate(store["items"].items()):
            if selected_items[store_name][i].get(
            ):  # Check if this item was selected
                if purse >= price:
                    purse -= price
                    cart[item] = price
                    # Mark item for removal from the store
                    items_to_remove.append(item)
                    purse_label.config(text=f"Gold: {purse}")
                else:
                    # Insufficient gold, just skip this item
                    continue

        # Remove bought items from the store's inventory
        for item in items_to_remove:
            store["items"].pop(item)

    update_store()  # Refresh the store display to remove purchased items
    update_inventory_display(
    )  # Update the inventory display with purchased items


# Initialize the Tkinter root window
root = tk.Tk()
window.title("Shop Game")

# Define colors for each store
store_colors = {
    "Blacksmith": "#D3D3D3",
    "Alchemy Shop": "#E6E6FA",
    "General Store": "#FFFACD",
}

# Create frames for each store (left side)
store_frames = []
for store in stores:
    frame = tk.Frame(root, bg=store_colors[store["name"]])
    frame.pack(side=tk.LEFT, padx=10, pady=10)
    store_frames.append(frame)

# Create a dictionary of BooleanVars for each store
selected_items = {}
for store in stores:
    selected_items[store["name"]] = []
    for _ in store["items"]:
        selected_items[store["name"]].append(tk.BooleanVar(value=False))

# Create a right side frame for displaying inventory and remaining gold
right_frame = tk.Frame(root)
right_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Label to display current gold
purse_label = tk.Label(right_frame,
                       text=f"Gold: {purse}",
                       font=("Helvetica", 14))
purse_label.pack(pady=10)

# Label to display the shopping cart and purchased items
inventory_label = tk.Label(right_frame,
                           text="Inventory:",
                           font=("Helvetica", 14))
inventory_label.pack(pady=10)

inventory_text = tk.Text(right_frame, height=15, width=30, wrap=tk.WORD)
inventory_text.pack(pady=10)

# Button to buy item
buy_button = tk.Button(right_frame,
                       text="Buy Items",
                       command=buy_items,
                       font=("Helvetica", 14))
buy_button.pack(pady=10)

update_store()

window.mainloop()
