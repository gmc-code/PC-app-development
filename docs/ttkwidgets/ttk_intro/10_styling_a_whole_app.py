# ttk widgets and styling - Styling a whole app

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("320x260")
root.title("Sign up")
root.config(bg="white")

# ---------- Styles ----------
style = ttk.Style()
style.theme_use("clam")
style.configure(".", font=("Arial", 12), background="white")      # "." means every widget
style.configure("Title.TLabel", font=("Arial", 20, "bold"), foreground="teal")
style.configure("TButton", foreground="white", background="teal", padding=8)
style.map("TButton", background=[("active", "darkcyan")])
style.configure("TEntry", fieldbackground="azure")

# ---------- Widgets ----------
ttk.Label(root, text="Sign up", style="Title.TLabel").pack(pady=10)

ttk.Label(root, text="Name:").pack()
ttk.Entry(root).pack(pady=2)

ttk.Label(root, text="Email:").pack()
ttk.Entry(root).pack(pady=2)

ttk.Checkbutton(root, text="Send me the newsletter").pack(pady=5)
ttk.Button(root, text="Join").pack(pady=5)

root.mainloop()
