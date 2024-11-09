import tkinter as tk

BGCOL = "LightGray"
FGCOL = "black"

root = tk.Tk()
root.geometry("600x400")
root.title("Relief options with different border widths")

# Function to create a row of labels with different border widths
def create_label_row(text, relief):
    frame = tk.Frame(root)
    frame.pack(pady=5)

    label_bd1 = tk.Label(frame, text=f"{text} bd=1", relief=relief, padx=5, pady=5, fg=FGCOL, bg=BGCOL, bd=1)
    label_bd3 = tk.Label(frame, text=f"{text} bd=3", relief=relief, padx=5, pady=5, fg=FGCOL, bg=BGCOL, bd=3)
    label_bd5 = tk.Label(frame, text=f"{text} bd=5", relief=relief, padx=5, pady=5, fg=FGCOL, bg=BGCOL, bd=5)
    label_bd12 = tk.Label(frame, text=f"{text} bd=12", relief=relief, padx=5, pady=5, fg=FGCOL, bg=BGCOL, bd=12)

    label_bd1.pack(side=tk.LEFT, padx=5)
    label_bd3.pack(side=tk.LEFT, padx=5)
    label_bd5.pack(side=tk.LEFT, padx=5)
    label_bd12.pack(side=tk.LEFT, padx=5)

# Create rows for each relief type
create_label_row("FLAT", tk.FLAT)
create_label_row("RAISED", tk.RAISED)
create_label_row("SUNKEN", tk.SUNKEN)
create_label_row("GROOVE", tk.GROOVE)
create_label_row("RIDGE", tk.RIDGE)

root.mainloop()
