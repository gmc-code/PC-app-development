import tkinter as tk

# Constants
WINDOW_BG_COLOR = "#ffffff"
INPUT_BG_COLOR = "#ffffff"
INPUT_FG_COLOR = "#0d6efd"
BUTTON_BG_COLOR = "#fd7e14"
BUTTON_FG_COLOR = "#ffffff"
OUTPUT_BG_COLOR = "#ffffff"
OUTPUT_FG_COLOR = "#dc3545"
FONT_STYLE = ("Arial", 32)

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


# Create the main window
window = tk.Tk()
window.title("Fahrenheit to Celsius Converter")
window.geometry("550x350")
window.configure(bg=WINDOW_BG_COLOR)

# Create widgets
f_label = tk.Label(window, text="Fahrenheit", bg=INPUT_BG_COLOR, fg=INPUT_FG_COLOR, font=FONT_STYLE)
f_entry = tk.Entry(window, width=10, bg=INPUT_BG_COLOR, fg=INPUT_FG_COLOR, font=FONT_STYLE)
c_label = tk.Label(window, text="Celsius", bg=OUTPUT_BG_COLOR, fg=OUTPUT_FG_COLOR, font=FONT_STYLE)
c_text = tk.Text(window, height=1, width=10, bg=OUTPUT_BG_COLOR, fg=OUTPUT_FG_COLOR, font=FONT_STYLE)
convert_button = tk.Button(window, text="Convert", width=20, bg=BUTTON_BG_COLOR,
                           fg=BUTTON_FG_COLOR, font=FONT_STYLE, command=convert_f_to_c)

# Place widgets on window
f_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
f_entry.grid(row=0, column=1, sticky="w", padx=10, pady=10)
c_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)
c_text.grid(row=2, column=1, sticky="w", padx=10, pady=10)
convert_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
window.mainloop()
