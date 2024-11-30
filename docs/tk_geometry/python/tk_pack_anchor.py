import tkinter as tk

root = tk.Tk()
root.title("pack anchor")
root.geometry('250x150')

label1 = tk.Label(root, text="Top-Left", bg="lightblue")
label1.pack(anchor='nw')

label2 = tk.Label(root, text="Center", bg="lightgreen")
label2.pack(anchor='center')

label3 = tk.Label(root, text="Bottom-Right", bg="lightpink")
label3.pack(anchor='se')

root.mainloop()

