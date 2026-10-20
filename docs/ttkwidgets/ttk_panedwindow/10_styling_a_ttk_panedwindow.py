# ttk PanedWindow - Styling a ttk PanedWindow

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("PanedWindow style")

style = ttk.Style()
style.theme_use("clam")
style.configure("TPanedwindow", background="red")
style.configure("Sash", sashthickness=10)

panes = ttk.PanedWindow(root, orient="horizontal")
panes.pack(fill="both", expand=True)

panes.add(tk.Label(panes, text="Left", bg="white"), weight=1)
panes.add(tk.Label(panes, text="Right", bg="white"), weight=1)

root.mainloop()
