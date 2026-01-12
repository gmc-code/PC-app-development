import tkinter as tk

root = tk.Tk()


label1 = tk.Label(root, text="ipadx=10, ipady=5", bg="red", fg="white")
label1.pack(ipadx=10, ipady=5)
label2 = tk.Label(root, text="ipadx=20, ipady=10", bg="purple", fg="white")
label2.pack(ipadx=20, ipady=10)
label3 = tk.Label(root, text="ipadx=30, ipady=20", bg="blue", fg="white")
label3.pack(ipadx=30, ipady=20)


root.mainloop()

