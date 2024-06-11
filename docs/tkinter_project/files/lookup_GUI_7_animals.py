
# A GUI app using a dictionary data type
'''
# instructions
# remove each of these comments as they are completed then put your name here instead

# find the error in the tkinter code that stops the file from running and fix it
# find the spelling error and fix it.

# change the dictionary to look up these iconic Australian animals:

Kangaroo: These marsupials are known for their powerful hind legs, which allow them to bound across the landscape at speeds of up to 44 mph. Kangaroos feed on grasses and herbaceous plants and are gracefully agile swimmers in water.
Saltwater Crocodile: Also known as 'salties,' these giant reptiles inhabit various waterways in Australia. They can grow up to 20 feet long, weigh over 1,000 pounds, and have sharp teeth for catching prey like fish, birds, and small mammals.
Scrub Python: This nonvenomous snake is the longest snake species in Australia, with an average length of 16-23 feet. It has distinctive coloration and ambushes prey by hiding in vegetation before striking with lightning speed.
Koala: These adorable creatures have soft, gray fur, big ears, and spend most of their time in trees. Koalas mainly eat leaves, grasses, and shrubs, and they're very social animals that often cuddle together in trees.
Wedge-Tailed Eagle: A majestic bird of prey, the wedge-tailed eagle soars through the sky with its impressive wingspan. It's a symbol of strength and freedom in Australian culture.
Platypus: The platypus is a unique monotreme that lays eggs and has a duck-like bill, webbed feet, and a beaver-like tail. It's a fascinating blend of features rarely seen in other animals.
Wombat: These sturdy marsupials are excellent diggers, creating burrows in the ground. With their stocky bodies and powerful legs, wombats are well-adapted to their bushland habitats.

# change bg colours from yellow to orange
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

