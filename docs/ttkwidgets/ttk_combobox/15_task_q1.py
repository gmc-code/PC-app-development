# ttk Combobox - Tasks Q1

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Holidays")

holiday_box = ttk.Combobox(root, values=["Beach", "Snow", "City", "Camping"],
                           state="readonly")
holiday_box.set("Beach")
holiday_box.pack(pady=30)

root.mainloop()
