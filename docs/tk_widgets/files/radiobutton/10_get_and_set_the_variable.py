# tk Radiobutton - get and set (the variable)

import tkinter as tk


def reset():
    drink.set("none")       # Matches no button, so nothing is chosen


root = tk.Tk()
root.geometry("300x200")
root.title("get and set")

drink = tk.StringVar()
drink.set("Juice")          # Start with Juice chosen

tk.Radiobutton(root, text="Water", variable=drink, value="Water").pack()
tk.Radiobutton(root, text="Juice", variable=drink, value="Juice").pack()
tk.Radiobutton(root, text="Milk", variable=drink, value="Milk").pack()

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(pady=10)

root.mainloop()
