
# A GUI app using a dictionary data type
'''
# instructions
# remove each of these comments as they are completed then put your name here instead

# find the error in the tkinter code that stops the file from running and fix it
# find the spelling error and fix it.

# change the dictionary to look up these planets:

Mercury: The closest planet to the Sun, Mercury is a small, rocky world with an iron core and a rocky crust.
Venus: Earth's sister planet; Venus is similar in size but radically different—its thick atmosphere is mostly carbon dioxide, and surface temperatures can exceed 454°C.
Earth: Our home planet; Earth is the only known place where life exists, with a breathable atmosphere and abundant water.
Mars: Known as the Red Planet, Mars has a thin atmosphere and is home to the largest volcano and deepest canyon in the solar system.
Jupiter: The largest planet, Jupiter is a gas giant composed mainly of hydrogen and helium, with a powerful magnetic field.
Saturn: Famous for its stunning rings, Saturn is another gas giant with a similar composition to Jupiter.
Uranus: An ice giant, Uranus has a tilted axis that causes extreme seasons and a unique ring system.
Neptune: The farthest planet from the Sun, Neptune is also an ice giant, with a deep blue color and strong winds.

# change bg colours from yellow to cornsilk
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
window = tk.Tk()
window.title("Rainbow hex colours")

# create label with instructions to enter term, stick to left of cell 
info_label = tk.Label(window, height=5, wraplength=300, justify='left', text="Enter a colour to look up: \nred, orange")
info_label.grid(row=0, column=0, sticky="w")

# create text entry box for user to enter term, stick to left of cell 
entry = tk.Entry(window, width=30, bg="yellow")
entry.grid(row=1, column=0, sticky="w")

# Add a submit button, stick to left of cell 
submit = tk.Button(window, text="LOOK UP COLOUR", width=25, bg="yellow", command=click)
submit.grid(row=2,column=0, sticky="w")

# create label for dictionary value, stick to left of cell 
def_label = tktkintersgreat.Label(window, text="Dicsoonairy value:")
def_label.grid(row=3, column=0, sticky="w")

# create text box to display dictionary value, stick to left of cell 
output_value = tk.Text(window, width=40, height=6, bg="yellow")
output_value.grid(row=4, column=0, columnspan=2, sticky="w")

# Run mainloop
window.mainloop()

