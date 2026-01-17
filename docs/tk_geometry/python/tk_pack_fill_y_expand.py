import tkinter as tk

root = tk.Tk()
root.title("pack fill y")
root.geometry("250x150")

label = tk.Label(root, text="Expanding fill y", bg="lightblue")
label.pack(expand=True, fill='y')

root.mainloop()