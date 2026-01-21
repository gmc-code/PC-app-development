import tkinter as tk

root = tk.Tk()
root.title("Vertical buttons")
root.geometry("120x240")

# -------------------
# Create buttons
# -------------------
btn1 = tk.Button(root, text="1", width=10, height=2, bg="#ffccbc")
btn2 = tk.Button(root, text="2", width=10, height=2, bg="#bbdefb")
btn3 = tk.Button(root, text="3", width=10, height=2, bg="#c8e6c9")
btn4 = tk.Button(root, text="4", width=10, height=2, bg="#f8bbd0")

# -------------------
# Pack buttons (all at the end)
# -------------------
btn1.pack(side="top")
btn2.pack(side="top")
btn3.pack(side="top")
btn4.pack(side="top")

root.mainloop()
