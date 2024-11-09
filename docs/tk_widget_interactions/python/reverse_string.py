import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("400x300")
root.title("String Reverser")

# Create a StringVar to hold the user input
input_var = tk.StringVar()

# Create a Label and Entry for user input
input_label = tk.Label(root, text="Enter a string:", font=("Helvetica", 12))
input_label.pack(pady=10)
input_entry = tk.Entry(root, textvariable=input_var, font=("Helvetica", 12))
input_entry.pack(pady=10)

output_labe = tk.Label(root, text="Reversed string:", font=("Helvetica", 12))
output_labe.pack(pady=10)

# Create a StringVar to hold the transformed text
output_var = tk.StringVar()
output_var.set("")

# Create a Label widget with textvariable for the output
output_result = tk.Label(root, textvariable=output_var, font=("Helvetica", 12))
output_result.pack(pady=10)


# Function to transform the text
def transform_text():
    user_input = input_var.get()
    if user_input:
        # reverse
        reversed_text = user_input[::-1]
        output_var.set(reversed_text)
    else:
        output_var.set("Please enter a string.")


# Create a Button to trigger the text Reversal
button = tk.Button(root, text="Reversed Text", command=transform_text)
button.pack(pady=20)

# Run the application
root.mainloop()
