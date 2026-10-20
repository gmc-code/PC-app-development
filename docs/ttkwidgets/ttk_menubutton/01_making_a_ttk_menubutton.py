# ttk Menubutton - Making a ttk Menubutton

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets


def say(word):
    message_label.config(text=word)


root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first ttk Menubutton")

greet_button = ttk.Menubutton(root, text="Greetings")                  # 1. Create it

greet_menu = tk.Menu(greet_button, tearoff=0)                          # 2. Its menu
greet_menu.add_command(label="Hello", command=lambda: say("Hello!"))   # 3. Commands
greet_menu.add_command(label="Goodbye", command=lambda: say("Goodbye!"))

greet_button.config(menu=greet_menu)                                   # 4. Link them
greet_button.pack(pady=20)                                             #    and place

message_label = ttk.Label(root, text="", font=("Arial", 16))
message_label.pack()

root.mainloop()                 # Keep the window open
