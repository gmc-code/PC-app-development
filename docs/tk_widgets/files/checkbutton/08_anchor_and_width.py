# tk Checkbutton - anchor and width

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("anchor and width")

ham = tk.IntVar()
pineapple = tk.IntVar()
mushrooms = tk.IntVar()

ham_check = tk.Checkbutton(root, text="Ham", variable=ham, width=15, anchor="w")
ham_check.pack()

pineapple_check = tk.Checkbutton(root, text="Pineapple", variable=pineapple, width=15, anchor="w")
pineapple_check.pack()

mushrooms_check = tk.Checkbutton(root, text="Mushrooms", variable=mushrooms, width=15, anchor="w")
mushrooms_check.pack()

root.mainloop()
