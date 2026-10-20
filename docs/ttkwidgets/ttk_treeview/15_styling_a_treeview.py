# ttk Treeview - Styling a Treeview

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("340x240")
root.title("Treeview style")

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", font=("Arial", 12), rowheight=28, background="white",
                fieldbackground="white")
style.configure("Treeview.Heading", font=("Arial", 12, "bold"), foreground="white",
                background="teal")
style.map("Treeview", background=[("selected", "gold")], foreground=[("selected", "black")])

table = ttk.Treeview(root, columns=("name", "score"), show="headings", height=5)
table.heading("name", text="Name")
table.heading("score", text="Score")
for row in [("Ava", 95), ("Ben", 88), ("Chloe", 91)]:
    table.insert("", tk.END, values=row)
table.pack(pady=10)

root.mainloop()
