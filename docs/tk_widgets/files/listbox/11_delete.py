# tk Listbox - delete

import tkinter as tk


def delete_chosen():
    chosen = job_list.curselection()
    if chosen:
        job_list.delete(chosen[0])


def clear_all():
    job_list.delete(0, tk.END)


root = tk.Tk()
root.geometry("300x280")
root.title("delete")

job_list = tk.Listbox(root, height=5)
for job in ["Feed the dog", "Do homework", "Tidy room", "Practise piano"]:
    job_list.insert(tk.END, job)
job_list.pack(pady=5)

done_button = tk.Button(root, text="Done (delete chosen)", command=delete_chosen)
done_button.pack(pady=2)

clear_button = tk.Button(root, text="Clear all", command=clear_all)
clear_button.pack(pady=2)

root.mainloop()
