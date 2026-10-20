import tkinter as tk

root = tk.Tk()
root.geometry("300x250")
root.title("image")

picture = tk.PhotoImage(file="logo.png")    # Load the picture

label = tk.Label(root, image=picture, text="Our logo", compound="top")
label.pack(pady=20)

root.mainloop()