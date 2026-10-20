# tk LabelFrame - Tasks Q3

import tkinter as tk

root = tk.Tk()
root.geometry("300x250")
root.title("Seasons")

season_box = tk.LabelFrame(root, text="Favourite season", padx=10, pady=5)
season_box.pack(pady=10)

season = tk.StringVar(value="Summer")
for choice in ["Summer", "Autumn", "Winter", "Spring"]:
    tk.Radiobutton(season_box, text=choice, variable=season,
                   value=choice).pack(anchor="w")

root.mainloop()
