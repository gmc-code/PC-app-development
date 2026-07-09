import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("ttk Entry Task")
root.geometry("500x300")

style = ttk.Style()
style.theme_use("clam")

style.configure("Task.TEntry",
                fieldbackground="#eaeaea",
                foreground="#1f1f1f",
                )

# Create Entry widget applying a simple tuple font
# Format: ("Family", Size, "Optional Styles")
entry = ttk.Entry(root, font=("Arial Rounded MT Bold", 24),
                  style="Task.TEntry", justify="center", width=25)
entry.pack(padx=10, pady=10, ipady=8)

root.mainloop()
