# tk Button - Tasks Q3

import tkinter as tk


def pressed():
    message_label.config(text="You pressed the button!")


root = tk.Tk()
root.geometry("300x200")
root.title("Buttons")

button = tk.Button(root, text="Press me", font=("Arial", 16),
                   fg="white", bg="purple", width=15,
                   activebackground="black", activeforeground="white",
                   cursor="hand2", command=pressed)
button.pack(pady=20)

message_label = tk.Label(root, text="", font=("Arial", 14))
message_label.pack()

root.mainloop()
