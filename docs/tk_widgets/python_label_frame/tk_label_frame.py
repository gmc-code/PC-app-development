import tkinter as tk

root = tk.Tk()
root.title("LabelFrame Widget Example")
root.geometry("320x220")

settings = tk.LabelFrame(
    root,
    text="User Settings",
    font=("Arial", 10),
    padx=10,
    pady=10,
    bd=2,
    relief="groove"
)

settings.pack(padx=20, pady=20, fill="both", expand=True)

root.mainloop()