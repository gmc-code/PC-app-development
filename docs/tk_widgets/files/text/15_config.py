# tk Text - config

import tkinter as tk


def show_table():
    results_box.config(state="normal")          # 1. Unlock
    results_box.delete("1.0", tk.END)
    for number in range(1, 11):
        results_box.insert(tk.END, f"{number} x 5 = {number * 5}\n")    # 2. Insert
    results_box.config(state="disabled")        # 3. Lock again


root = tk.Tk()
root.geometry("300x300")
root.title("config")

table_button = tk.Button(root, text="Show the 5 times table", command=show_table)
table_button.pack(pady=10)

results_box = tk.Text(root, width=20, height=10, state="disabled")
results_box.pack()

root.mainloop()
