# ttk LabelFrame - Tasks Q4

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x220")
root.title("Seasons")

style = ttk.Style()
style.configure("TLabelframe.Label", font=("Arial", 14, "bold"), foreground="purple")

season_box = ttk.LabelFrame(root, text="Favourite season", padding=10)
season_box.pack(pady=10)

season = tk.StringVar(value="Summer")
for choice in ["Summer", "Autumn", "Winter", "Spring"]:
    ttk.Radiobutton(season_box, text=choice, variable=season,
                    value=choice).pack(anchor="w")

root.mainloop()
