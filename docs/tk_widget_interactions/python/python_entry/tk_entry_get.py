import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("500x300")  # Set window size
window.title("Entry Example")  # Set window title

# Create a StringVar to associate with the entry
name_var = tk.StringVar()

# Function to get the value from the entry field and display it in the label
def get_name():
    name = name_var.get()
    output_label.config(text=f"Name entered:\n{name}")

# Create the entry widget for input
name_entry = tk.Entry(window, textvariable=name_var, font=('calibre', 24, 'normal'), width=20)
name_entry.pack(pady=20)  # Add some padding to the top

# Create a button to trigger the get_name function
submit_button = tk.Button(window, text="Submit", command=get_name)
submit_button.pack(pady=10)

# Create a label to display the output
output_label = tk.Label(window, text="", font=('calibre', 24, 'normal'), width=30, height=2)
output_label.pack(pady=20)

# Run the main event loop
window.mainloop()
