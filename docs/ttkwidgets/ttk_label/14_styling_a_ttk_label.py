# ttk Label - Styling a ttk Label

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x220")
root.title("Label styles")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))                                  # Every label
style.configure("Title.TLabel", font=("Arial", 22, "bold"), foreground="navy")
style.configure("Warning.TLabel", foreground="white", background="red", padding=5)

ttk.Label(root, text="My App", style="Title.TLabel").pack(pady=10)
ttk.Label(root, text="A normal label").pack(pady=5)
ttk.Label(root, text="Save your work!", style="Warning.TLabel").pack(pady=5)

root.mainloop()
