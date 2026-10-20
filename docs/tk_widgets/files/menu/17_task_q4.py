# tk Menu - Tasks Q4

import tkinter as tk


def show_popup(event):
    mood_menu.tk_popup(event.x_root, event.y_root)


root = tk.Tk()
root.geometry("300x200")
root.title("Moods")

face_label = tk.Label(root, text="Right-click me", font=("Arial", 30))
face_label.pack(pady=50)

mood_menu = tk.Menu(root, tearoff=0)
mood_menu.add_command(label="Happy", command=lambda: face_label.config(text=":)"))
mood_menu.add_command(label="Sad", command=lambda: face_label.config(text=":("))

root.bind("<Button-3>", show_popup)

root.mainloop()
