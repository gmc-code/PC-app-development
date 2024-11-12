import tkinter as tk
from tkinter import messagebox

# Define the shops with more diverse items
blacksmith = {"name": "Blacksmith", "items": {"sword": 150,
                                              "shield": 100, "armor": 300, "helmet": 75, "boots": 50}}

alchemy_shop = {"name": "Alchemy Shop", "items": {"health potion": 50,
                                                  "mana potion": 60, "strength potion": 120, "invisibility potion": 200, "antidote": 30}}

general_store = {"name": "General Store", "items": {
    "rope": 10, "torch": 5, "rations": 20, "water flask": 15, "map": 25}}

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
    for i in range(len(stores)):
        store = stores[i]
        frame = store_frames[i]

        # Destroy all existing widgets in the frame
        for widget in frame.winfo_children():
            widget.destroy()

        # Create store label with background color matching the frame
        store_label = tk.Label(frame, text=store["name"], font=("Helvetica", 16), bg=store_colors[store["name"]])
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
                bg=store_colors[store["name"]],  # Set background color to match store frame
            )
            item_check.pack(anchor="w", pady=5)


def buy_item():
    global purse
    for store in stores:
        store_name = store["name"]
        items_to_remove = []  # Track items to remove after purchase
        for i, (item, price) in enumerate(store["items"].items()):
            if selected_items[store_name][i].get():  # Check if this item was selected
                if purse >= price:
                    purse -= price
                    cart[item] = price
                    # Mark item for removal from the store
                    items_to_remove.append(item)
                    purse_label.config(text=f"Gold: {purse}")
                    messagebox.showinfo("Purchase Successful", f"You bought {
                                        item} for {price} gold.")
                else:
                    messagebox.showwarning("Insufficient Gold", f"You don't have enough gold for {
                                           item} from {store_name}.")
                    return

        # Remove bought items from the store's inventory
        for item in items_to_remove:
            store["items"].pop(item)

    update_store()  # Refresh the store display to remove purchased items


def end_game():
    items_purchased = ""
    for item, price in cart.items():
        items_purchased += f"{item}: {price} gold\n"

    total_cost = sum(cart.values())
    gold_left = purse

    messagebox.showinfo("Game Over", f"Items Purchased:\n{
                        items_purchased}\n\nTotal cost: {total_cost} gold\nGold left: {gold_left} gold")


# Initialize the Tkinter root window
root = tk.Tk()
root.title("Shop Game")

# Define colors for each store
# Light gray for Blacksmith  # Lavender for Alchemy Shop  # Lemon chiffon for General Store
store_colors = {"Blacksmith": "#D3D3D3",
                "Alchemy Shop": "#E6E6FA", "General Store": "#FFFACD"}

# Modify store_frames creation to include colors
store_frames = []
for store in stores:
    # Set background color
    frame = tk.Frame(root, bg=store_colors[store["name"]])
    frame.pack(side=tk.LEFT, padx=10, pady=10)
    store_frames.append(frame)


# Create a dictionary of BooleanVars for each store without dictionary comprehensions
selected_items = {}
for store in stores:
    selected_items[store["name"]] = []
    for _ in store["items"]:
        selected_items[store["name"]].append(tk.BooleanVar(value=False))

purse_label = tk.Label(root, text=f"Gold: {purse}", font=("Helvetica", 14))
purse_label.pack(pady=10)

buy_button = tk.Button(root, text="Buy Item",
                       command=buy_item, font=("Helvetica", 14))
buy_button.pack(pady=10)

end_button = tk.Button(root, text="End Game",
                       command=end_game, font=("Helvetica", 14))
end_button.pack(pady=10)

update_store()

root.mainloop()
