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

user_color = input('Enter a rainbow color (red, orange, yellow, green, blue, indigo, violet): ')

def return_hex_color(user_color, rainbow_colors):
    # Convert the input to lowercase for case-insensitivity
    user_color = user_color.lower()

    # Check if the input color exists in the rainbow_colors dictionary
    if user_color in rainbow_colors:
        return rainbow_colors[user_color]
    else:
        return "not listed in the dictionary"

hex_val = return_hex_color(user_color, rainbow_colors)
print(f"The hexadecimal value for {user_color} is {hex_val}.")