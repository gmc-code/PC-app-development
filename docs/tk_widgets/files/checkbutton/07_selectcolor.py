# tk Checkbutton - selectcolor

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("selectcolor")

sport = tk.IntVar()

sport_check = tk.Checkbutton(root, text="Sport", variable=sport,
                             font=("Arial", 16), selectcolor="lightgreen")
sport_check.pack(pady=20)

root.mainloop()
