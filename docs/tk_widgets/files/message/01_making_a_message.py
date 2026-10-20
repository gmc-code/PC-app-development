# tk Message - Making a Message

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first message")  # Words in the title bar

rules = tk.Message(root, text="Answer each question by clicking a button. "
                              "You get one point for each correct answer. "
                              "Good luck!")          # 1. Create the message
rules.pack(pady=10)                                  # 2. Place it in the window

root.mainloop()                 # Keep the window open
