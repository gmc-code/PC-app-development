# tk Scrollbar - Tasks Q4

import tkinter as tk

root = tk.Tk()
root.geometry("300x250")
root.title("Fruit")

tk.Label(root, text="Fruit", font=("Arial", 14)).pack()

list_frame = tk.Frame(root)
list_frame.pack(pady=5)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

fruit_list = tk.Listbox(list_frame, height=5, yscrollcommand=scrollbar.set)
fruit_list.pack(side="left")
scrollbar.config(command=fruit_list.yview)

for fruit in ["Apple", "Banana", "Cherry", "Grape", "Kiwi",
              "Lemon", "Mango", "Orange", "Peach", "Pear"]:
    fruit_list.insert(tk.END, fruit)

tk.Button(root, text="Choose").pack()

root.mainloop()
