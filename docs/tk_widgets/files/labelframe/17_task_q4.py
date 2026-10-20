# tk LabelFrame - Tasks Q4

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Scoreboard")

home = tk.LabelFrame(root, text="Home", padx=20, pady=10)
home.pack(side="left", padx=10, pady=20)
tk.Label(home, text="0", font=("Arial", 24)).pack()

away = tk.LabelFrame(root, text="Away", padx=20, pady=10)
away.pack(side="left", padx=10, pady=20)
tk.Label(away, text="0", font=("Arial", 24)).pack()

root.mainloop()
