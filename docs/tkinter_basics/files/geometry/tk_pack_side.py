import tkinter as tk

window = tk.Tk()
window.title("pack side")
window.geometry("250x150")

button1 = tk.Button(text="Left")
button1.pack(side="left")

button2 = tk.Button(text="Top")
button2.pack(side="top")

button3 = tk.Button(text="Right")
button3.pack(side="right")

button4 = tk.Button(text="Bottom")
button4.pack(side="bottom")

window.mainloop()
