import tkinter as tk

window = tk.Tk()
window.title("pack fill x")
window.geometry("250x150")

label = tk.Label(window, text="Expanding Label", bg="lightblue")
label.pack(expand=True, fill='x')

window.mainloop()