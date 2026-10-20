# ttk Treeview - A tree with columns

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("350x250")
root.title("Tree with columns")

tree = ttk.Treeview(root, columns=("legs",), height=8)
tree.heading("#0", text="Animal")           # The tree column
tree.heading("legs", text="Legs")
tree.column("#0", width=200)
tree.column("legs", width=80, anchor="center")

mammals = tree.insert("", tk.END, text="Mammals", open=True)
tree.insert(mammals, tk.END, text="Kangaroo", values=(2,))
tree.insert(mammals, tk.END, text="Koala", values=(4,))

insects = tree.insert("", tk.END, text="Insects", open=True)
tree.insert(insects, tk.END, text="Ant", values=(6,))
tree.insert(insects, tk.END, text="Bee", values=(6,))

tree.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
