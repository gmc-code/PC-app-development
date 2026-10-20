# tk Button - Tasks Q2

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Buttons")

button = tk.Button(root, text="Press me", font=("Arial", 16),
                   fg="white", bg="purple", width=15,
                   activebackground="black", activeforeground="white",
                   cursor="hand2")
button.pack(pady=20)

root.mainloop()
