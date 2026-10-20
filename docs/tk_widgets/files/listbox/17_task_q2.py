# tk Listbox - Tasks Q2

import tkinter as tk


def choose():
    chosen = sport_list.curselection()
    if chosen:
        result_label.config(text="You chose " + sport_list.get(chosen[0]))


root = tk.Tk()
root.geometry("300x250")
root.title("Sports")

sport_list = tk.Listbox(root, height=5, font=("Arial", 14))
for sport in ["Cricket", "Football", "Netball", "Swimming", "Tennis"]:
    sport_list.insert(tk.END, sport)
sport_list.pack(pady=5)

choose_button = tk.Button(root, text="Choose", command=choose)
choose_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
