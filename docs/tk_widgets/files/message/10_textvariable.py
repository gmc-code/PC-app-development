# tk Message - textvariable

import tkinter as tk


def next_page():
    story.set("The dragon flew over the mountains, looking for somewhere to land.")


root = tk.Tk()
root.geometry("300x200")
root.title("textvariable")

story = tk.StringVar(value="Once upon a time, there was a small green dragon.")

page = tk.Message(root, textvariable=story, width=250, font=("Arial", 12))
page.pack(pady=10)

tk.Button(root, text="Next page", command=next_page).pack()

root.mainloop()
