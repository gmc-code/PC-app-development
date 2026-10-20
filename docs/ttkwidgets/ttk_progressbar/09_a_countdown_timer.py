# ttk Progressbar - A countdown timer

import tkinter as tk
from tkinter import ttk

seconds_left = 10


def tick():
    global seconds_left
    if seconds_left > 0:
        seconds_left = seconds_left - 1
        timer_bar["value"] = seconds_left
        time_label.config(text=f"{seconds_left} seconds left")
        root.after(1000, tick)                  # 1000 milliseconds = 1 second
    else:
        time_label.config(text="Time's up!")


root = tk.Tk()
root.geometry("300x200")
root.title("Countdown")

timer_bar = ttk.Progressbar(root, length=250, maximum=10, value=10)
timer_bar.pack(pady=30)

time_label = ttk.Label(root, text="10 seconds left", font=("Arial", 16))
time_label.pack()

root.after(1000, tick)                          # Start counting after 1 second

root.mainloop()
