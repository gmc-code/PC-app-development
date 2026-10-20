# tk Frame - pack_forget

import tkinter as tk


def show_answer():
    question_frame.pack_forget()        # Hide the question
    answer_frame.pack(pady=20)          # Show the answer


root = tk.Tk()
root.geometry("300x200")
root.title("pack_forget")

question_frame = tk.Frame(root)
question_frame.pack(pady=20)
tk.Label(question_frame, text="What is the largest planet?").pack()
tk.Button(question_frame, text="Show answer", command=show_answer).pack(pady=5)

answer_frame = tk.Frame(root)           # Not packed yet, so it is hidden
tk.Label(answer_frame, text="Jupiter!", font=("Arial", 24)).pack()

root.mainloop()
