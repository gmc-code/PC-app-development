import tkinter as tk

root = tk.Tk()
root.title("pack fill x")
root.geometry("250x150")

label = tk.Label(root, text="Not Expanding fill x", bg="lightblue")
label.pack(expand=False, fill='x')

root.mainloop()