# tk Button - command

import tkinter as tk


def say_hello():
    message_label.config(text="Hello!")


root = tk.Tk()
root.geometry("300x200")
root.title("command")

hello_button = tk.Button(root, text="Say hello", command=say_hello)
hello_button.pack(pady=20)

message_label = tk.Label(root, text="", font=("Arial", 20))
message_label.pack()

root.mainloop()
