# tk Button - A Quit button

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Quit")

quit_button = tk.Button(root, text="Quit", bg="salmon", command=root.destroy)
quit_button.pack(pady=20)

root.mainloop()
