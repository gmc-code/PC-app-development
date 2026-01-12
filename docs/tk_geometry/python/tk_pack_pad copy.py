import tkinter as tk

root = tk.Tk()

# --- Block 1 ---
frame1 = tk.Frame(root, bd=1, relief="solid")
frame1.pack(pady=1)

label1 = tk.Label(frame1, text="padx=10, pady=5", bg="red", fg="white")
label1.pack(padx=10, pady=5)

# --- Block 2 ---
frame2 = tk.Frame(root, bd=1, relief="solid")
frame2.pack(pady=1)

label2 = tk.Label(frame2, text="padx=20, pady=10", bg="purple", fg="white")
label2.pack(padx=20, pady=10)

# --- Block 3 ---
frame3 = tk.Frame(root, bd=1, relief="solid")
frame3.pack(pady=1)

label3 = tk.Label(frame3, text="padx=30, pady=20", bg="blue", fg="white")
label3.pack(padx=30, pady=20)

root.mainloop()
