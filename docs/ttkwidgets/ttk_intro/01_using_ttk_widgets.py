# ttk widgets and styling - Using ttk widgets

import tkinter as tk            # The window, variables and tk widgets
from tkinter import ttk         # The themed widgets

root = tk.Tk()                  # The window is still made with tk
root.geometry("300x200")
root.title("tk and ttk")

old_button = tk.Button(root, text="tk Button")      # tk version
old_button.pack(pady=10)

new_button = ttk.Button(root, text="ttk Button")    # ttk version
new_button.pack(pady=10)

root.mainloop()
