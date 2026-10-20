# tk Text - Tasks Q3

import tkinter as tk


def count_letters():
    writing = diary_box.get("1.0", "end-1c")
    count_label.config(text=f"Characters: {len(writing)}")


root = tk.Tk()
root.geometry("400x300")
root.title("Diary")

diary_box = tk.Text(root, width=40, height=10, wrap="word",
                    bg="lightyellow", font=("Arial", 12))
diary_box.pack(pady=10)

count_button = tk.Button(root, text="Count letters", command=count_letters)
count_button.pack()

count_label = tk.Label(root, text="Characters: 0")
count_label.pack()

root.mainloop()
