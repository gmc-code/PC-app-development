import tkinter as tk


# 1. DATA DICTIONARIES & LISTS
# Juices and the price of a regular cup
juices = {
    "Orange": 5.00,
    "Apple": 4.50,
    "Mango": 6.00,
    "Watermelon": 5.50,
    "Pineapple": 5.50,
}


# 2. CONSTANTS
BG_COLOUR = "#fff8dc"        # pale cream background
TEXT_COLOUR = "#2f4f2f"      # dark green text
ADD_COLOUR = "#c8f0c8"       # pale green button

LABEL_FONT = ("Segoe UI", 13, "normal")
RADIO_FONT = ("Segoe UI", 12, "normal")
BUTTON_FONT = ("Segoe UI", 12, "bold")


# 3. DEFINITIONS


def show_juice_choice():
    """Shows the juice that is picked and its price."""
    juice = juice_var.get()
    choice_label.config(text=f"You picked {juice}: ${juices[juice]:.2f}")


# 4. TKINTER WIDGETS
# Main window
root = tk.Tk()
root.title("Juice Bar")
root.geometry("450x300")
root.config(bg=BG_COLOUR)

# Juice (radio buttons)
juice_label = tk.Label(root)  # 1. create
juice_label.grid(row=0, column=0, padx=10, pady=10, sticky="ne")  # 2. position
juice_label.config(text="Juice:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

juice_frame = tk.Frame(root)  # 1. create
juice_frame.grid(row=0, column=1, padx=10, pady=10, sticky="w")  # 2. position
juice_frame.config(bg=BG_COLOUR)  # 3. configure

juice_var = tk.StringVar(root)  # A. make
juice_var.set("Orange")  # B. set

for juice in juices.keys():
    juice_radio = tk.Radiobutton(juice_frame, variable=juice_var, value=juice)  # 1. create
    juice_radio.pack(anchor="w")  # 2. position
    juice_radio.config(text=f"{juice} (${juices[juice]:.2f})", font=RADIO_FONT,
                       bg=BG_COLOUR, fg=TEXT_COLOUR, activebackground=BG_COLOUR,
                       highlightthickness=0)  # 3. configure

# Show button
show_button = tk.Button(root)  # 1. create
show_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")  # 2. position
show_button.config(text="Show my choice", font=BUTTON_FONT, bg=ADD_COLOUR, fg=TEXT_COLOUR)  # 3. configure
show_button.config(command=show_juice_choice)  # 4. command

# Choice
choice_label = tk.Label(root)  # 1. create
choice_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")  # 2. position
choice_label.config(text="", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure


# 5. MAIN CODE
root.mainloop()
