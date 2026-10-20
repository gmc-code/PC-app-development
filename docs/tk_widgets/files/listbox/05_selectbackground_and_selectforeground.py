# tk Listbox - selectbackground and selectforeground

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("select colours")

team_list = tk.Listbox(root, selectbackground="orange", selectforeground="black", height=4)
for team in ["Red team", "Blue team", "Green team"]:
    team_list.insert(tk.END, team)
team_list.pack(pady=10)

root.mainloop()
