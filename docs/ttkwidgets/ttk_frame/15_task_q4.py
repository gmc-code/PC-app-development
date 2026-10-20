# ttk Frame - Tasks Q4

import tkinter as tk
from tkinter import ttk


def start():
    start_frame.pack_forget()
    game_frame.pack(pady=30)


root = tk.Tk()
root.geometry("300x200")
root.title("Game")

start_frame = ttk.Frame(root)
start_frame.pack(pady=30)
ttk.Button(start_frame, text="Start", command=start).pack()

game_frame = ttk.Frame(root)
ttk.Label(game_frame, text="Game started!", font=("Arial", 18)).pack()

root.mainloop()
