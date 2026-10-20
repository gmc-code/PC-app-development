# tk Text - tag_configure (coloured text)

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("tags")

text_box = tk.Text(root, width=30, height=6, font=("Arial", 12))
text_box.pack(pady=10)

# Make the styles
text_box.tag_configure("title", font=("Arial", 14, "bold"))
text_box.tag_configure("right", foreground="green")
text_box.tag_configure("wrong", foreground="red")

# Use the styles
text_box.insert(tk.END, "Quiz results\n", "title")
text_box.insert(tk.END, "Question 1: correct\n", "right")
text_box.insert(tk.END, "Question 2: wrong\n", "wrong")

root.mainloop()
