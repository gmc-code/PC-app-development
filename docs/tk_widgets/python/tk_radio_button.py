import tkinter as tk
from tkinter import font


def display_option():
    selected_option = option_var.get()
    text_widget.delete(1.0, 'end')
    text_widget.insert(tk.END, f"You selected: {selected_option}")


root = tk.Tk()
root.title("Option Buttons")

frame = tk.Frame(root, bg="light blue")
frame.pack(padx=10, pady=10)

fontStyle = font.Font(family="Lucida Grande", size=18)

option_var = tk.StringVar(value=None)  # No default value

options = ["Option 1", "Option 2", "Option 3"]
for option in options:
    button = tk.Radiobutton(frame, text=option, variable=option_var, value=option, command=display_option, bg="white", fg="black", font=fontStyle)
    button.pack(side="left", padx=5)

text_widget = tk.Text(root, height=2, width=30, bg="white", fg="black", font=fontStyle)
text_widget.pack(padx=10, pady=10)

root.mainloop()
