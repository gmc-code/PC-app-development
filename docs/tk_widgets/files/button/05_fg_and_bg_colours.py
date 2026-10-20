# tk Button - fg and bg (colours)

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("fg and bg")

go_button = tk.Button(root, text="GO", font=("Arial", 16), fg="white", bg="green")
go_button.pack(pady=10)

stop_button = tk.Button(root, text="STOP", font=("Arial", 16), fg="white", bg="red")
stop_button.pack(pady=10)

root.mainloop()
