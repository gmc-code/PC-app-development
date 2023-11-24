====================================================
Superheroes
====================================================

.. image:: images/superhero1.png
    :scale: 100%

| The details below are for a simple superhero name generator using initials as input.

----

Superhero Name Generator: simple version
-------------------------------------------

Making a new project in pyscript starts with 3 files.

.. image:: images/new_project_files.png
    :scale: 100%

| The **index.html** file is served to your browser. It has the interface elements and links to python code.
| The **main.py** is for python code that defines how your application works.
| The **pyscript.toml** file is used to configure the project. e.g specifying python modules via   ``packages = ["numpy"]``

----

pyscript.toml
------------------

| This file will be empty, since htere are no needed modules in this simple version.

----

index.html
-----------------


| The 


.. code-block:: html

    <!-- GMC Nov 2023; no css; no js; using 2023.05.1/pyscript.js -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Superhero Name</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <link rel="stylesheet" href="https://pyscript.net/releases/2023.11.1/pyscript.css" />
        <script type="module" src="https://pyscript.net/releases/2023.11.1/core.js"></script>
    </head>
    <body>
        <h1>Superhero Name Generator</h1>
        <p>Enter initials.</p>
        <div class="form-group">
            <label for="firstinitial">First name initial:</label>
            <input type="text" id="firstinitial" name="firstinitial"">
        </div>
        <div class="form-group">
            <label for="lastinitial">Last name initial:</label>
            <input type="text" id="lastinitial" name="lastinitial">
        </div>
        <button py-click="namegenerator">Generate Superhero</button><br>
        <div class="form-group">
            <label for="superhero">Superhero name:</label>
            <p id="superhero"></p>
        </div>
        <py-config src="./pyscript.toml"></py-config>
        <py-script src="./main.py"></py-script>
    </body>
    </html>

| `<div class="form-group">` is an HTML element that is used to group related form elements together. It is used here to the labels and input fields together.
| `<p id="superhero"></p>` has no text between the tags. It will be filled when the button is clicked.
| `<py-script src="./main.py"></py-script>` links to the `main.py` file. They could be renamed to suit.
----

main.py
------------

| The code is a program that generates and displays a superhero name based on the user input. It uses two dictionaries to store the possible first and last names for superheroes, and a function that returns a superhero name based on the first and last initials. It also uses another function that handles the user input and displays the superhero name or an error message if the input is not valid. The code uses the pyscript module to interact with the HTML elements of the web page. 

.. code-block:: python

    from pyscript import document

    # Define two dictionaries to store the possible first and last names for superheroes
    first_names = {
        "A": "Atomic", "B": "Blazing", "C": "Cosmic",
        "D": "Daring", "E": "Electric", "F": "Furious",
        "G": "Galactic", "H": "Hyper", "I": "Invincible",
        "J": "Justice", "K": "Kinetic", "L": "Legendary",
        "M": "Mighty", "N": "Noble", "O": "Omega",
        "P": "Polaris", "Q": "Quantum", "R": "Radiant",
        "S": "Stealth", "T": "Titan", "U": "Unstoppable",
        "V": "Vigilant", "W": "Warrior", "X": "Xeno",
        "Y": "Yieldless", "Z": "Zephyr",
    }

    last_names = {
        "A": "Avenger", "B": "Blade", "C": "Crusader",
        "D": "Defender", "E": "Eagle", "F": "Falcon",
        "G": "Guardian", "H": "Hawk", "I": "Inferno",
        "J": "Jaguar", "K": "Knight", "L": "Lion",
        "M": "Marvel", "N": "Ninja", "O": "Oracle",
        "P": "Phantom", "Q": "Quicksilver", "R": "Ranger",
        "S": "Specter", "T": "Thunder", "U": "Ultra",
        "V": "Viper", "W": "Wolf", "X": "Xiphos",
        "Y": "Youngstorm", "Z": "Zoom",
    }

    # Define a function that takes two initials as parameters and returns a superhero name
    def get_superhero(first_initial, last_initial):
        """Returns a superhero name based on the first and last initials.

        Args:
            first_initial (str): The first initial of the superhero name.
            last_initial (str): The last initial of the superhero name.

        Returns:
            str: The superhero name composed of the first and last names corresponding to the initials.
        """
        superhero_name = first_names[first_initial] + " " + last_names[last_initial]
        return superhero_name

        
    # Define a function that handles the user input and displays the superhero name
    def namegenerator(event):
        """Generates and displays a superhero name based on the user input.

        Args:
            event (Event): The event object that triggered the function.

        Returns:
            None
        """
        # Get the input elements for the first and last initials
        firstinitial_element = document.querySelector("#firstinitial")
        lastinitial_element = document.querySelector("#lastinitial")
        # Add validation for letters A to Z; random if empty
        validAZ = True
        first_initial = firstinitial_element.value.upper()
        last_initial = lastinitial_element.value.upper()
        # Check if the inputs are alphabetic characters
        if not first_initial.isalpha():
            validAZ = False
        if not last_initial.isalpha():
            validAZ = False
        # Get the output element for the superhero name
        output_div_text = document.querySelector("#superhero")
        # If the inputs are valid, generate and display the superhero name
        if validAZ:
            output_div_text.innerText = get_superhero(first_initial, last_initial)
        # Otherwise, display an error message
        else:
            output_div_text.innerText = "Enter initials."


----

Javascript improvements
----------------------------

.. image:: images/superhero_files.png
    :scale: 100%

.value and .innerText are both properties of HTML elements that can be used to get or set the text content of an element. However, they are used in different contexts.

.value is used to get or set the value of an input element, such as a text input or a select element. For example, if you have an input element with an id of myInput, you can get its value using document.getElementById('myInput').value.

.innerText is used to get or set the text content of an element, such as a <div> or a <p> element. For example, if you have a <div> element with an id of myDiv, you can get its text content using document.getElementById('myDiv').innerText.

In general, you should use .value to get or set the value of an input element, and .innerText to get or set the text content of other types of elements.