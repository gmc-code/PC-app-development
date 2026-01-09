import tkinter as tk

root = tk.Tk()
root.title("pack fill y")
root.geometry("250x150")

label = tk.Label(root, text="Not Expanding fill y", bg="lightblue")
label.pack(expand=False, fill='y')

root.mainloop()