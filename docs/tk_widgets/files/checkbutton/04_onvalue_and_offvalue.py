# tk Checkbutton - onvalue and offvalue

import tkinter as tk


def show():
    result_label.config(text="Sauce: " + sauce.get())


root = tk.Tk()
root.geometry("300x200")
root.title("onvalue and offvalue")

sauce = tk.StringVar(value="No")

sauce_check = tk.Checkbutton(root, text="Tomato sauce", variable=sauce,
                             onvalue="Yes", offvalue="No", command=show)
sauce_check.pack(pady=20)

result_label = tk.Label(root, text="Sauce: No")
result_label.pack()

root.mainloop()
