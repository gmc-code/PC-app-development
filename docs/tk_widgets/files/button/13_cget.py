# tk Button - cget

import tkinter as tk


def switch():
    if light_button.cget("text") == "ON":
        light_button.config(text="OFF", bg="gray")
    else:
        light_button.config(text="ON", bg="yellow")


root = tk.Tk()
root.geometry("300x200")
root.title("cget")

light_button = tk.Button(root, text="OFF", bg="gray", font=("Arial", 20), width=6,
                         command=switch)
light_button.pack(pady=20)

root.mainloop()
