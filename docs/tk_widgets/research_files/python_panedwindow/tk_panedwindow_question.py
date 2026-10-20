import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("PanedWindow Question")
root.geometry("300x310")

# Create the PanedWindow
paned = tk.PanedWindow(
    root,
    orient="vertical",
    sashwidth=5
)

paned.pack(fill="both", expand=True)

# Create three frames
top_frame = tk.Frame(
    paned,
    bg="light blue",
    width=300,
    height=100
)

middle_frame = tk.Frame(
    paned,
    bg="light yellow",
    width=300,
    height=100
)

bottom_frame = tk.Frame(
    paned,
    bg="light green",
    width=300,
    height=100
)

# Add frames to the PanedWindow
paned.add(top_frame, minsize=50)
paned.add(middle_frame, minsize=50)
paned.add(bottom_frame, minsize=50)

# Run the main event loop
root.mainloop()