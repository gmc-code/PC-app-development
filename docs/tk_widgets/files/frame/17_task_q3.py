# tk Frame - Tasks Q3

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Frames")

top_frame = tk.Frame(root, bg="darkblue")
top_frame.pack(fill="x")
tk.Label(top_frame, text="My App", fg="white", bg="darkblue",
         font=("Arial", 16)).pack(pady=5)

main_frame = tk.Frame(root, bg="white")
main_frame.pack(fill="both", expand=True)

root.mainloop()
