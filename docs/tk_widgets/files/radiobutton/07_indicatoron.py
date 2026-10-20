# tk Radiobutton - indicatoron

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("indicatoron")

level = tk.StringVar(value="Easy")

for choice in ["Easy", "Medium", "Hard"]:
    tk.Radiobutton(root, text=choice, variable=level, value=choice,
                   indicatoron=0, width=12, selectcolor="lightgreen").pack(pady=2)

root.mainloop()
