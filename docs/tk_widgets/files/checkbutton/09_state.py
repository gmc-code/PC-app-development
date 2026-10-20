# tk Checkbutton - state

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("state")

free = tk.IntVar()
sold_out = tk.IntVar()

free_check = tk.Checkbutton(root, text="Chips", variable=free)
free_check.pack(pady=5)

sold_out_check = tk.Checkbutton(root, text="Ice cream (sold out)", variable=sold_out,
                                state="disabled")
sold_out_check.pack(pady=5)

root.mainloop()
