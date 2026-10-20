# tk OptionMenu - Tasks Q1

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Holidays")

holiday = tk.StringVar(value="Beach")

holiday_menu = tk.OptionMenu(root, holiday, "Beach", "Snow", "City", "Camping")
holiday_menu.pack(pady=20)

root.mainloop()
