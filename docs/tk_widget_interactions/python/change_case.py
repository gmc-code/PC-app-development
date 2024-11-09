import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("400x300")
root.title("String Transformer")

# Create a StringVar to hold the user input
input_var = tk.StringVar()

# Create a Label and Entry for user input
input_label = tk.Label(root, text="Enter a string:", font=("Helvetica", 12))
input_label.pack(pady=10)
input_entry = tk.Entry(root, textvariable=input_var, font=("Helvetica", 12))
input_entry.pack(pady=10)

# Create a StringVar to hold the transformed text
output_var = tk.StringVar()
output_var.set("Transformed Text")

# Create a Label widget with textvariable for the output
output_label = tk.Label(root, textvariable=output_var, font=("Helvetica", 16))
output_label.pack(pady=20)


# Function to transform the text
def transform_text():
    user_input = input_var.get()
    if user_input:
        # Perform some interesting transformations
        reversed_text = user_input[::-1]
        uppercase_text = user_input.upper()
        vowel_count = sum(1 for char in user_input if char.lower() in "aeiou")

        # Create a result string with the transformations
        result = f"Reversed: {reversed_text}\nUppercase: {uppercase_text}\nVowel Count: {vowel_count}"
        output_var.set(result)
    else:
        output_var.set("Please enter a string.")


# Create a Button to trigger the text transformation
button = tk.Button(root, text="Transform Text", command=transform_text)
button.pack(pady=20)

# Run the application
root.mainloop()
