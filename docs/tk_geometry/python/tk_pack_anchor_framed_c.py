import tkinter as tk

root = tk.Tk()
root.title("pack anchor framed c")
root.geometry("360x240")


# anchor = nw
frame_nw = tk.Frame(root, width=110, height=60, bg="white", highlightbackground="black", highlightthickness=1)
frame_nw.pack(side="left", padx=6, pady=10)
frame_nw.pack_propagate(False)
label_nw = tk.Label(frame_nw, text="anchor=nw", bg="#fff9c4")
label_nw.pack(expand=True, anchor="nw")

# anchor = center
frame_c = tk.Frame(root, width=110, height=60, bg="white", highlightbackground="black", highlightthickness=1)
frame_c.pack(side="left", padx=6, pady=10)
frame_c.pack_propagate(False)
label_c = tk.Label(frame_c, text="anchor=center", bg="#ffccbc")
label_c.pack(expand=True, anchor="center")

# anchor = se
frame_se = tk.Frame(root, width=110, height=60, bg="white", highlightbackground="black", highlightthickness=1)
frame_se.pack(side="left", padx=6, pady=10)
frame_se.pack_propagate(False)
label_se = tk.Label(frame_se, text="anchor=se", bg="#f8bbd0")
label_se.pack(expand=True, anchor="se")


root.mainloop()
