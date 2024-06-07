# Dictionary with rainbow colors
rainbow_colors = {"red": "#FF0000", "orange": "#FFA500", "yellow": "#FFFF00", "green": "#008000", "blue": "#0000FF", "indigo": "#4B0082", "violet": "#EE82EE"}

# Ask the user for input (color name)
user_color = input("Enter a color from the rainbow (red, orange, yellow, green, blue, indigo, violet): ")


def return_hex_color(user_color):
    # Convert the input to lowercase for case-insensitivity
    user_color = user_color.lower()

    # Check if the input color exists in the rainbow_colors dictionary
    if user_color in rainbow_colors:
        return rainbow_colors[user_color]
    else:
        return "not a valid colour of the rainbow"


def return_hex_color_statement(user_color):
    # Convert the input to lowercase for case-insensitivity
    user_color = user_color.lower()

    # Check if the input color exists in the rainbow_colors dictionary
    if user_color in rainbow_colors:
        return f"The hexadecimal value for {user_color} is {rainbow_colors[user_color]}."
    else:
        return f"{user_color} is not a valid color from the rainbow."


print(return_hex_color(user_color))
print(return_hex_color_statement(user_color))
