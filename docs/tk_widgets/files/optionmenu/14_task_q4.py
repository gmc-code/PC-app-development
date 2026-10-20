# tk OptionMenu - Tasks Q4

import tkinter as tk


def show():
    result_label.config(text="Welcome to " + year.get())


root = tk.Tk()
root.geometry("300x200")
root.title("Year level")

year = tk.StringVar(value="Year 7")

year_menu = tk.OptionMenu(root, year, "Year 7", "Year 8", "Year 9")
year_menu.pack(pady=10)

show_button = tk.Button(root, text="Show", command=show)
show_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
