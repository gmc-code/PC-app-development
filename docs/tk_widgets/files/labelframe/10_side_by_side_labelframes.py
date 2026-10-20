# tk LabelFrame - Side-by-side LabelFrames

import tkinter as tk

root = tk.Tk()
root.geometry("350x200")
root.title("Side by side")

player_1 = tk.LabelFrame(root, text="Player 1", padx=20, pady=10)
player_1.pack(side="left", padx=10, pady=20)
tk.Label(player_1, text="Score: 0", font=("Arial", 14)).pack()

player_2 = tk.LabelFrame(root, text="Player 2", padx=20, pady=10)
player_2.pack(side="left", padx=10, pady=20)
tk.Label(player_2, text="Score: 0", font=("Arial", 14)).pack()

root.mainloop()
