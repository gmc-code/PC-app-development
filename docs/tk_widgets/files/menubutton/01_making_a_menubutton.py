# tk Menubutton - Making a Menubutton

import tkinter as tk            # Load the tkinter library


def say(word):
    message_label.config(text=word)


root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first Menubutton")

greet_button = tk.Menubutton(root, text="Greetings", relief="raised")   # 1. Create it

greet_menu = tk.Menu(greet_button, tearoff=0)                           # 2. Its menu
greet_menu.add_command(label="Hello", command=lambda: say("Hello!"))    # 3. Add commands
greet_menu.add_command(label="Goodbye", command=lambda: say("Goodbye!"))

greet_button.config(menu=greet_menu)                                    # 4. Link them
greet_button.pack(pady=20)                                              # 5. Place it

message_label = tk.Label(root, text="", font=("Arial", 16))
message_label.pack()

root.mainloop()                 # Keep the window open
