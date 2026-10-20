# tk Button - invoke

import tkinter as tk


def say_hello():
    message_label.config(text="Hello!")


root = tk.Tk()
root.geometry("300x200")
root.title("invoke")

hello_button = tk.Button(root, text="Say hello", command=say_hello)
hello_button.pack(pady=20)

message_label = tk.Label(root, text="Click or press Enter", font=("Arial", 16))
message_label.pack()

root.bind("<Return>", lambda event: hello_button.invoke())

root.mainloop()
