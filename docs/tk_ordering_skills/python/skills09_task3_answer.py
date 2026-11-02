import tkinter as tk


# 1. DATA DICTIONARIES & LISTS
tacos = {"Beef": 4.00, "Chicken": 4.50, "Fish": 5.50}


# 2. CONSTANTS
BG_COLOUR = "#fff0d9"
TEXT_COLOUR = "#5a2d0c"
LABEL_FONT = ("Segoe UI", 13, "normal")


# 3. DEFINITIONS


def show_taco_choice():
    """Shows the taco that is picked and its price."""
    taco = taco_var.get()
    choice_label.config(text=f"You picked {taco}: ${tacos[taco]:.2f}")


# 4. TKINTER WIDGETS
root = tk.Tk()
root.title("Taco Truck")
root.geometry("400x250")
root.config(bg=BG_COLOUR)

taco_label = tk.Label(root)  # 1. create
taco_label.grid(row=0, column=0, padx=10, pady=10, sticky="ne")  # 2. position
taco_label.config(text="Taco:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

taco_frame = tk.Frame(root)  # 1. create
taco_frame.grid(row=0, column=1, padx=10, pady=10, sticky="w")  # 2. position
taco_frame.config(bg=BG_COLOUR)  # 3. configure

taco_var = tk.StringVar(root)  # A. make
taco_var.set("Beef")  # B. set

for taco in tacos.keys():
    taco_radio = tk.Radiobutton(taco_frame, variable=taco_var, value=taco)  # 1. create
    taco_radio.pack(anchor="w")  # 2. position
    taco_radio.config(text=f"{taco} (${tacos[taco]:.2f})", font=LABEL_FONT,
                      bg=BG_COLOUR, fg=TEXT_COLOUR, activebackground=BG_COLOUR,
                      highlightthickness=0)  # 3. configure

show_button = tk.Button(root)  # 1. create
show_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")  # 2. position
show_button.config(text="Show my choice", font=LABEL_FONT)  # 3. configure
show_button.config(command=show_taco_choice)  # 4. command

choice_label = tk.Label(root)  # 1. create
choice_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")  # 2. position
choice_label.config(text="", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure


# 5. MAIN CODE
root.mainloop()
