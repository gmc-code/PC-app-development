====================================================
Elves
====================================================

| The details below are for a simple elves name generator.
| Demo app is at: https://gmc_ps.pyscriptapps.com/elves/latest/

.. image:: images/elves/elves.png
    :scale: 75%

----

index.html
---------------------

| The html is below.
| Note that is refers to a favicon.ico that is placed in the files section in the pyscirpt editor so it shows in a browser tab bar.

.. code-block:: html

    <!-- GMC Nov 2024 -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>20_Elves</title>
        <!-- Recommended meta tags -->
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width,initial-scale=1.0">

        <!-- favicon to appear in browser tab -->
        <link rel="icon" href="favicon.ico" type="image/x-icon>

        <!-- PyScript CSS -->
        <link rel="stylesheet" href="https://pyscript.net/releases/2024.11.1/core.css">

        <!-- This script tag bootstraps PyScript -->
        <script type="module" src="https://pyscript.net/releases/2024.11.1/core.js"></script>

        <!-- CSS only -->
        <link rel="stylesheet" href="main.css">
    </head>
    <body>
        <h1>Elves Name Generator</h1>
        <p>How many Elves (from 1 to 20) would you like to name?</p>
        <div style="display: flex; align-items: center;">
            <input type="number" min="1" max="20" id="elfnumber" placeholder="1" ">
            <button id="elf_generator">Name Elves</button>
        </div>

        <h2>Elf names:</h2>
        <div id="elves">
        </div>

        <script type="py" src="./main.py" config="./pyscript.toml"></script>
    </body>
    </html>

----

main css:
--------------------

The custom css is below.

.. code-block:: css

    body {
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        padding: 20px;
        background-color: #f8f9fa;
    }

    h1,
    h2 {
        color: #343a40;
    }

    p {
        margin-bottom: 20px;
        color: #6c757d;
    }

    input[type="number"] {
        max-width: 50px; /* Increase the width */
        height: 28px; /* Increase the height */
        margin-right: 10px;
        padding: 10px 20px; /* Adjust padding as needed */
        border: 1px solid #ced4da;
        border-radius: 0.25rem;
        font-size: 18px; /* Increase the font size */
    }

    button {
        background-color: #007bff; /* Bootstrap primary */
        border: none;
        color: white;
        padding: 10px 20px; /* Adjust padding as needed */
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 24px; /* Adjust font size as needed */
        margin: 0.375rem 0.375rem;
        cursor: pointer;
        border-radius: 0.25rem;
        transition: background-color 0.15s ease-in-out;
    }

    button:hover {
        background-color: #0056b3;
    }

    #elves {
        margin-top: 0px;
        border: 1px solid #ced4da;
        padding: 0 20px 20px;
        border-radius: 0.25rem;
        min-height: 50px;
        max-width: 350px; /* Increase the width */
    }


----

main.py
------------------

| The python code below generates random elf names based on user input. Here's a brief summary:

- Imports: It imports necessary modules from PyScript and the random module.
- Dictionaries: Two dictionaries, firstNames and lastNames, map initials to elf names.
- Function get_elves(num): Generates a specified number of random elf names by combining a random first name and last name from the dictionaries.
- Function validate_elfnumber(event): Validates the user input for the number of elves, ensuring it's between 1 and 20. If the input is invalid, it sets a default value. This function is called whenever there is an input event on the html element with the ID elfnumber. This ensures that the number of elves entered by the user is validated in real-time.
- Function elf_generator(event): This function is called when the element with the ID elf_generator is clicked. It calls validate_elfnumber to ensure the input is valid, generates the elf names using get_elves, and displays the result in the html element with the ID elves.

.. code-block:: python

    from pyscript import document
    from pyscript import display
    from pyscript import when
    import random

    firstNames = {
        'A':'Angelic', 'B':'Blustery', 'C':'Cheery',
        'D':'Dancy', 'E':'Elfie', 'F':'Festive',
        'G':'Glistening', 'H':'Happy', 'I':'Icy',
        'J':'Jolly', 'K':'Kringle', 'L':'Lucky',
        'M':'Merry', 'N':'Naughty', 'O':'Oily',
        'P':'Pointy', 'Q':'Quirky', 'R':'Rosie',
        'S':'Snowy', 'T':'Tinsel', 'U':'Unity',
        'V':'Very Merry', 'W':'Wintry', 'X':'Xmasy',
        'Y':'Yule', 'Z':'Zippy'
    }

    lastNames = {
        'A':'Angel', 'B':'Bells', 'C':'Candy Cane',
        'D':'Dash', 'E':'Evergreen', 'F':'Feet',
        'G':'Gingerbread', 'H':'Holidays', 'I':'Icicles',
        'J':'Jingles', 'K':'Kringles', 'L':'Lights',
        'M':'McSnowface', 'N':'Noel', 'O':'Ornament',
        'P':'Peppermint', 'Q':'Quince Pie', 'R':'Ribbon',
        'S':'Snowball', 'T':'Toes', 'U':'Upatree',
        'V':'Vixen', 'W':'Wonderland', 'X':'Xmas',
        'Y':'Yuletide', 'Z':'Zest'
    }


    def get_elves(num):
        elves = ""
        for i in range(num):
            firstInitial = random.choice(list(firstNames.keys()))
            lastInitial = random.choice(list(lastNames.keys()))
            elfName = firstNames [firstInitial] + " " + lastNames [lastInitial]
            if elves == "":
                elves = elfName
            else:
                elves = elves + ", " + elfName
        return elves

    @when('input', '#elfnumber')
    def validate_elfnumber(event):
        input_text_element = document.getElementById("elfnumber")
        try:
            num = int(input_text_element.value)
            if num < 1 or num > 20:
                if num < 1:
                    num = 1
                    input_text_element.value = 1
                elif num > 20:
                    num = 20
                    input_text_element.value =20
        except ValueError:
            num = 1
            input_text_element.value = 1


    @when('click', '#elf_generator')
    def elf_generator(event):
        validate_elfnumber(event)
        input_text_element = document.getElementById("elfnumber")
        num = int(input_text_element.value)
        elves_text = get_elves(num)
        output_div_text = document.getElementById("elves")
        # output_div_text.innerText = elves_text
        display(elves_text, target="#elves", append=False)
