# tk Label - Tasks Q2

import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
root.title("About me")

name_label = tk.Label(root, text="Sam", font=("Arial", 24), fg="white", bg="blue")
name_label.pack()

food_label = tk.Label(root, text="Pizza", relief="solid", borderwidth=2,
                      padx=10, pady=10)
food_label.pack()

root.mainloop()
