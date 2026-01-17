import tkinter as tk

root = tk.Tk()
root.title("pack side")
root.geometry("250x150")

button1 = tk.Button(text="1 Top", bg="lightgreen")
button1.pack(side="top")

button2 = tk.Button(text="2 Bottom", bg="khaki")
button2.pack(side="bottom")

button3 = tk.Button(text="3 Left", bg="lightblue")
button3.pack(side="left")

button4 = tk.Button(text="4 Right", bg="lightcoral")
button4.pack(side="right")

root.mainloop()
