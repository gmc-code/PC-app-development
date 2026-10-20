# tk Checkbutton - text

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("text")

agree = tk.IntVar()

agree_check = tk.Checkbutton(root, text="I agree to the rules", variable=agree)
agree_check.pack(pady=20)

root.mainloop()
