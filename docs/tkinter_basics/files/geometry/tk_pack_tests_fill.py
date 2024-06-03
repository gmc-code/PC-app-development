import tkinter as tk

window = tk.Tk()
window.geometry('200x150')

label = tk.Label(window, text="Expanding Label", bg="lightblue")
# label.pack(expand=True)
label.pack(expand=True, fill='y')
# label.pack(expand=True, fill='x')
# label.pack(expand=True, fill='both')

window.mainloop()