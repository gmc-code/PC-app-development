import tkinter as tk

root = tk.Tk()
root.title('rowconfigure')
root.geometry('300x200')

# Set weights for rows
root.rowconfigure(0, weight=1, pad=10)
root.rowconfigure(1, weight=2, pad=10)
root.rowconfigure(2, weight=3, pad=10)

label1 = tk.Label(root, text="Label 1", width=30, bg="lightblue")
label2 = tk.Label(root, text="Label 2", bg="lightgreen")
label3 = tk.Label(root, text="Label 3", bg="lightyellow")

label1.grid(row=0, column=0, sticky="nsew")
label2.grid(row=1, column=0, sticky="nsew")
label3.grid(row=2, column=0, sticky="nsew")


root.mainloop()
