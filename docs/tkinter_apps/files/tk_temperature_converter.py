import tkinter as tk


def convert_f_to_c():
    try:
        fahrenheit = float(f_entry.get())
        celsius = (fahrenheit - 32) / 1.8
        c_text.delete(1.0, 'end')  # Clear any previous result
        c_text.insert(1.0, f'{celsius:.1f}')
    except ValueError:
        c_text.delete(1.0, 'end')
        c_text.insert(1.0, "Invalid input.")


# Create the main window
window = tk.Tk()
window.title("Fahrenheit to Celsius Converter")
window.geometry('300x200')
window.configure(bg='#333333')

# Create widgets
f_label = tk.Label(window, text="Fahrenheit", bg='#333333', fg='#FFFFFF', font=("Arial", 16))
c_label = tk.Label(window, text="Celsius", bg='#333333', fg='#FFFFFF', font=("Arial", 16))

f_entry = tk.Entry(window, width = 10, font=("Arial", 16))
# height of 1 is one text row
c_text = tk.Text(window, height=1, width = 10, font=("Arial", 16))

convert_button = tk.Button(window, text="Convert", width=20, bg='#FF3399', fg='#FFFFFF', font=("Arial", 16), command=convert_f_to_c)

# Place widgets on window
f_label.grid(row=0, column=0, padx=10, pady=10)
f_entry.grid(row=0, column=1, padx=10, pady=10)
c_label.grid(row=2, column=0, padx=10, pady=10)
c_text.grid(row=2, column=1, padx=10, pady=10)
convert_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)



# Start the main event loop
window.mainloop()
