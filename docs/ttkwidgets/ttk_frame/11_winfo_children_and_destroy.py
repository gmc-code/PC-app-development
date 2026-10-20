# ttk Frame - winfo_children and destroy

import tkinter as tk
from tkinter import ttk


def game_over():
    for widget in controls.winfo_children():
        widget.state(["disabled"])


root = tk.Tk()
root.geometry("300x220")
root.title("winfo_children")

controls = ttk.Frame(root, padding=10)
controls.pack()
for word in ["Up", "Down", "Left", "Right"]:
    ttk.Button(controls, text=word).pack()

ttk.Button(root, text="Game over", command=game_over).pack(pady=5)
ttk.Button(root, text="Remove controls", command=controls.destroy).pack()

root.mainloop()
