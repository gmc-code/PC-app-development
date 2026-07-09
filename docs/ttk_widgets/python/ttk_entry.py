import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("ttk Entry Alphabet Example")
root.geometry("400x300")

style = ttk.Style()
style.theme_use("clam")

style.configure("Task.TEntry",
                fieldbackground="#fafafa",
                foreground="#2f2f2f",
                )

entry = ttk.Entry(root, style="Task.TEntry", font=("Comic Sans MS", 16), justify="left", width=20)
entry.pack(padx=20, pady=20, ipady=5)

root.mainloop()
