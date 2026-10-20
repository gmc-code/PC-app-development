# tk OptionMenu - Tasks Q2

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Holidays")

holiday = tk.StringVar(value="Beach")

holiday_menu = tk.OptionMenu(root, holiday, "Beach", "Snow", "City", "Camping")
holiday_menu.config(font=("Arial", 14), width=12, bg="lightblue")
holiday_menu.pack(pady=20)

root.mainloop()
