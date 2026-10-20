# ttk Frame - pack_forget

import tkinter as tk
from tkinter import ttk


def show_answer():
    question_frame.pack_forget()
    answer_frame.pack(pady=30)


root = tk.Tk()
root.geometry("300x200")
root.title("pack_forget")

question_frame = ttk.Frame(root)
question_frame.pack(pady=30)
ttk.Label(question_frame, text="What is the largest planet?").pack()
ttk.Button(question_frame, text="Show answer", command=show_answer).pack(pady=5)

answer_frame = ttk.Frame(root)          # Not packed yet, so hidden
ttk.Label(answer_frame, text="Jupiter!", font=("Arial", 24)).pack()

root.mainloop()
