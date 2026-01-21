import tkinter as tk

root = tk.Tk()
root.title("pack fill both")
root.geometry("250x150")

label = tk.Label(root, text="Not Expanding fill both", bg="lightblue")
label.pack(expand=False, fill='both')

root.mainloop()