# tk Radiobutton - Tasks Q3

import tkinter as tk


def show():
    result_label.config(text="You travel by " + transport.get())


root = tk.Tk()
root.geometry("300x200")
root.title("Transport")

transport = tk.StringVar(value="Walk")

bus_radio = tk.Radiobutton(root, text="Bus", variable=transport, value="Bus")
bus_radio.pack()
car_radio = tk.Radiobutton(root, text="Car", variable=transport, value="Car")
car_radio.pack()
walk_radio = tk.Radiobutton(root, text="Walk", variable=transport, value="Walk")
walk_radio.pack()

show_button = tk.Button(root, text="Show", command=show)
show_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
