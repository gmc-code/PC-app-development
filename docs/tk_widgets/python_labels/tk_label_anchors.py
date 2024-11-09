import tkinter as tk

root = tk.Tk()
root.geometry("500x150")
root.title("Label Anchors in a 3x3 Grid")

# List of anchor values
anchors = ["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]


# Create a 3x3 grid of labels with different anchor values
for i, anchor in enumerate(anchors):
    row = i // 3
    col = i % 3
    label = tk.Label(root, text=f"Anchor: {anchor}", anchor=anchor, width=20, height=2, bg="LightGray", fg="blue", relief=tk.RIDGE, bd=2)
    label.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
