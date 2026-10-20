# tk Message - config

import tkinter as tk

facts = [
    "The Sun is a star.",
    "Light from the Sun takes about 8 minutes to reach Earth.",
    "Jupiter is the largest planet in our solar system.",
]
fact_number = 0


def next_fact():
    global fact_number              # Allow the function to change fact_number
    fact_number = (fact_number + 1) % len(facts)     # Go back to 0 after the last fact
    fact_message.config(text=facts[fact_number])


root = tk.Tk()
root.geometry("300x200")
root.title("config")

fact_message = tk.Message(root, text=facts[0], width=250, font=("Arial", 14))
fact_message.pack(pady=10)

tk.Button(root, text="Next fact", command=next_fact).pack()

root.mainloop()
