import tkinter as tk

# Create a new window
root = tk.Tk()
# Set the title of the window
root.title("Button formatting")
# Set the size of the window
root.geometry("350x400")

def button_clicked():
    print("Button clicked!")

def change_text():
    button.config(text="New Text")

def toggle_state():
    if button['state'] == tk.NORMAL:
        button.config(state=tk.DISABLED,
                      disabledforeground="gray",
                      bg="darkgray")
    else:
        button.config(state=tk.NORMAL,
                      fg="black",
                      bg="lightgray")

def change_color():
    button.config(bg="yellow")

def reset_defaults():
    button.config(text="Click Me",
                  state=tk.NORMAL,
                  fg="black",
                  bg="lightgray",
                  highlightcolor="red")

def set_normal():
    button.config(state=tk.NORMAL,
                  fg="black",
                  bg="lightgray")

def set_disabled():
    button.config(state=tk.DISABLED,
                  disabledforeground="gray",
                  bg="darkgray")

def set_active():
    button.config(state=tk.ACTIVE,
                  activeforeground="blue",
                  activebackground="lightblue")

# Creating the main button with specified options
button = tk.Button(root,
                text="Click Me",
                command=button_clicked,
                activebackground="lightblue",
                activeforeground="blue",
                anchor="center",
                bd=3,
                cursor="hand2",
                font=("Arial", 14),
                height=2,
                highlightbackground="black",
                highlightcolor="red",
                highlightthickness=2,
                justify="center",
                overrelief="raised",
                padx=10,
                pady=5,
                width=15,
                wraplength=50)

button.pack(padx=20, pady=20)

# Creating additional buttons to modify the main button
change_text_button = tk.Button(root, text="Change Text", command=change_text)
change_text_button.pack(pady=5)

toggle_state_button = tk.Button(root, text="Disable/Enable", command=toggle_state)
toggle_state_button.pack(pady=5)

change_color_button = tk.Button(root, text="Change Color", command=change_color)
change_color_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_defaults)
reset_button.pack(pady=5)

# Creating state buttons to set the main button state
set_normal_button = tk.Button(root, text="Set Normal", command=set_normal)
set_normal_button.pack(pady=5)

set_disabled_button = tk.Button(root, text="Set Disabled", command=set_disabled)
set_disabled_button.pack(pady=5)

set_active_button = tk.Button(root, text="Set Active", command=set_active)
set_active_button.pack(pady=5)

root.mainloop()
