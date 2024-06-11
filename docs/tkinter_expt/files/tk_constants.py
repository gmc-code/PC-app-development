import tkinter as tk

root = tk.Tk()

text_widget = tk.Text(root, width=40, height=10, wrap=tk.WORD)

text_widget.insert(tk.END, "This is some justified text.")
text_widget.tag_configure("justify_left", justify='left')
text_widget.tag_add("justify_left", "1.0", "end")
text_widget.pack()

root.mainloop()
