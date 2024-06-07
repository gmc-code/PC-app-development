# Dictionary with rainbow colors
rainbow_colors = {
    "red": "#FF0000",
    "orange": "#FFA500",
    "yellow": "#FFFF00",
    "green": "#008000",
    "blue": "#0000FF",
    "indigo": "#4B0082",
    "violet": "#EE82EE"
}

# Ask the user for input (color name)
user_input = input("Enter a color from the rainbow (red, orange, yellow, green, blue, indigo, violet): ")

# Convert the input to lowercase for case-insensitivity
user_input = user_input.lower()

# Check if the input color exists in the rainbow_colors dictionary
if user_input in rainbow_colors:
    print(
        f"The hexadecimal value for {user_input} is {rainbow_colors[user_input]}."
    )
else:
    print(f"{user_input} is not a valid color from the rainbow.")
