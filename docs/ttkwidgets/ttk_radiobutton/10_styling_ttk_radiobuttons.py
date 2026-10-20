# ttk Radiobutton - Styling ttk Radiobuttons

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Radiobutton style")

style = ttk.Style()
style.theme_use("clam")
style.configure("TRadiobutton", font=("Arial", 14), background="lavender")
style.map("TRadiobutton", foreground=[("selected", "purple")],
          indicatorbackground=[("selected", "violet")])

pet = tk.StringVar(value="Dog")
for choice in ["Dog", "Cat", "Rabbit"]:
    ttk.Radiobutton(root, text=choice, variable=pet, value=choice).pack(pady=3)

root.mainloop()
