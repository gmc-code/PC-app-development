import tkinter as tk
import random

# List of palindromes
palindromes = [
    "aibohphobia", "civic", "deified", "kayak", "level", "madam", "minim", "noon",
    "racecar", "radar", "refer", "repaper", "reviver", "rotator", "rotor", "sagas",
    "solos", "stats", "tenet", "wow"
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


# Create the main window
window = tk.Tk()
window.geometry("300x200")
window.title("String Reverser")

# Create a StringVar to hold the user input
input_var = tk.StringVar()

# Create a Label and Entry for user input
input_label = tk.Label(window, text="Enter a string:", font=("Helvetica", 12))
input_label.pack(pady=5)
input_entry = tk.Entry(window, textvariable=input_var, font=("Helvetica", 12))
input_entry.pack(pady=5)

# Create a Button to trigger the text reversal
button = tk.Button(window, text="Reverse Text", command=transform_text)
button.pack(pady=20)

# Create a StringVar to hold the transformed text
output_var = tk.StringVar()
output_var.set("")

# Create a Label widget with textvariable for the output
output_result = tk.Label(window, textvariable=output_var, font=("Helvetica", 12))
output_result.pack(pady=5)


# Run the application
window.mainloop()
