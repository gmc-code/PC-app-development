# tk Radiobutton - Tasks Q1

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Transport")

transport = tk.StringVar(value="none")

bus_radio = tk.Radiobutton(root, text="Bus", variable=transport, value="Bus")
bus_radio.pack()
car_radio = tk.Radiobutton(root, text="Car", variable=transport, value="Car")
car_radio.pack()
walk_radio = tk.Radiobutton(root, text="Walk", variable=transport, value="Walk")
walk_radio.pack()

root.mainloop()
