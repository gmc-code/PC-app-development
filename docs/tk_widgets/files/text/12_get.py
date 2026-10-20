# tk Text - get

import tkinter as tk


def count_words():
    writing = text_box.get("1.0", "end-1c")     # Read everything that was typed
    words = len(writing.split())                # Split into words and count them
    count_label.config(text=f"Words: {words}")


root = tk.Tk()
root.geometry("300x250")
root.title("get")

text_box = tk.Text(root, width=30, height=6, wrap="word")
text_box.pack(pady=10)

count_button = tk.Button(root, text="Count words", command=count_words)
count_button.pack()

count_label = tk.Label(root, text="Words: 0", font=("Arial", 14))
count_label.pack(pady=5)

root.mainloop()
