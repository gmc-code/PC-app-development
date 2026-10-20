# ttk Progressbar - Changing colour as it fills

import tkinter as tk
from tkinter import ttk


def update(value):
    level = int(float(value))
    bar["value"] = level
    if level < 30:
        bar.config(style="Low.Horizontal.TProgressbar")
    elif level < 70:
        bar.config(style="Mid.Horizontal.TProgressbar")
    else:
        bar.config(style="High.Horizontal.TProgressbar")


root = tk.Tk()
root.geometry("300x200")
root.title("Traffic light bar")

style = ttk.Style()
style.theme_use("clam")
style.configure("Low.Horizontal.TProgressbar", background="red", thickness=25)
style.configure("Mid.Horizontal.TProgressbar", background="orange", thickness=25)
style.configure("High.Horizontal.TProgressbar", background="green", thickness=25)

bar = ttk.Progressbar(root, length=250, style="Low.Horizontal.TProgressbar")
bar.pack(pady=20)

ttk.Label(root, text="Drag the slider:").pack()
ttk.Scale(root, from_=0, to=100, length=250, command=update).pack(pady=5)

root.mainloop()
