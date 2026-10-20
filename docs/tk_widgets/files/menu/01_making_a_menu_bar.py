# tk Menu - Making a menu bar

import tkinter as tk            # Load the tkinter library


def say_hello():
    message_label.config(text="Hello!")


root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first menu")     # Words in the title bar

menubar = tk.Menu(root)                     # 1. Create the menu bar
root.config(menu=menubar)                   #    and attach it to the window

file_menu = tk.Menu(menubar, tearoff=0)     # 2. Create the File drop-down menu

file_menu.add_command(label="Say hello", command=say_hello)    # 3. Add commands
file_menu.add_command(label="Exit", command=root.destroy)

menubar.add_cascade(label="File", menu=file_menu)              # 4. Put "File" on the bar

message_label = tk.Label(root, text="Click File at the top", font=("Arial", 14))
message_label.pack(pady=40)

root.mainloop()                 # Keep the window open
