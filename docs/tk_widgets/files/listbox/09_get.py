# tk Listbox - get

import tkinter as tk


def show_choice():
    chosen = country_list.curselection()        # e.g. (2,)
    if chosen:                                  # Check something is chosen
        country = country_list.get(chosen[0])   # Get the words
        result_label.config(text="You chose " + country)
    else:
        result_label.config(text="Please choose a country")


root = tk.Tk()
root.geometry("300x250")
root.title("curselection and get")

country_list = tk.Listbox(root, height=5)
for country in ["Australia", "Japan", "Kenya", "Brazil", "Canada"]:
    country_list.insert(tk.END, country)
country_list.pack(pady=5)

show_button = tk.Button(root, text="Show choice", command=show_choice)
show_button.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
