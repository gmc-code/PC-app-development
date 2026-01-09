import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("expand / fill demo (refactored + reordered)")
root.geometry("350x600")

style = ttk.Style()
style.configure("A.TLabel", background="#ff9999")   # red-ish
style.configure("B.TLabel", background="#99ff99")   # green-ish
style.configure("C.TLabel", background="#9999ff")   # blue-ish
style.configure("D.TLabel", background="#ffff99")   # yellow-ish
style.configure("E.TLabel", background="#ffcc99")   # orange-ish
style.configure("F.TLabel", background="#cc99ff")   # purple-ish
style.configure("G.TLabel", background="#99ffff")   # cyan-ish
style.configure("H.TLabel", background="#ff99ff")   # pink-ish

# -------------------------------
# Frame 1: expand = False widgets
# -------------------------------
frame_false = ttk.Frame(root)
frame_false.pack(fill='both', expand=False, pady=10)

ttk.Label(frame_false, text="expand=False examples", anchor="center").pack()

# 1. expand=False, fill='both'
ttk.Label(frame_false, text="1: expand=False, fill='both'", style="G.TLabel", anchor="center")\
    .pack(fill='both')

# 2. expand=False, fill='x'
ttk.Label(frame_false, text="2: expand=False, fill='x'", style="E.TLabel", anchor="center")\
    .pack(fill='x')

# 3. expand=False, fill='y'
ttk.Label(frame_false, text="3: expand=False, fill='y'", style="F.TLabel", anchor="center")\
    .pack(fill='y')

# 4. expand=False, fill=None
ttk.Label(frame_false, text="4: expand=False, fill=None", style="A.TLabel", anchor="center")\
    .pack()


# -------------------------------
# Frame 2: expand = True widgets
# -------------------------------
frame_true = ttk.Frame(root)
frame_true.pack(fill='both', expand=True, pady=10)

ttk.Label(frame_true, text="expand=True examples", anchor="center").pack()

# 5. expand=True, fill='both'
ttk.Label(frame_true, text="5: expand=True, fill='both'", style="H.TLabel", anchor="center")\
    .pack(expand=True, fill='both')

# 6. expand=True, fill='x'
ttk.Label(frame_true, text="6: expand=True, fill='x'", style="C.TLabel", anchor="center")\
    .pack(expand=True, fill='x')

# 7. expand=True, fill='y'
ttk.Label(frame_true, text="7: expand=True, fill='y'", style="D.TLabel", anchor="center")\
    .pack(expand=True, fill='y')

# 8. expand=True, fill=None
ttk.Label(frame_true, text="8: expand=True, fill=None", style="B.TLabel", anchor="center")\
    .pack(expand=True)

root.mainloop()
