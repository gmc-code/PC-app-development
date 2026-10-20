# tk Checkbutton - Tasks Q3

import tkinter as tk


def how_many():
    total = sport.get() + music.get() + art.get()
    count_label.config(text=f"Hobbies ticked: {total}")


root = tk.Tk()
root.geometry("300x200")
root.title("Hobbies")

sport = tk.IntVar()
music = tk.IntVar()
art = tk.IntVar()
music.set(1)

sport_check = tk.Checkbutton(root, text="Sport", variable=sport)
sport_check.pack()
music_check = tk.Checkbutton(root, text="Music", variable=music)
music_check.pack()
art_check = tk.Checkbutton(root, text="Art", variable=art)
art_check.pack()

count_button = tk.Button(root, text="How many?", command=how_many)
count_button.pack(pady=5)

count_label = tk.Label(root, text="")
count_label.pack()

root.mainloop()
