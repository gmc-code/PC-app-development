# tk Checkbutton - font, fg and bg

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("font, fg and bg")

music = tk.IntVar()

music_check = tk.Checkbutton(root, text="Play music", variable=music,
                             font=("Arial", 16), fg="blue", bg="lightyellow")
music_check.pack(pady=20)

root.mainloop()
