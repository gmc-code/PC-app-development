# ttk Progressbar - Filling the bar with after

import tkinter as tk
from tkinter import ttk


def fill():
    if bar["value"] < 100:
        bar["value"] = bar["value"] + 2
        percent_label.config(text=f"{int(bar['value'])}%")
        root.after(50, fill)                    # Run again in 50 milliseconds
    else:
        percent_label.config(text="Download complete!")


def begin():
    bar["value"] = 0
    fill()


root = tk.Tk()
root.geometry("300x200")
root.title("Download")

bar = ttk.Progressbar(root, length=250)
bar.pack(pady=20)

percent_label = ttk.Label(root, text="0%", font=("Arial", 14))
percent_label.pack()

ttk.Button(root, text="Download", command=begin).pack(pady=10)

root.mainloop()
