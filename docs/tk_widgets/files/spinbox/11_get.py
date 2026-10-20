# tk Spinbox - get

import tkinter as tk


def calculate():
    pizzas = int(pizza_spinbox.get())      # Text -> number
    result_label.config(text=f"{pizzas * 8} slices")


root = tk.Tk()
root.geometry("300x200")
root.title("get")

question_label = tk.Label(root, text="How many pizzas?")
question_label.pack(pady=5)

pizza_spinbox = tk.Spinbox(root, from_=1, to=20, width=5)
pizza_spinbox.pack()

slices_button = tk.Button(root, text="How many slices?", command=calculate)
slices_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
