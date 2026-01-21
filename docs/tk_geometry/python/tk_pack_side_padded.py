import tkinter as tk

root = tk.Tk()
root.title("padding")
root.geometry("260x300")

# -------------------
# Row 1
# -------------------
row1 = tk.Frame(root)
row1.pack(side="top")

btn1 = tk.Button(row1, text="1", width=10, height=2, bg="#ffccbc")
btn1.pack(side="left")
btn2 = tk.Button(row1, text="2", width=10, height=2, bg="#bbdefb")
btn2.pack(side="left")
# -------------------
# Row 2
# -------------------
row2 = tk.Frame(root)
row2.pack(side="top")

btn3 = tk.Button(row2, text="3", width=10, height=2, bg="#c8e6c9")
btn3.pack(side="left")
btn4 = tk.Button(row2, text="4", width=10, height=2, bg="#f48fb1")
btn4.pack(side="left", ipady=10)

# -------------------
# Row 3
# -------------------
row3 = tk.Frame(root)
row3.pack(side="top")

btn5 = tk.Button(row3, text="5", width=10, height=2, bg="#ffe082")
btn5.pack(side="left")
btn6 = tk.Button(row3, text="6", width=10, height=2, bg="#b39ddb")
btn6.pack(side="left", ipadx=10)

# -------------------
# Row 4
# -------------------
row4 = tk.Frame(root)
row4.pack(side="top")

btn7 = tk.Button(row4, text="7", width=10, height=2, bg="#80cbc4")
btn7.pack(side="left")
btn8 = tk.Button(row4, text="8", width=10, height=2, bg="#f48fb1")
btn8.pack(side="left", padx=10, pady=10)
root.mainloop()
