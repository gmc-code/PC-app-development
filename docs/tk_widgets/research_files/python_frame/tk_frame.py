import tkinter as tk

root = tk.Tk()
root.title("Frame Widget Example")
root.geometry("300x200")

# Creating a frame with specified options
frame = tk.Frame(
    root,
    bg="#f9f9f9",
    bd=2,
    relief="groove",
    width=200,
    height=150,
    padx=10,
    pady=10,
)

frame.pack(padx=20, pady=20)

root.mainloop()