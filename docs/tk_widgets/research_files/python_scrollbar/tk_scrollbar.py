import tkinter as tk

root = tk.Tk()
root.title("Scrollbar Example")

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

text = tk.Text(root, width=40, height=10,
                yscrollcommand=scrollbar.set)
text.pack(side="left", fill="both", expand=True)

scrollbar.config(command=text.yview)

for i in range(1, 21):
    text.insert("end", f"Line {i}\n")

root.mainloop()