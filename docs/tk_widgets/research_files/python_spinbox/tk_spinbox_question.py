import tkinter as tk

root = tk.Tk()
root.title("Scrollbar Question")

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="left", fill="y")

text = tk.Text(
    root,
    width=30,
    height=10,
    yscrollcommand=scrollbar.set
)
text.pack(side="left")

scrollbar.config(command=text.yview)

for i in range(1, 16):
    text.insert("end", f"Line {i}\n")

root.mainloop()

