
# A GUI app using a dictionary data type
'''
# instructions
# remove each of these comments as they are completed then put your name here instead

# find the error in the tkinter code that stops the file from running and fix it
# find the spelling error and fix it.

# change the dictionary to look up these classic board games:

Monopoly: The iconic real estate trading game where players buy, sell, and build properties to bankrupt opponents.
Scrabble: A word game where players create words on a grid using letter tiles with different point values.
Yahtzee: A dice game where players roll dice to form specific combinations and score points.
Chess: The timeless two-player strategy game with origins dating back to the sixth century A.D..
Connect Four: A quick and engaging game where players aim to align four discs in a row vertically, horizontally, or diagonally.
Risk: A classic strategy game of global conquest, where players lead armies and vie for world domination.
Clue: A deduction game where players solve a murder mystery by identifying the murderer, weapon, and location.

# change bg colours from yellow to moccasin
# change window title to match the topic
# change labels and button text to better indicate the topic
# change the first label text so it has a list of possible user inputs

'''

import tkinter as tk


# The dictionary:
my_dictionary = {
    "red": "#FF0000",
    "orange": "#FFA500",
}

# place dictionary value
def click():
    entered_text = entry.get()  # collect text from text entry box
    output_value.delete(0.0, "end")  # clear text box
    value = my_dictionary.get(entered_text,"There is no entry for this value.")
    output_value.insert("end", value)  # add text to end of text

# main:
root = tk.Tk()
root.title("Rainbow hex colours")

# create label with instructions to enter term, stick to left of cell
info_label = tk.Label(root, height=5, wraplength=300, justify='left', text="Enter a colour to look up: \nred, orange")
info_label.grid(row=0, column=0, sticky="w")

# create text entry box for user to enter term, stick to left of cell
entry = tk.Entry(root, width=30, bg="yellow")
entry.grid(row=1, column=0, sticky="w")

# Add a submit button, stick to left of cell
submit = tk.Button(root, text="LOOK UP COLOUR", width=25, bg="yellow", command=click)
submit.grid(row=2,column=0, sticky="w")

# create label for dictionary value, stick to left of cell
def_label = tktkintersgreat.Label(root, text="Dicsoonairy value:")
def_label.grid(row=3, column=0, sticky="w")

# create text box to display dictionary value, stick to left of cell
output_value = tk.Text(root, width=40, height=6, bg="yellow")
output_value.grid(row=4, column=0, columnspan=2, sticky="w")

# Run mainloop
root.mainloop()

