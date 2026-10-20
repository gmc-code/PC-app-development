# ttk Progressbar - Styling a Progressbar

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Progressbar style")

style = ttk.Style()
style.theme_use("clam")
style.configure("Horizontal.TProgressbar", background="green", troughcolor="lightgray",
                thickness=25)
style.configure("Red.Horizontal.TProgressbar", background="red", lightcolor="red",
                darkcolor="red", troughcolor="mistyrose", thickness=25)

ttk.Label(root, text="Battery").pack(pady=5)
ttk.Progressbar(root, length=250, value=80).pack()

ttk.Label(root, text="Health").pack(pady=5)
ttk.Progressbar(root, length=250, value=20, style="Red.Horizontal.TProgressbar").pack()

root.mainloop()
