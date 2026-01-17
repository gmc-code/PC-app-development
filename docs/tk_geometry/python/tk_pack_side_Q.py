import tkinter as tk

root = tk.Tk()
root.title("pack side Q")
root.geometry("250x150")

button1 = tk.Button(text="1 Top", bg="lightgreen")
button2 = tk.Button(text="2 Bottom", bg="khaki")
button3 = tk.Button(text="3 Left", bg="lightblue")
button4 = tk.Button(text="4 Right", bg="lightcoral")

button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="left")
button4.pack(side="left")

root.mainloop()
