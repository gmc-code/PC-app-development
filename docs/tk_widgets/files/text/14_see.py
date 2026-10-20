# tk Text - see

import tkinter as tk


def add_line():
    text_box.insert(tk.END, "New line\n")
    text_box.see(tk.END)        # Scroll down to show the new line


root = tk.Tk()
root.geometry("300x200")
root.title("see")

text_box = tk.Text(root, width=30, height=4)
text_box.pack(pady=10)

add_button = tk.Button(root, text="Add a line (click lots!)", command=add_line)
add_button.pack()

root.mainloop()
