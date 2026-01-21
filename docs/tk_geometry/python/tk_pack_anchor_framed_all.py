import tkinter as tk

root = tk.Tk()
root.title("pack anchor expand - 3x3 layout")
root.geometry("360x240")

# -------------------
# Row 1
# -------------------

row1 = tk.Frame(root)
row1.pack(side="top")
# anchor = nw
frame_nw = tk.Frame(row1, width=110, height=60, bg="white", highlightbackground="black", highlightthickness=1)
frame_nw.pack(side="left", padx=4, pady=4)
frame_nw.pack_propagate(False)
label_nw = tk.Label(frame_nw, text="anchor=nw", bg="#fff9c4")
label_nw.pack(expand=True, anchor="nw")

# anchor = n
frame_n = tk.Frame(row1, width=110, height=60, bg="white", highlightbackground="black", highlightthickness=1)
frame_n.pack(side="left", padx=4, pady=4)
frame_n.pack_propagate(False)
label_n = tk.Label(frame_n, text="anchor=n", bg="#e1f5fe")
label_n.pack(expand=True, anchor="n")

# anchor = ne
frame_ne = tk.Frame(row1, width=110, height=60, bg="white", highlightbackground="black", highlightthickness=1)
frame_ne.pack(side="left", padx=4, pady=4)
frame_ne.pack_propagate(False)
label_ne = tk.Label(frame_ne, text="anchor=ne", bg="#fce4ec")
label_ne.pack(expand=True, anchor="ne")

# -------------------
# Row 2
# -------------------

row2 = tk.Frame(root)
row2.pack(side="top")
# anchor = w
frame_w = tk.Frame(row2, width=110, height=60, bg="white", highlightbackground="black", highlightthickness=1)
frame_w.pack(side="left", padx=4, pady=4)
frame_w.pack_propagate(False)
label_w = tk.Label(frame_w, text="anchor=w", bg="#e8f5e9")
label_w.pack(expand=True, anchor="w")

# anchor = center
frame_c = tk.Frame(row2, width=110, height=60, bg="white", highlightbackground="black", highlightthickness=1)
frame_c.pack(side="left", padx=4, pady=4)
frame_c.pack_propagate(False)
label_c = tk.Label(frame_c, text="anchor=center", bg="#ffccbc")
label_c.pack(expand=True, anchor="center")

# anchor = e
frame_e = tk.Frame(row2, width=110, height=60, bg="white", highlightbackground="black", highlightthickness=1)
frame_e.pack(side="left", padx=4, pady=4)
frame_e.pack_propagate(False)
label_e = tk.Label(frame_e, text="anchor=e", bg="#ede7f6")
label_e.pack(expand=True, anchor="e")

# -------------------
# Row 3
# -------------------

row3 = tk.Frame(root)
row3.pack(side="top")
# anchor = sw
frame_sw = tk.Frame(row3, width=110, height=60, bg="white", highlightbackground="black", highlightthickness=1)
frame_sw.pack(side="left", padx=4, pady=4)
frame_sw.pack_propagate(False)
label_sw = tk.Label(frame_sw, text="anchor=sw", bg="#bbdefb")
label_sw.pack(expand=True, anchor="sw")

# anchor = s
frame_s = tk.Frame(row3, width=110, height=60, bg="white", highlightbackground="black", highlightthickness=1)
frame_s.pack(side="left", padx=4, pady=4)
frame_s.pack_propagate(False)
label_s = tk.Label(frame_s, text="anchor=s", bg="#dcedc8")
label_s.pack(expand=True, anchor="s")

# anchor = se
frame_se = tk.Frame(row3, width=110, height=60, bg="white", highlightbackground="black", highlightthickness=1)
frame_se.pack(side="left", padx=4, pady=4)
frame_se.pack_propagate(False)
label_se = tk.Label(frame_se, text="anchor=se", bg="#f8bbd0")
label_se.pack(expand=True, anchor="se")

root.mainloop()
