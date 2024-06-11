
# A GUI app using a dictionary data type
'''
# instructions
# remove each of these comments as they are completed then put your name here instead

# find the error in the tkinter code that stops the file from running and fix it
# find the spelling error and fix it.

# change the dictionary to look up these remarkable achievements of mankind:

Travelling to the Moon: Landing on the moon represents our ultimate technological achievement, surpassing millennia-old religious questions and opening up possibilities for exploration beyond our solar system.
Mastering Flight: From the Wright brothers' first flight to modern aviation, flight has revolutionized travel, exploration, and global connectivity.
Creating Photography: Photography immortalizes moments in time, allowing us to capture history, culture, and personal memories.
Creating Electronic Devices: From radios to smartphones, electricity and electronic devices have transformed communication, entertainment, and medicine.
Development of Vaccines: Vaccines have saved countless lives and eradicated deadly diseases.
Climbing Mount Everest: Conquering the world's highest peak showcases human determination and resilience.
The Great Pyramids: Ancient engineering marvels like the Pyramids of Giza continue to awe us with their precision and endurance.

# change bg colours from yellow to pink
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

