# tk Listbox - selectmode

import tkinter as tk

root = tk.Tk()
root.geometry("300x250")
root.title("selectmode")

topping_list = tk.Listbox(root, selectmode="multiple", height=6)
for topping in ["Cheese", "Ham", "Pineapple", "Olives", "Mushrooms"]:
    topping_list.insert(tk.END, topping)
topping_list.pack(pady=10)

root.mainloop()
