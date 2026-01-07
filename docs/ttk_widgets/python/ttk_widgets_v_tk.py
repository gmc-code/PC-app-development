import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tk vs TTK — Shared Widgets Comparison")
# root.geometry("950x900")

# ---------------------------------------------------------
# LOCK TK WIDGET COLORS
# ---------------------------------------------------------
root.option_clear()
root.option_add("*Background", "#ECECEC")
root.option_add("*Label.Background", "#ECECEC")
root.option_add("*Button.Background", "#ECECEC")
root.option_add("*Entry.Background", "white")
root.option_add("*Frame.Background", "#ECECEC")
root.option_add("*Labelframe.Background", "#ECECEC")

# ---------------------------------------------------------
# THEME SELECTOR
# ---------------------------------------------------------
style = ttk.Style()

def change_theme(event=None):
    style.theme_use(theme_box.get())

selector = ttk.Frame(root, padding=10)
selector.pack(fill="x")

ttk.Label(selector, text="Select Theme:", padding=5).pack(side="left")

theme_box = ttk.Combobox(selector, values=style.theme_names(), state="readonly")
theme_box.pack(side="left", padx=5)
theme_box.set(style.theme_use())
theme_box.bind("<<ComboboxSelected>>", change_theme)


# ---------------------------------------------------------
# MAIN CONTAINER
# ---------------------------------------------------------
container = ttk.Frame(root, padding=10)
container.pack(fill="both", expand=True)

tk_frame = tk.LabelFrame(container, text="tk Widgets (Not Themed)", padx=10, pady=10, bg="#ECECEC")
ttk_frame = ttk.LabelFrame(container, text="ttk Widgets (Themed)", padding=10)

tk_frame.grid(row=0, column=0, sticky="n", padx=(0,40))
ttk_frame.grid(row=0, column=1, sticky="n")

# ---------------------------------------------------------
# WIDGET LIST
# ---------------------------------------------------------
common_widgets = [
    "Button", "Label", "Entry", "Checkbutton", "Radiobutton",
    "Scale", "Scrollbar", "Spinbox", "Frame", "Labelframe",
    "Menubutton", "Panedwindow"
]

# ---------------------------------------------------------
# PERFECT ALIGNMENT USING FIXED ROW HEIGHTS
# ---------------------------------------------------------
ROW_HEIGHT = 50

for row_index, name in enumerate(common_widgets):

    tk_frame.grid_rowconfigure(row_index, minsize=ROW_HEIGHT)
    ttk_frame.grid_rowconfigure(row_index, minsize=ROW_HEIGHT)

    # ---------------- TK SIDE ----------------
    tk_label = tk.Label(tk_frame, text=name + ":", bg="#ECECEC", anchor="e", width=14)
    tk_label.grid(row=row_index, column=0, sticky="ne", padx=5)

    tk_cell = tk.Frame(tk_frame, bg="#ECECEC", width=240, height=ROW_HEIGHT)
    tk_cell.grid(row=row_index, column=1, sticky="n")
    tk_cell.grid_propagate(False)

    if name == "Frame":
        w = tk.Frame(tk_cell, width=150, height=40, bg="lightgray")
        w.pack(expand=True)

    elif name == "Labelframe":
        w = tk.LabelFrame(tk_cell, text="tk.LabelFrame", width=150, height=40, bg="#ECECEC")
        w.pack(expand=True)

    elif name == "Scrollbar":
        w = tk.Scrollbar(tk_cell, orient="vertical")
        w.pack(expand=True)

    elif name == "Scale":
        w = tk.Scale(tk_cell, orient="horizontal")
        w.pack(expand=True)

    elif name == "Spinbox":
        w = tk.Spinbox(tk_cell, from_=0, to=10)
        w.pack(expand=True)

    elif name == "Menubutton":
        w = tk.Menubutton(tk_cell, text="tk.Menubutton", relief="raised")
        menu = tk.Menu(w, tearoff=0)
        menu.add_command(label="Option 1")
        menu.add_command(label="Option 2")
        w.config(menu=menu)
        w.pack(expand=True)

    elif name == "Panedwindow":
        w = tk.PanedWindow(tk_cell, orient="horizontal", bg="#ECECEC")
        left = tk.Frame(w, width=60, height=40, bg="lightgray")
        right = tk.Frame(w, width=60, height=40, bg="lightgray")
        w.add(left)
        w.add(right)
        w.pack(expand=True)

    else:
        w = getattr(tk, name)(tk_cell, text=f"tk.{name}") if name != "Entry" else getattr(tk, name)(tk_cell)
        w.pack(expand=True)

    # ---------------- TTK SIDE ----------------
    ttk.Label(ttk_frame, text=name + ":", width=14, anchor="e").grid(
        row=row_index, column=0, sticky="ne", padx=5
    )

    ttk_cell = ttk.Frame(ttk_frame, width=240, height=ROW_HEIGHT)
    ttk_cell.grid(row=row_index, column=1, sticky="n")
    ttk_cell.grid_propagate(False)

    if name == "Frame":
        w = ttk.Frame(ttk_cell, width=150, height=40, style="Visible.TFrame")
        w.pack(expand=True)
        ttk.Label(w, text="Frame", background="#bcdcff").pack(expand=True)

    elif name == "Labelframe":
        w = ttk.Labelframe(ttk_cell, text="ttk.LabelFrame", width=150, height=40, style="Visible.TFrame")
        w.pack(expand=True)
        ttk.Label(w, text="Inside", background="#bcdcff").pack(expand=True)

    elif name == "Scrollbar":
        w = ttk.Scrollbar(ttk_cell, orient="vertical")
        w.pack(expand=True)

    elif name == "Scale":
        w = ttk.Scale(ttk_cell, orient="horizontal")
        w.pack(expand=True)

    elif name == "Spinbox":
        w = ttk.Spinbox(ttk_cell, from_=0, to=10)
        w.pack(expand=True)

    elif name == "Menubutton":
        w = ttk.Menubutton(ttk_cell, text="ttk.Menubutton")
        menu = tk.Menu(w, tearoff=0)
        menu.add_command(label="Option 1")
        menu.add_command(label="Option 2")
        w["menu"] = menu
        w.pack(expand=True)

    elif name == "Panedwindow":
        outer = ttk.Frame(ttk_cell, style="Visible.TFrame")
        outer.pack(expand=True)

        w = ttk.Panedwindow(outer, orient="horizontal")
        w.pack(expand=True)

        left = ttk.Frame(w, width=60, height=40, style="Visible.TFrame")
        right = ttk.Frame(w, width=60, height=40, style="Visible.TFrame")

        w.add(left)
        w.add(right)

        ttk.Label(left, text="Pane 1", background="#bcdcff").pack(expand=True)
        ttk.Label(right, text="Pane 2", background="#bcdcff").pack(expand=True)

    else:
        w = getattr(ttk, name)(ttk_cell, text=f"ttk.{name}") if name != "Entry" else getattr(ttk, name)(ttk_cell)
        w.pack(expand=True)

root.mainloop()
