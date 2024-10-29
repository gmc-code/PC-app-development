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

def convert():
    """
    Converts Pounds to Kgs and displays the result in the GUI.

    Reads the Pounds value from the input field, performs the conversion,
    and updates the result in the output text widget.

    Raises:
        ValueError: If the input is not a valid float.
    """
    try:
        pounds = float(input_entry.get())
        kilograms = pounds * 0.45359237
        output_text.delete(1.0, "end")  # Clear any previous result
        output_text.insert(1.0, f"{kilograms:.2f}")
    except ValueError:
        output_text.delete(1.0, "end")
        output_text.insert(1.0, "Invalid input.")

# Create the main window
window = tk.Tk()
window.title("Pounds to Kgs Converter")
window.geometry("550x300")
window.configure(bg=WINDOW_BG_COLOR)

# Create widgets
input_label = tk.Label(window, text="Pounds", bg=INPUT_BG_COLOR, fg=INPUT_FG_COLOR, font=FONT_STYLE)
input_entry = tk.Entry(window, width=10, bg=INPUT_BG_COLOR, fg=INPUT_FG_COLOR,
highlightcolor=INPUT_FG_COLOR, highlightbackground=INPUT_FG_COLOR, highlightthickness=2, font=FONT_STYLE)
output_label = tk.Label(window, text="Kgs", bg=OUTPUT_BG_COLOR, fg=OUTPUT_FG_COLOR, font=FONT_STYLE)
output_text = tk.Text(window, height=1, width=10, fg=OUTPUT_FG_COLOR, highlightcolor=OUTPUT_FG_COLOR, highlightbackground=OUTPUT_FG_COLOR, highlightthickness=1, font=FONT_STYLE)
convert_button = tk.Button(window, text="Convert", width=20, bg=BUTTON_BG_COLOR,
                           fg=BUTTON_FG_COLOR, font=FONT_STYLE, command=convert)


# Place widgets on window
input_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
input_entry.grid(row=0, column=1, sticky="w", padx=10, pady=10)
output_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)
output_text.grid(row=2, column=1, sticky="w", padx=10, pady=10)
convert_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
window.mainloop()
