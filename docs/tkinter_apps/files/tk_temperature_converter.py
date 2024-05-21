import tkinter as tk


def convert_f_to_c():
    """
    Converts Fahrenheit to Celsius and displays the result in the GUI.

    Reads the Fahrenheit value from the input field, performs the conversion,
    and updates the result in the output text widget.

    Raises:
        ValueError: If the input is not a valid float.
    """
    try:
        fahrenheit = float(f_entry.get())
        celsius = (fahrenheit - 32) / 1.8
        c_text.delete(1.0, "end")  # Clear any previous result
        c_text.insert(1.0, f"{celsius:.1f}")
    except ValueError:
        c_text.delete(1.0, "end")
        c_text.insert(1.0, "Invalid input.")


def setup_gui():
    """
    Sets up the Fahrenheit to Celsius converter GUI.
    Creates the main window, labels, entry fields, and buttons.
    """
    window = tk.Tk()
    window.title("Fahrenheit to Celsius Converter")
    window.geometry("300x200")
    window.configure(bg="#333333")

    # Common font style
    font_style = ("Arial", 16)

    # Colors
    bg_color = "#333333"
    fg_color = "#FFFFFF"
    button_color = "#FF3399"

    # Create widgets
    f_label = tk.Label(window, text="Fahrenheit", bg=bg_color, fg=fg_color, font=font_style)
    f_entry = tk.Entry(window, width=10, font=font_style)
    
    c_label = tk.Label(window, text="Celsius", bg=bg_color, fg=fg_color, font=font_style)
    c_text = tk.Text(window, height=1, width=10, font=font_style)

    convert_button = tk.Button(window, text="Convert", width=20, 
                               bg=button_color, fg=fg_color, font=font_style, command=convert_f_to_c)

    # Place widgets on window
    f_label.grid(row=0, column=0, padx=10, pady=10)
    f_entry.grid(row=0, column=1, padx=10, pady=10)
    c_label.grid(row=2, column=0, padx=10, pady=10)
    c_text.grid(row=2, column=1, padx=10, pady=10)
    convert_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Start the main event loop
    window.mainloop()


# Call the setup function
setup_gui()
