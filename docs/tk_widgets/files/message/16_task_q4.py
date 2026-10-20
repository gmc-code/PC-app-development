# tk Message - Tasks Q4

import tkinter as tk


def change():
    fact.config(text="An octopus has three hearts!", bg="lightgreen")


root = tk.Tk()
root.geometry("300x200")
root.title("Fun fact")

fact = tk.Message(root, text="Click the button for a fun fact.", width=250)
fact.pack(pady=10)

tk.Button(root, text="Change", command=change).pack()

root.mainloop()
