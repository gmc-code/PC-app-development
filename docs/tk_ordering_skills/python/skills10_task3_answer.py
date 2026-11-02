import tkinter as tk


# 1. DATA DICTIONARIES & LISTS
# Extras and their extra cost
extras = {"No extra": 0.00, "Cheese": 1.00, "Guacamole": 1.50}


# 2. CONSTANTS
LABEL_FONT = ("Segoe UI", 13, "normal")


# 3. DEFINITIONS


# 4. TKINTER WIDGETS
# Main window
root = tk.Tk()
root.title("Taco Truck")
root.geometry("500x300")

extra_label = tk.Label(root)  # 1. create
extra_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")  # 2. position
extra_label.config(text="Extra:", font=LABEL_FONT)  # 3. configure

extra_var = tk.StringVar(root)  # A. make
extra_var.set("No extra")  # B. set

extra_menu = tk.OptionMenu(root, extra_var, "No extra")  # 1. create
extra_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")  # 2. position
extra_menu.config(width=12, font=LABEL_FONT)  # 3. configure

extra_choices = extra_menu["menu"]
extra_choices.delete(0)   # remove the starting choice
for extra in extras.keys():
    extra_choices.add_radiobutton(label=extra, variable=extra_var, value=extra)


# 5. MAIN CODE
root.mainloop()
