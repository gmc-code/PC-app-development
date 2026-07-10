import tkinter as tk

root = tk.Tk()
root.title("LabelFrame Widget Example")
root.geometry("320x220")

settings = tk.LabelFrame(
    root,
    text="User Settings",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=10,
    bd=2,
    relief="groove"
)

settings.pack(padx=20, pady=20, fill="both", expand=True)

tk.Label(settings, text="Username").pack(anchor="w")
tk.Entry(settings, width=25).pack(pady=(0, 10))

tk.Checkbutton(settings, text="Remember me").pack(anchor="w")

root.mainloop()