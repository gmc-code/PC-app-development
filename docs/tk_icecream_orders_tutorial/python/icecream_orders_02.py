import tkinter as tk


# 1. DATA DICTIONARIES & LISTS
# Ice cream flavours and the price of one scoop
flavours = {
    "Vanilla": 4.00,
    "Chocolate": 4.00,
    "Strawberry": 4.50,
    "Mint Choc Chip": 5.00,
    "Cookies and Cream": 5.50,
}

# Containers and their extra cost
containers = {
    "Cup": 0.00,
    "Plain cone": 0.50,
    "Waffle cone": 1.50,
}

# Toppings and their extra cost
toppings = {
    "No topping": 0.00,
    "Sprinkles": 0.50,
    "Chocolate sauce": 1.00,
    "Crushed nuts": 1.00,
}

# List that stores every ice cream in the order
orders = []


# 2. CONSTANTS


# 3. DEFINITIONS


# 4. TKINTER WIDGETS
# Main window
root = tk.Tk()
root.title("Ice Cream Shop")
root.geometry("940x520")


# 5. MAIN CODE
root.mainloop()
