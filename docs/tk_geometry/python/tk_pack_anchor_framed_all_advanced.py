import tkinter as tk

root = tk.Tk()
root.title("pack anchor framed all")
root.geometry("360x240")

anchors = [
    "nw", "n", "ne",
    "w", "center", "e",
    "sw", "s", "se",
]

colors = [
    "#fff9c4", "#e1f5fe", "#fce4ec",
    "#e8f5e9", "#ffccbc", "#ede7f6",
    "#bbdefb", "#dcedc8", "#f8bbd0",
]

# Create 3 horizontal container frames for the rows
row_frames = []
for _ in range(3):
    row_frame = tk.Frame(root)
    row_frame.pack(side="top", pady=4)
    row_frames.append(row_frame)

# Pack each small frame inside the appropriate row frame
for index, (anchor, color) in enumerate(zip(anchors, colors)):
    row = index // 3
    frame = tk.Frame(
        row_frames[row],
        width=110,
        height=60,
        bg="white",
        highlightbackground="black",
        highlightthickness=1,
    )
    frame.pack(side="left", padx=4)
    frame.pack_propagate(False)

    label = tk.Label(frame, text=f"anchor={anchor}", bg=color)
    label.pack(expand=True, anchor=anchor)

root.mainloop()
