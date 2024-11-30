import tkinter as tk


# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(*args):
    celsius = celsius_var.get()
    fahrenheit = round(celsius * 9 / 5 + 32, 1)  # Round to 1 decimal place
    fahrenheit_var.set(fahrenheit)


# Create the main window
window = tk.Tk()
window.geometry("300x200")
window.title("Celsius to Fahrenheit Converter")

# Create a DoubleVar to hold the Celsius value
celsius_var = tk.DoubleVar()
celsius_var.set(0.0)  # Initial value

# Create a DoubleVar to hold the Fahrenheit value
fahrenheit_var = tk.DoubleVar()
fahrenheit_var.set(32.0)  # Initial value

# Create a Label and Entry for Celsius
celsius_label = tk.Label(window, text="Celsius:", font=("Helvetica", 12))
celsius_label.grid(row=0, column=0, padx=2, pady=10, sticky="e")
celsius_entry = tk.Entry(window, textvariable=celsius_var, font=("Helvetica", 12))
celsius_entry.grid(row=0, column=1, padx=5, pady=10)
celsius_var.trace_add("write", convert_to_fahrenheit)

# Create a Label and Entry for Fahrenheit (read-only)
fahrenheit_label = tk.Label(window, text="Fahrenheit:", font=("Helvetica", 12))
fahrenheit_label.grid(row=1, column=0, padx=2, pady=10, sticky="e")
fahrenheit_entry = tk.Entry(window, textvariable=fahrenheit_var, font=("Helvetica", 12), state="readonly")
fahrenheit_entry.grid(row=1, column=1, padx=5, pady=10)

# Create an informational Label
info_label = tk.Label(window, text="Enter a temperature in Celsius to convert it to Fahrenheit.", font=("Helvetica", 10), wraplength=200)
info_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the application
window.mainloop()
