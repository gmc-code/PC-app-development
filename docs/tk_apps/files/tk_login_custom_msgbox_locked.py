import tkinter as tk

# Constants
BG_COLOR = "#333333"  # dark grey
FG_COLOR = "#FFFFFF"   # white
FG_BUTTON_COLOR = "#FF3399"  # bright pink
FONT_STYLE = ("Arial", 24)
USERNAME = "johns"
PASSWORD = "123"


def custom_messagebox(title, message, parent):
    """Custom messagebox aligned over the parent widget and disabling the parent window."""
    # Disable parent window while the messagebox is active
    parent.attributes('-disabled', True)

    top = tk.Toplevel(parent)  # Create a new top-level window
    top.title(title)
    top.configure(bg=BG_COLOR)
    top.transient(parent)  # Keep it on top of the parent
    top.grab_set()  # Make it modal (block input to the parent)

    # Center the top-level window over the parent
    parent_x = parent.winfo_rootx()
    parent_y = parent.winfo_rooty()
    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()

    # Calculate position to center the messagebox over the parent
    top_width = 500
    top_height = 150
    x = parent_x + (parent_width // 2) - (top_width // 2)
    y = parent_y + (parent_height // 2) - (top_height // 2)

    top.geometry(f"{top_width}x{top_height}+{x}+{y}")

    # Callback to close the messagebox and re-enable the parent window
    def on_close():
        parent.attributes('-disabled', False)  # Re-enable the parent window
        top.destroy()  # Destroy the messagebox

    # Bind the close button of the messagebox to the on_close function
    top.protocol("WM_DELETE_WINDOW", on_close)

    # Create widgets inside the custom messagebox
    message_label = tk.Label(top, text=message, bg=BG_COLOR, fg=FG_COLOR, font=FONT_STYLE)
    ok_button = tk.Button(top, text="OK", bg=FG_BUTTON_COLOR,
                            fg=FG_COLOR, font=FONT_STYLE, command=on_close)

    # Layout the widgets
    message_label.pack(expand=True, pady=20)
    ok_button.pack(pady=10)


def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    if entered_username == USERNAME and entered_password == PASSWORD:
        custom_messagebox("Login", "Logged in successfully!", window)
    else:
        custom_messagebox("Login Error", "Invalid login", window)


# Create the main window
window = tk.Tk()
window.title("Login form")
window.geometry("540x440")
window.configure(bg=BG_COLOR)

# Create frame widget for other widgets
frame = tk.Frame(window, bg=BG_COLOR)
frame.place(relx=0.5, rely=0.5, anchor='center')  # Centering the frame inside the window

# Create widgets inside the frame
login_label = tk.Label(frame, text="Login", bg=BG_COLOR, fg=FG_BUTTON_COLOR, font=FONT_STYLE)
username_label = tk.Label(frame, text="Username", bg=BG_COLOR, fg=FG_COLOR, font=FONT_STYLE)
password_label = tk.Label(frame, text="Password", bg=BG_COLOR, fg=FG_COLOR, font=FONT_STYLE)
username_entry = tk.Entry(frame, font=FONT_STYLE)
password_entry = tk.Entry(frame, show="*", font=FONT_STYLE)
login_button = tk.Button(frame, text="Login", bg=FG_BUTTON_COLOR, fg=FG_COLOR, font=FONT_STYLE, command=login)

# Place widgets in the frame using grid layout
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
username_label.grid(row=1, column=0, padx=10)
password_label.grid(row=2, column=0, padx=10)
username_entry.grid(row=1, column=1, pady=20)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=20)

window.mainloop()
