# ttk Scrollbar - With a Text widget

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Text")

scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

story_box = tk.Text(root, wrap="word", yscrollcommand=scrollbar.set)
story_box.pack(side="left", fill="both", expand=True)
scrollbar.config(command=story_box.yview)

for number in range(1, 31):
    story_box.insert(tk.END, f"This is line {number} of the story.\n")

root.mainloop()
