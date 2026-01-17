import tkinter as tk

root = tk.Tk()
root.title("pack fill x")
root.geometry("250x150")

label = tk.Label(root, text="Expanding fill x", bg="lightblue")
label.pack(expand=True, fill='x')

root.mainloop()