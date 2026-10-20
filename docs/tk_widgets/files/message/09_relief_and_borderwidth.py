# tk Message - relief and borderwidth

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("relief")

box = tk.Message(root, text="This message has a solid border around it.", width=200,
                 relief="solid", borderwidth=2, padx=10, pady=10)
box.pack(pady=20)

root.mainloop()
