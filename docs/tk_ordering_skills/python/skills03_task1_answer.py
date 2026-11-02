import tkinter as tk


# 1. DATA DICTIONARIES & LISTS


# 2. CONSTANTS
# Colours
BG_COLOUR = "#e0ffe0"        # pale green background
TITLE_COLOUR = "#000080"     # dark blue title
TEXT_COLOUR = "#2f4f2f"      # dark green text

# Fonts
TITLE_FONT = ("Segoe UI", 20, "bold")
LABEL_FONT = ("Segoe UI", 13, "normal")


# 3. DEFINITIONS


# 4. TKINTER WIDGETS
# Main window
root = tk.Tk()
root.title("Juice Bar")
root.geometry("400x300")
root.config(bg=BG_COLOUR)

# Title
title_label = tk.Label(root)  # 1. create
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")  # 2. position
title_label.config(text="Juice Bar", font=TITLE_FONT, bg=BG_COLOUR, fg=TITLE_COLOUR)  # 3. configure

# Juice heading
juice_label = tk.Label(root)  # 1. create
juice_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")  # 2. position
juice_label.config(text="Pick a juice:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure


# 5. MAIN CODE
root.mainloop()
