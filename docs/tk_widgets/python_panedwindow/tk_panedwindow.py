import tkinter as tk

root = tk.Tk()
root.title("PanedWindow Example")
root.geometry("500x300")

# Create the PanedWindow
paned = tk.PanedWindow(
    root,
    orient="horizontal",
    sashwidth=5,
    bg="lightgray"
)

paned.pack(fill="both", expand=True)

# Create child frames
left_frame = tk.Frame(
    paned,
    bg="lightblue",
    width=200,
    height=200
)

right_frame = tk.Frame(
    paned,
    bg="lightgreen",
    width=200,
    height=200
)

# Add frames to the PanedWindow
paned.add(left_frame)
paned.add(right_frame)

root.mainloop()
