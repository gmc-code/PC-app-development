# ttk Frame - side, fill and expand

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x250")
root.title("Layout")

style = ttk.Style()
style.configure("Top.TFrame", background="navy")
style.configure("Side.TFrame", background="lightsteelblue")
style.configure("Main.TFrame", background="white")
style.configure("Top.TLabel", background="navy", foreground="white", font=("Arial", 18))

top = ttk.Frame(root, style="Top.TFrame", padding=5)
top.pack(fill="x")
ttk.Label(top, text="Science Quiz", style="Top.TLabel").pack()

side = ttk.Frame(root, style="Side.TFrame", padding=10)
side.pack(side="left", fill="y")
ttk.Button(side, text="Start", width=10).pack(pady=5)
ttk.Button(side, text="Scores", width=10).pack(pady=5)

main = ttk.Frame(root, style="Main.TFrame")
main.pack(side="left", fill="both", expand=True)

root.mainloop()
