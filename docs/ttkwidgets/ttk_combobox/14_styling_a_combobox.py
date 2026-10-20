# ttk Combobox - Styling a Combobox

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Combobox style")

style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", foreground="navy", arrowcolor="white", background="navy",
                padding=5)
style.map("TCombobox", fieldbackground=[("readonly", "lightyellow")])

root.option_add("*TCombobox*Listbox.font", ("Arial", 14))            # The drop-down list
root.option_add("*TCombobox*Listbox.background", "lightyellow")

animal_box = ttk.Combobox(root, values=["Koala", "Kangaroo", "Wombat"], state="readonly",
                          font=("Arial", 14))
animal_box.set("Koala")
animal_box.pack(pady=40)

root.mainloop()
