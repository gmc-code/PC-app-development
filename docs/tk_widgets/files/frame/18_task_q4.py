# tk Frame - Tasks Q4

import tkinter as tk


def start():
    start_frame.pack_forget()
    game_frame.pack(pady=20)


root = tk.Tk()
root.geometry("300x200")
root.title("Game")

start_frame = tk.Frame(root)
start_frame.pack(pady=20)
tk.Button(start_frame, text="Start", command=start).pack()

game_frame = tk.Frame(root)
tk.Label(game_frame, text="Game started!", font=("Arial", 18)).pack()

root.mainloop()
