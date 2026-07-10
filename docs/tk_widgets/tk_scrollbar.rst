====================================================
tk Scrollbar
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Scrollbar>`_
| See: `<https://www.geeksforgeeks.org/python-tkinter-scrollbar/>`_




e.g
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

text = tk.Text(root, yscrollcommand=scrollbar.set)

scrollbar.config(command=text.yview)