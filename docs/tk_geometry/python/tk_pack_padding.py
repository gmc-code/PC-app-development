import tkinter as tk

window = tk.Tk()
window.title("pack padding")
window.geometry("250x150")

label1 = tk.Label(window, text="Red", bg="red", fg="white")
label1.pack(ipadx=30, ipady=6)

label2 = tk.Label(window, text="Purple", bg="purple", fg="white")
label2.pack(pady=20, ipadx=8, ipady=20)

window.mainloop()