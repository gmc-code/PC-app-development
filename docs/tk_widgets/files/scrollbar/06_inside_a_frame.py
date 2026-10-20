# tk Scrollbar - Inside a Frame

import tkinter as tk

root = tk.Tk()
root.geometry("300x250")
root.title("In a frame")

tk.Label(root, text="Countries", font=("Arial", 14)).pack()

list_frame = tk.Frame(root)
list_frame.pack(pady=5)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

country_list = tk.Listbox(list_frame, height=6, yscrollcommand=scrollbar.set)
country_list.pack(side="left")
scrollbar.config(command=country_list.yview)

for country in ["Australia", "Brazil", "Canada", "Denmark", "Egypt", "France",
                "Germany", "India", "Japan", "Kenya", "Mexico", "Norway"]:
    country_list.insert(tk.END, country)

tk.Button(root, text="Choose").pack()

root.mainloop()
