import tkinter as tk

root = tk.Tk()
root.title("pack padding")
root.geometry("250x150")

label1 = tk.Label(root, text="Red", bg="red", fg="white")
label1.pack(ipadx=30, ipady=6)

label2 = tk.Label(root, text="Purple", bg="purple", fg="white")
label2.pack(pady=20, ipadx=8, ipady=20)

root.mainloop()