# tk Frame - A full layout example

import tkinter as tk

root = tk.Tk()
root.geometry("400x250")
root.title("Layout")

# Title bar along the top
title_frame = tk.Frame(root, bg="darkgreen")
title_frame.pack(fill="x")
tk.Label(title_frame, text="Science Quiz", fg="white", bg="darkgreen",
         font=("Arial", 18)).pack(pady=5)

# Menu down the left side
menu_frame = tk.Frame(root, bg="lightgreen", padx=10, pady=10)
menu_frame.pack(side="left", fill="y")
tk.Button(menu_frame, text="Start", width=10).pack(pady=5)
tk.Button(menu_frame, text="Scores", width=10).pack(pady=5)
tk.Button(menu_frame, text="Quit", width=10, command=root.destroy).pack(pady=5)

# Main area on the right
main_frame = tk.Frame(root, bg="white")
main_frame.pack(side="left", fill="both", expand=True)
tk.Label(main_frame, text="Press Start to begin", bg="white",
         font=("Arial", 14)).pack(pady=40)

root.mainloop()
