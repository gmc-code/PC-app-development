import tkinter as tk

window = tk.Tk()
window.title("pack anchor")
window.geometry('250x150')

label1 = tk.Label(window, text="Top-Left", bg="lightblue")
label1.pack(anchor='nw')

label2 = tk.Label(window, text="Center", bg="lightgreen")
label2.pack(anchor='center')

label3 = tk.Label(window, text="Bottom-Right", bg="lightpink")
label3.pack(anchor='se')

window.mainloop()

