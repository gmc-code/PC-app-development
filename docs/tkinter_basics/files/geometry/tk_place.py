import tkinter as tk

# window
window = tk.Tk()
window.title("place")
window.geometry("200x200")

# widgets
label1 = tk.Label(window, text="Label 1", background="red")
label2 = tk.Label(window, text="Label 2", background="pink")
label3 = tk.Label(window, text="Label 3", background="orange")

# place
label1.place(x=50, y=40)
label2.place(x=50, y=75, width=60, height=80)
label3.place(x=110, y=155, anchor="center")

# Start the main event loop
window.mainloop()
