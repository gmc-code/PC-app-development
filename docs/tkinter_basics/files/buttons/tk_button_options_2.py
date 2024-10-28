import tkinter as tk

# Create a new window
window = tk.Tk()
# Set the title of the window
window.title("Button formatting")
# Set the size of the window
window.geometry("350x400")

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

# Creating the main button with specified options
button = tk.Button(window,
                text="Click Me",
                command=button_clicked,
                activebackground="blue",
                activeforeground="white",
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
change_text_button = tk.Button(window, text="Change Text", command=change_text)
change_text_button.pack(pady=5)

toggle_state_button = tk.Button(window, text="Disable/Enable", command=toggle_state)
toggle_state_button.pack(pady=5)

change_color_button = tk.Button(window, text="Change Color", command=change_color)
change_color_button.pack(pady=5)

reset_button = tk.Button(window, text="Reset", command=reset_defaults)
reset_button.pack(pady=5)

window.mainloop()
