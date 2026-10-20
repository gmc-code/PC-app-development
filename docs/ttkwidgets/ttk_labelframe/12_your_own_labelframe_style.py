# ttk LabelFrame - Your own LabelFrame style

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("350x200")
root.title("Custom LabelFrame style")

style = ttk.Style()
style.configure("Red.TLabelframe.Label", foreground="red", font=("Arial", 13, "bold"))
style.configure("Blue.TLabelframe.Label", foreground="blue", font=("Arial", 13, "bold"))

red_team = ttk.LabelFrame(root, text="Red team", style="Red.TLabelframe", padding=15)
red_team.pack(side="left", padx=20, pady=30)
ttk.Label(red_team, text="Score: 0").pack()

blue_team = ttk.LabelFrame(root, text="Blue team", style="Blue.TLabelframe", padding=15)
blue_team.pack(side="left", padx=20, pady=30)
ttk.Label(blue_team, text="Score: 0").pack()

root.mainloop()
