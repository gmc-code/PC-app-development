# tk LabelFrame - font and fg

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("font and fg")

scores = tk.LabelFrame(root, text="High scores", font=("Arial", 14, "bold"), fg="darkblue",
                       padx=10, pady=10)
scores.pack(pady=20)

tk.Label(scores, text="Ava: 120").pack()
tk.Label(scores, text="Ben: 95").pack()

root.mainloop()
