import tkinter as tk
from tkinter import messagebox

# Constants
BG_COLOR = "#333333"  # dark grey
FG_COLOR = "#FFFFFF"   # white
FG_BUTTON_COLOR = "#FF3399"  # bright pink
FONT_STYLE = ("Arial", 24)
USERNAME = "johns"
PASSWORD = "123"


def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    if entered_username == USERNAME and entered_password == PASSWORD:
        messagebox.showinfo("Login", "Logged in successfully!")
    else:
        messagebox.showerror("Login Error", "Invalid login")


# Create the main window
window = tk.Tk()
window.title("Login form")
window.geometry("600x440")
window.configure(bg=BG_COLOR)

#  create frame widget for other widgets
frame = tk.Frame(window, bg=BG_COLOR)
frame.place(relx=0.5, rely=0.5, anchor='center')  # Centering the frame inside the window

#  create widgets in frame
login_label = tk.Label(frame, text="Login", bg=BG_COLOR, fg=FG_BUTTON_COLOR, font=FONT_STYLE)
username_label = tk.Label(frame, text="Username", bg=BG_COLOR, fg=FG_COLOR, font=FONT_STYLE)
password_label = tk.Label(frame, text="Password", bg=BG_COLOR, fg=FG_COLOR, font=FONT_STYLE)
username_entry = tk.Entry(frame, font=FONT_STYLE)
password_entry = tk.Entry(frame, show="*", font=FONT_STYLE)
login_button = tk.Button(frame, text="Login", bg=FG_BUTTON_COLOR, fg=FG_COLOR, font=FONT_STYLE, command=login)


# place widgets in frame
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
username_label.grid(row=1, column=0)
password_label.grid(row=2, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=20)


window.mainloop()
