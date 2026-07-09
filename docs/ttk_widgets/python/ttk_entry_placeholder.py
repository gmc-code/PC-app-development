import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ttk Entry Alphabet Example")
root.geometry("400x300")

style = ttk.Style()
style.theme_use("clam")

# style.configure is only for the looks!
style.configure(
    "Task.TEntry",
    fieldbackground="#fafafa",
    foreground="#2f2f2f"
)

entry = ttk.Entry(root, font=("Comic Sans MS", 16), style="Task.TEntry", justify="left", width=20)
entry.pack(padx=20, pady=20, ipady=5)

# --- Placeholder Logic ---
placeholder = "Enter your name here"
entry.insert(0, placeholder)

def on_focus_in(event):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)

def on_focus_out(event):
    if not entry.get():
        entry.insert(0, placeholder)

# Bind the click/focus events to the entry box
entry.bind("<FocusIn>", on_focus_in)
entry.bind("<FocusOut>", on_focus_out)

root.mainloop()