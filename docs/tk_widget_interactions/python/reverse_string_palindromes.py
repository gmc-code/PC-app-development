import tkinter as tk
import random

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

output_label = tk.Label(root, text="Reversed string:", font=("Helvetica", 12))
output_label.pack(pady=10)

# Create a StringVar to hold the transformed text
output_var = tk.StringVar()
output_var.set("")

# Create a Label widget with textvariable for the output
output_result = tk.Label(root, textvariable=output_var, font=("Helvetica", 12))
output_result.pack(pady=10)

# List of palindromes
palindromes = [
    "aibohphobia", "civic", "deified", "kayak", "level", "madam", "minim", "noon", "racecar", "radar",
    "refer", "repaper", "reviver", "rotator", "rotor", "sagas", "solos", "stats", "tenet", "wow"
]


# Function to transform the text
def transform_text():
    user_input = input_var.get()
    if user_input:
        # Reverse the user input
        reversed_text = user_input[::-1]
        output_var.set(reversed_text)
    else:
        # Use a random palindrome if no input is provided
        random_palindrome = random.choice(palindromes)
        input_var.set(random_palindrome)
        output_var.set(random_palindrome)


# Create a Button to trigger the text reversal
button = tk.Button(root, text="Reverse Text", command=transform_text)
button.pack(pady=20)

# Run the application
root.mainloop()
