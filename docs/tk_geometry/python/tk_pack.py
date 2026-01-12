import tkinter as tk

root = tk.Tk()
root.title("pack all options")
root.geometry("300x200")

label = tk.Label(root, text="All pack options", bg="lightblue")
label.pack(side="left", fill="y", ipadx=15, ipady=5)

# label2 = tk.Label(root, text="All pack options", bg="lightblue")
# label2.pack(side="right", ipadx=15, ipady=5)

root.mainloop()