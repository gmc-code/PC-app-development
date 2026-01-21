import tkinter as tk

root = tk.Tk()
root.title("pack anchor")
root.geometry('250x150')

label1 = tk.Label(root, text="anchor=w", bg="lightblue")
label1.pack(anchor='w')

label2 = tk.Label(root, text="anchor=center", bg="lightgreen")
label2.pack(anchor='center')

label3 = tk.Label(root, text="anchor=e", bg="lightpink")
label3.pack(anchor='e')

root.mainloop()
