# ttk Button - Tasks Q3

import tkinter as tk
from tkinter import ttk


def clicked():
    result_label.config(text="Clicked!")


root = tk.Tk()
root.geometry("300x200")
root.title("ttk Buttons")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 16), foreground="white",
                background="darkblue")

click_button = ttk.Button(root, text="Click me", width=15, padding=10,
                          command=clicked)
click_button.pack(pady=20)

result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
