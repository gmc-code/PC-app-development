# tk Checkbutton - get and set (the variable)

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("get and set")

sound = tk.IntVar()
sound.set(1)            # Start with the box ticked

sound_check = tk.Checkbutton(root, text="Sound on", variable=sound)
sound_check.pack(pady=20)

root.mainloop()
