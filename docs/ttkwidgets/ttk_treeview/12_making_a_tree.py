# ttk Treeview - Making a tree

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x250")
root.title("A tree")

tree = ttk.Treeview(root, show="tree", height=10)

science = tree.insert("", tk.END, text="Science", open=True)    # Parent rows
maths = tree.insert("", tk.END, text="Maths")

tree.insert(science, tk.END, text="Biology")                    # Rows inside Science
tree.insert(science, tk.END, text="Chemistry")
physics = tree.insert(science, tk.END, text="Physics")
tree.insert(physics, tk.END, text="Forces")                     # Inside Physics

tree.insert(maths, tk.END, text="Algebra")                      # Rows inside Maths
tree.insert(maths, tk.END, text="Geometry")

tree.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
