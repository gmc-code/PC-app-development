# ttk Button - Making a ttk Button

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets


def say_hello():
    message_label.config(text="Hello!")


root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first ttk Button")

hello_button = ttk.Button(root, text="Say hello", command=say_hello)   # 2. Create
hello_button.pack(pady=20)                                            # 3. Place

message_label = ttk.Label(root, text="", font=("Arial", 18))
message_label.pack()

root.mainloop()                 # Keep the window open
