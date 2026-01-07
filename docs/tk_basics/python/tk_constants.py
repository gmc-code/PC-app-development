import tkinter as tk

root = tk.Tk()
root.title("Tkinter Constants — Visual Grid Demo")
root.geometry("900x720")
root.configure(bg="#f0f0f0")

# Helper to create labeled demo cells
def make_cell(parent, title, widget_fn):
    frame = tk.LabelFrame(parent, text=title, padx=10, pady=10)
    frame.pack_propagate(False)
    frame.configure(width=250, height=150)
    frame.grid_propagate(False)
    widget_fn(frame)
    return frame

# ---------------------------------------------------------
# GRID CONTAINER
# ---------------------------------------------------------
grid = tk.Frame(root, bg="#f0f0f0")
grid.pack(padx=20, pady=20)

# ---------------------------------------------------------
# 1. ANCHOR DEMOS
# ---------------------------------------------------------
def anchor_demo(parent):
    lbl = tk.Label(parent, text="Anchored LEFT", bg="#d0eaff", anchor=tk.W)
    lbl.pack(fill=tk.BOTH, expand=True)

def anchor_center_demo(parent):
    lbl = tk.Label(parent, text="CENTER", bg="#d0eaff", anchor=tk.CENTER)
    lbl.pack(fill=tk.BOTH, expand=True)

# ---------------------------------------------------------
# 2. STICKY DEMOS
# ---------------------------------------------------------
def sticky_demo(parent):
    f = tk.Frame(parent, bg="#d0eaff")
    f.grid(row=0, column=0, sticky=tk.NSEW)
    parent.grid_rowconfigure(0, weight=1)
    parent.grid_columnconfigure(0, weight=1)

# ---------------------------------------------------------
# 3. SIDE DEMOS
# ---------------------------------------------------------
def side_demo(parent):
    tk.Button(parent, text="LEFT").pack(side=tk.LEFT)
    tk.Button(parent, text="RIGHT").pack(side=tk.RIGHT)

# ---------------------------------------------------------
# 4. FILL DEMOS
# ---------------------------------------------------------
def fill_demo(parent):
    tk.Button(parent, text="FILL X").pack(fill=tk.X)
    tk.Button(parent, text="FILL BOTH").pack(fill=tk.BOTH, expand=True)

# ---------------------------------------------------------
# 5. RELIEF DEMOS
# ---------------------------------------------------------
def relief_demo(parent):
    for relief in [tk.RAISED, tk.SUNKEN, tk.GROOVE, tk.RIDGE]:
        tk.Button(parent, text=relief, relief=relief).pack(side=tk.LEFT, padx=3)

# ---------------------------------------------------------
# 6. ORIENT DEMOS
# ---------------------------------------------------------
def orient_demo(parent):
    tk.Scale(parent, from_=0, to=100, orient=tk.HORIZONTAL).pack(fill=tk.X)
    tk.Scale(parent, from_=0, to=100, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y)

# ---------------------------------------------------------
# 7. WRAP DEMOS
# ---------------------------------------------------------
def wrap_demo(parent):
    txt = tk.Text(parent, height=4, wrap=tk.WORD)
    txt.insert(tk.END, "This text wraps by WORD.\nResize me to see wrapping.")
    txt.pack(fill=tk.BOTH, expand=True)

# ---------------------------------------------------------
# 8. STATE DEMOS
# ---------------------------------------------------------
def state_demo(parent):
    e1 = tk.Entry(parent)
    e1.insert(0, "NORMAL")
    e1.pack(fill=tk.X)

    e2 = tk.Entry(parent, state=tk.DISABLED)
    e2.insert(0, "DISABLED")
    e2.pack(fill=tk.X, pady=5)

# ---------------------------------------------------------
# 9. SPECIAL POSITIONS (END, INSERT)
# ---------------------------------------------------------
def special_demo(parent):
    txt = tk.Text(parent, height=4)
    txt.pack(fill=tk.BOTH, expand=True)
    txt.insert(tk.END, "Inserted at END\n")
    txt.insert(tk.INSERT, "Inserted at INSERT\n")

# ---------------------------------------------------------
# PLACE CELLS IN A VISUAL GRID
# ---------------------------------------------------------
cells = [
    ("Anchor (W)", anchor_demo),
    ("Anchor (CENTER)", anchor_center_demo),
    ("Sticky (NSEW)", sticky_demo),
    ("Side (LEFT/RIGHT)", side_demo),
    ("Fill (X/BOTH)", fill_demo),
    ("Relief Styles", relief_demo),
    ("Orient (H/V)", orient_demo),
    ("Wrap (WORD)", wrap_demo),
    ("States (NORMAL/DISABLED)", state_demo),
    ("Special Positions (END/INSERT)", special_demo),
]

# 3 columns
cols = 3
for i, (title, fn) in enumerate(cells):
    r = i // cols
    c = i % cols
    cell = make_cell(grid, title, fn)
    cell.grid(row=r, column=c, padx=10, pady=10)

root.mainloop()
import tkinter as tk

root = tk.Tk()
root.title("Tkinter Constants — Visual Grid Demo")
root.geometry("900x900")
root.configure(bg="#f0f0f0")

# Helper to create labeled demo cells
def make_cell(parent, title, widget_fn):
    frame = tk.LabelFrame(parent, text=title, padx=10, pady=10)
    frame.pack_propagate(False)
    frame.configure(width=250, height=150)
    frame.grid_propagate(False)
    widget_fn(frame)
    return frame

# ---------------------------------------------------------
# GRID CONTAINER
# ---------------------------------------------------------
grid = tk.Frame(root, bg="#f0f0f0")
grid.pack(padx=20, pady=20)

# ---------------------------------------------------------
# 1. ANCHOR DEMOS
# ---------------------------------------------------------
def anchor_demo(parent):
    lbl = tk.Label(parent, text="Anchored LEFT", bg="#d0eaff", anchor=tk.W)
    lbl.pack(fill=tk.BOTH, expand=True)

def anchor_center_demo(parent):
    lbl = tk.Label(parent, text="CENTER", bg="#d0eaff", anchor=tk.CENTER)
    lbl.pack(fill=tk.BOTH, expand=True)

# ---------------------------------------------------------
# 2. STICKY DEMOS
# ---------------------------------------------------------
def sticky_demo(parent):
    f = tk.Frame(parent, bg="#d0eaff")
    f.grid(row=0, column=0, sticky=tk.NSEW)
    parent.grid_rowconfigure(0, weight=1)
    parent.grid_columnconfigure(0, weight=1)

# ---------------------------------------------------------
# 3. SIDE DEMOS
# ---------------------------------------------------------
def side_demo(parent):
    tk.Button(parent, text="LEFT").pack(side=tk.LEFT)
    tk.Button(parent, text="RIGHT").pack(side=tk.RIGHT)

# ---------------------------------------------------------
# 4. FILL DEMOS
# ---------------------------------------------------------
def fill_demo(parent):
    tk.Button(parent, text="FILL X").pack(fill=tk.X)
    tk.Button(parent, text="FILL BOTH").pack(fill=tk.BOTH, expand=True)

# ---------------------------------------------------------
# 5. RELIEF DEMOS
# ---------------------------------------------------------
def relief_demo(parent):
    for relief in [tk.RAISED, tk.SUNKEN, tk.GROOVE, tk.RIDGE]:
        tk.Button(parent, text=relief, relief=relief).pack(side=tk.LEFT, padx=3)

# ---------------------------------------------------------
# 6. ORIENT DEMOS
# ---------------------------------------------------------
def orient_demo(parent):
    tk.Scale(parent, from_=0, to=100, orient=tk.HORIZONTAL).pack(fill=tk.X)
    tk.Scale(parent, from_=0, to=100, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y)

# ---------------------------------------------------------
# 7. WRAP DEMOS
# ---------------------------------------------------------
def wrap_demo(parent):
    txt = tk.Text(parent, height=4, wrap=tk.WORD)
    txt.insert(tk.END, "This text wraps by WORD.\nAcdefg hijklmnop qrstuvwxyz  \nResize me to see wrapping.")
    txt.pack(fill=tk.BOTH, expand=True)

# ---------------------------------------------------------
# 8. STATE DEMOS
# ---------------------------------------------------------
def state_demo(parent):
    e1 = tk.Entry(parent)
    e1.insert(0, "NORMAL")
    e1.pack(fill=tk.X)

    e2 = tk.Entry(parent, state=tk.DISABLED)
    e2.insert(0, "DISABLED")
    e2.pack(fill=tk.X, pady=5)

# ---------------------------------------------------------
# 9. SPECIAL POSITIONS (END, INSERT)
# ---------------------------------------------------------
def special_demo(parent):
    txt = tk.Text(parent, height=4)
    txt.pack(fill=tk.BOTH, expand=True)
    txt.insert(tk.END, "Inserted at END\n")
    txt.insert(tk.INSERT, "Inserted at INSERT\n")

# ---------------------------------------------------------
# PLACE CELLS IN A VISUAL GRID
# ---------------------------------------------------------
cells = [
    ("Anchor (W)", anchor_demo),
    ("Anchor (CENTER)", anchor_center_demo),
    ("Sticky (NSEW)", sticky_demo),
    ("Side (LEFT/RIGHT)", side_demo),
    ("Fill (X/BOTH)", fill_demo),
    ("Relief Styles", relief_demo),
    ("Orient (H/V)", orient_demo),
    ("Wrap (WORD)", wrap_demo),
    ("States (NORMAL/DISABLED)", state_demo),
    ("Special Positions (END/INSERT)", special_demo),
]

# 3 columns
cols = 3
for i, (title, fn) in enumerate(cells):
    r = i // cols
    c = i % cols
    cell = make_cell(grid, title, fn)
    cell.grid(row=r, column=c, padx=10, pady=10)

root.mainloop()
