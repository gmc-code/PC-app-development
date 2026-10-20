# tk Text - Tasks Q2

import tkinter as tk


def clear():
    diary_box.delete("1.0", tk.END)


root = tk.Tk()
root.geometry("400x300")
root.title("Diary")

diary_box = tk.Text(root, width=40, height=10, wrap="word",
                    bg="lightyellow", font=("Arial", 12))
diary_box.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack()

root.mainloop()
