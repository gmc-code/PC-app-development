import tkinter as tk

root = tk.Tk()
root.title("LabelFrame labelanchor Examples")

positions = [
    "nw", "n", "ne",
    "w",  None, "e",
    "sw", "s", "se"
]

cell_width = 180
cell_height = 120

for i in range(3):
    root.grid_columnconfigure(i, minsize=cell_width)
    root.grid_rowconfigure(i, minsize=cell_height)

for index, position in enumerate(positions):
    row = index // 3
    column = index % 3

    if position is None:
        frame = tk.LabelFrame(
            root,
            width=cell_width,
            height=cell_height,
            bd=2,
            relief="groove"
        )
    else:
        frame = tk.LabelFrame(
            root,
            text=f"anchor='{position}'",
            labelanchor=position,
            width=cell_width,
            height=cell_height,
            bd=2,
            relief="groove"
        )

    frame.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )

    # Prevent the LabelFrame from shrinking to fit its contents
    frame.grid_propagate(False)

    label = tk.Label(frame, text="Content")
    label.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()