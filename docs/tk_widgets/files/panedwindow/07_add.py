# tk PanedWindow - add

import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
root.title("add")

panes = tk.PanedWindow(root, sashwidth=5)
panes.pack(fill="both", expand=True)

# Pane 1: a list of topics
topic_list = tk.Listbox(panes)
for topic in ["Planets", "Stars", "Moons"]:
    topic_list.insert(tk.END, topic)
panes.add(topic_list)

# Pane 2: a box for notes
notes_box = tk.Text(panes, wrap="word")
notes_box.insert("1.0", "Type your notes here")
panes.add(notes_box)

root.mainloop()
