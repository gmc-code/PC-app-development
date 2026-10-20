# tk Checkbutton - Tasks Q1

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Hobbies")

sport = tk.IntVar()
music = tk.IntVar()
art = tk.IntVar()

sport_check = tk.Checkbutton(root, text="Sport", variable=sport)
sport_check.pack()
music_check = tk.Checkbutton(root, text="Music", variable=music)
music_check.pack()
art_check = tk.Checkbutton(root, text="Art", variable=art)
art_check.pack()

root.mainloop()
