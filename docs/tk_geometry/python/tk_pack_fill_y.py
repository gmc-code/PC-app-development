import tkinter as tk

window = tk.Tk()
window.title("pack fill y")
window.geometry("250x150")

label = tk.Label(window, text="Expanding Label", bg="lightblue")
label.pack(expand=True, fill='y')

window.mainloop()