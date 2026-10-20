# tk Frame - fill and expand

import tkinter as tk

root = tk.Tk()
root.geometry("300x250")
root.title("fill and expand")

header = tk.Frame(root, bg="navy", height=40)
header.pack(fill="x")                       # Full width

main = tk.Frame(root, bg="white")
main.pack(fill="both", expand=True)         # Use all the space left

footer = tk.Frame(root, bg="gray", height=30)
footer.pack(fill="x")                       # Full width

root.mainloop()
