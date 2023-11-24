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
            <label for="superhero">Superhero name:</label> <p id="superhero"></p>
        </div>
        <py-config src="./pyscript.toml"></py-config>
        <py-script src="./main.py"></py-script>
    </body>
    </html>

----

main.py
------------

| 

.. code-block:: python

    from pyscript import document

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


    def get_superhero(first_initial, last_initial):
        superhero_name = first_names[first_initial] + " " + last_names[last_initial]
        return superhero_name

    def namegenerator(event):
        firstinitial_element = document.querySelector("#firstinitial")
        lastinitial_element = document.querySelector("#lastinitial")
        # add validation for letters A to Z; random if empty
        validAZ = True
        first_initial = firstinitial_element.value.upper()
        last_initial = lastinitial_element.value.upper()
        if not first_initial.isalpha():
            validAZ = False
        if not last_initial.isalpha():
            validAZ = False
        output_div_text = document.querySelector("#superhero")
        if validAZ:
            output_div_text.innerText = get_superhero(first_initial, last_initial)
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