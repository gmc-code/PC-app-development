import tkinter as tk

# Constants
BG_COLOR = "#FFFFFF"
FG_COLOR = "#444444"
BG_TEXT_COLOR = "#e5e5e5"
FONT_STYLE = ("Arial", 30)


def place_name_age():
    """
    Takes the name and age and displays 2 sentences with them in it, in the GUI.
    """
    # get name
    name = name_entry.get()
    if name == "":
        name = "John Smith"
    # get age
    age = age_entry.get()
    if age == "":
        age = "16"
    # clear name_age_text 1.0 represents line.column or line 1 character 0, tk.END or 'end' can be used.
    name_age_text.delete(1.0, "end")
    # insert name age using f string, \n is a line break;
    name_age_text.insert(1.0, f"My name is {name}. \nI am {age} years old.")


# Create the main window
window = tk.Tk()
window.title("Name and age")
window.geometry("700x380")
window.configure(bg=BG_COLOR)

#  create widgets
name_label = tk.Label(window, text="Name", bg=BG_COLOR, fg=FG_COLOR, font=FONT_STYLE)
age_label = tk.Label(window, text="Age", bg=BG_COLOR, fg=FG_COLOR, font=FONT_STYLE)
name_entry = tk.Entry(window, bg=BG_TEXT_COLOR, fg=FG_COLOR, font=FONT_STYLE)
age_entry = tk.Entry(window, bg=BG_TEXT_COLOR, fg=FG_COLOR, font=FONT_STYLE)
name_age_button = tk.Button(window, text="Name and Age", bg=BG_COLOR,
                            fg=FG_COLOR, font=FONT_STYLE, command=place_name_age)
# Text widget height=2 where height is in text rows.
name_age_text = tk.Text(window, height=2, width=30, bg=BG_TEXT_COLOR, fg=FG_COLOR, font=FONT_STYLE)

# place widgets on window
name_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
name_entry.grid(row=0, column=1, sticky="w", padx=10, pady=10)
age_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)
age_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)
name_age_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
name_age_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
window.mainloop()
