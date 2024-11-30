import tkinter as tk

root = tk.Tk()
root.title('columnconfigure')
root.geometry('300x200')
# frame = tk.Frame(root)

# Configuring the first column
root.columnconfigure(0, weight=1, pad=10)
# Configuring the second column
root.columnconfigure(1, weight=2, pad=10)
# Configuring the third column
root.columnconfigure(2, weight=3, pad=10)

# Adding widgets to the frame
label1 = tk.Label(root, text="Label 1", bg="lightblue")
label2 = tk.Label(root, text="Label 2", bg="lightgreen")
label3 = tk.Label(root, text="Label 3", bg="lightyellow")
label1.grid(row=0, column=0, sticky="news", padx=5, pady=5)
label2.grid(row=0, column=1, sticky="news", padx=5, pady=5)
label3.grid(row=0, column=2, sticky="news", padx=5, pady=5)

# frame.pack()
root.mainloop()
