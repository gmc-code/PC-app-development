# ttk LabelFrame - Side-by-side LabelFrames

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("350x200")
root.title("Scoreboard")

for team in ["Home", "Away"]:
    box = ttk.LabelFrame(root, text=team, padding=(30, 10))
    box.pack(side="left", padx=15, pady=30)
    ttk.Label(box, text="0", font=("Arial", 30)).pack()

root.mainloop()
