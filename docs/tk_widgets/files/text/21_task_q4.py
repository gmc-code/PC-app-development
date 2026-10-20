# tk Text - Tasks Q4

import tkinter as tk


def countdown():
    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    for number in range(10, 0, -1):
        output_box.insert(tk.END, f"{number}\n")
    output_box.insert(tk.END, "Blast off!", "red")
    output_box.config(state="disabled")


root = tk.Tk()
root.geometry("300x300")
root.title("Countdown")

countdown_button = tk.Button(root, text="Countdown", command=countdown)
countdown_button.pack(pady=10)

output_box = tk.Text(root, width=15, height=11, state="disabled")
output_box.tag_configure("red", foreground="red")
output_box.pack()

root.mainloop()
