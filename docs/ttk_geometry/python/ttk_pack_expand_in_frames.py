import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("expand + fill comparison")
root.geometry("350x600")

style = ttk.Style()
style.configure("A.TLabel", background="#ff9999")   # red
style.configure("B.TLabel", background="#99ff99")   # green
style.configure("C.TLabel", background="#9999ff")   # blue
style.configure("D.TLabel", background="#ffff99")   # yellow
style.configure("E.TLabel", background="#ffcc99")   # orange
style.configure("F.TLabel", background="#cc99ff")   # purple

# 1. expand=False, fill='x'
frame1 = ttk.LabelFrame(root, text="expand=False, fill='x'")
frame1.pack(fill='both', expand=True, pady=5)
ttk.Label(frame1, text="Label", style="A.TLabel", anchor="center")\
    .pack(expand=False, fill='x')

# 2. expand=False, fill='y'
frame2 = ttk.LabelFrame(root, text="expand=False, fill='y'")
frame2.pack(fill='both', expand=True, pady=5)
ttk.Label(frame2, text="Label", style="B.TLabel", anchor="center")\
    .pack(expand=False, fill='y')

# 3. expand=False, fill='both'
frame3 = ttk.LabelFrame(root, text="expand=False, fill='both'")
frame3.pack(fill='both', expand=True, pady=5)
ttk.Label(frame3, text="Label", style="C.TLabel", anchor="center")\
    .pack(expand=False, fill='both')

# 4. expand=True, fill='x'
frame4 = ttk.LabelFrame(root, text="expand=True, fill='x'")
frame4.pack(fill='both', expand=True, pady=5)
ttk.Label(frame4, text="Label", style="D.TLabel", anchor="center")\
    .pack(expand=True, fill='x')

# 5. expand=True, fill='y'
frame5 = ttk.LabelFrame(root, text="expand=True, fill='y'")
frame5.pack(fill='both', expand=True, pady=5)
ttk.Label(frame5, text="Label", style="E.TLabel", anchor="center")\
    .pack(expand=True, fill='y')

# 6. expand=True, fill='both'
frame6 = ttk.LabelFrame(root, text="expand=True, fill='both'")
frame6.pack(fill='both', expand=True, pady=5)
ttk.Label(frame6, text="Label", style="F.TLabel", anchor="center")\
    .pack(expand=True, fill='both')

root.mainloop()
