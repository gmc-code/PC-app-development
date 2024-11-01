import tkinter as tk

root = tk.Tk()
button = tk.Button(root, text="Click Me")
button.pack()
print(button.info_patchlevel())
