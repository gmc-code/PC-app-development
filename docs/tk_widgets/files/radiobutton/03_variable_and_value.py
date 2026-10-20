# tk Radiobutton - variable and value

import tkinter as tk


def show():
    result_label.config(text="You chose " + year.get())


root = tk.Tk()
root.geometry("300x220")
root.title("variable and value")

year = tk.StringVar(value="Year 7")

tk.Radiobutton(root, text="Year 7", variable=year, value="Year 7").pack()
tk.Radiobutton(root, text="Year 8", variable=year, value="Year 8").pack()
tk.Radiobutton(root, text="Year 9", variable=year, value="Year 9").pack()

show_button = tk.Button(root, text="Show", command=show)
show_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
