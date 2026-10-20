# tk Listbox - Tasks Q1

import tkinter as tk

root = tk.Tk()
root.geometry("300x250")
root.title("Sports")

sport_list = tk.Listbox(root, height=5, font=("Arial", 14))
for sport in ["Cricket", "Football", "Netball", "Swimming", "Tennis"]:
    sport_list.insert(tk.END, sport)
sport_list.pack(pady=5)

root.mainloop()
