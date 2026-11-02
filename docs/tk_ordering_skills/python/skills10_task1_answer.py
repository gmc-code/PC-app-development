import tkinter as tk


# 1. DATA DICTIONARIES & LISTS
# Sizes and their extra cost
sizes = {
    "Small": 0.00,
    "Regular": 1.00,
    "Large": 2.00,
    "Jumbo": 3.00,
}


# 2. CONSTANTS
BG_COLOUR = "#fff8dc"        # pale cream background
TEXT_COLOUR = "#2f4f2f"      # dark green text
MENU_COLOUR = "#ffe4b5"      # pale orange drop-down menu
ADD_COLOUR = "#c8f0c8"       # pale green button

LABEL_FONT = ("Segoe UI", 13, "normal")
BUTTON_FONT = ("Segoe UI", 12, "bold")


# 3. DEFINITIONS


def show_size_choice():
    """Shows the size that is picked and its extra cost."""
    size = size_var.get()
    choice_label.config(text=f"{size} costs ${sizes[size]:.2f} extra")


# 4. TKINTER WIDGETS
# Main window
root = tk.Tk()
root.title("Juice Bar")
root.geometry("500x300")
root.config(bg=BG_COLOUR)

# Size (drop-down menu)
size_label = tk.Label(root)  # 1. create
size_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")  # 2. position
size_label.config(text="Size:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

size_var = tk.StringVar(root)  # A. make
size_var.set("Small")  # B. set

size_menu = tk.OptionMenu(root, size_var, "Small")  # 1. create
size_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")  # 2. position
size_menu.config(width=12, font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR,
                 activebackground=MENU_COLOUR)  # 3. configure

size_choices = size_menu["menu"]
size_choices.config(font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR)
size_choices.delete(0)   # remove the starting choice
for size in sizes.keys():
    size_choices.add_radiobutton(label=size, variable=size_var, value=size)

# Show button
show_button = tk.Button(root)  # 1. create
show_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")  # 2. position
show_button.config(text="Show my choice", font=BUTTON_FONT, bg=ADD_COLOUR, fg=TEXT_COLOUR)  # 3. configure
show_button.config(command=show_size_choice)  # 4. command

# Choice
choice_label = tk.Label(root)  # 1. create
choice_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")  # 2. position
choice_label.config(text="", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure


# 5. MAIN CODE
root.mainloop()
