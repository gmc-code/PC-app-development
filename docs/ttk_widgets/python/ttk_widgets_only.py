import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("TTK — only Widgets")

# ---------------------------------------------------------
# THEME SELECTOR (at top)
# ---------------------------------------------------------
style = ttk.Style()

def change_theme(event=None):
    style.theme_use(theme_box.get())

ttk.Label(root, text="Select Theme:", padding=5).pack(anchor="w")

theme_box = ttk.Combobox(root, values=style.theme_names(), state="readonly")
theme_box.pack(anchor="w", padx=5, pady=(0,10))
theme_box.set(style.theme_use())   # show current theme
theme_box.bind("<<ComboboxSelected>>", change_theme)

# ---------------------------------------------------------
# MAIN SHOWCASE FRAME
# ---------------------------------------------------------
main = ttk.Frame(root, padding=12)
main.pack(fill="both", expand=True)

# Title
ttk.Label(main, text="TTK-Only Widgets",
          font=("Segoe UI", 14, "bold")).grid(row=0, column=0, columnspan=4, pady=(0,12))

# Combobox
ttk.Label(main, text="Combobox").grid(row=1, column=0, sticky="w", pady=(0,8))
ttk.Combobox(main, values=["One", "Two", "Three"]).grid(row=1, column=1, sticky="ew", pady=(0,8))

# Notebook
ttk.Label(main, text="Notebook").grid(row=2, column=0, sticky="w", pady=(0,8))
nb = ttk.Notebook(main)
nb.add(ttk.Frame(nb), text="Tab 1")
nb.add(ttk.Frame(nb), text="Tab 2")
nb.add(ttk.Frame(nb), text="Tab 3")
nb.grid(row=2, column=1, sticky="ew", pady=(0,8))

# Progressbar
ttk.Label(main, text="Progressbar").grid(row=4, column=0, sticky="w", pady=(0,8))
ttk.Progressbar(main, mode="determinate", value=20).grid(row=4, column=1, sticky="ew", pady=(0,8))

# Separator
ttk.Label(main, text="Separator").grid(row=5, column=0, sticky="w", pady=(0,8))
ttk.Separator(main, orient="horizontal").grid(row=5, column=1, sticky="ew", pady=(0,8))

# Sizegrip
ttk.Label(main, text="Sizegrip").grid(row=6, column=0, sticky="w", pady=(0,8))
ttk.Sizegrip(main).grid(row=6, column=1, sticky="w", pady=(0,8))

# Treeview
ttk.Label(main, text="Treeview").grid(row=3, column=0, sticky="w", pady=(0,8))
tree = ttk.Treeview(main, columns=("A", "B"), show="headings", height=4)
tree.heading("A", text="A")
tree.heading("B", text="B")
tree.insert("", "end", values=("Row 1", "Value 1"))
tree.insert("", "end", values=("Row 2", "Value 2"))
tree.grid(row=3, column=1, sticky="ew", pady=(0,8))


root.mainloop()
