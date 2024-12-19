====================================================
Introduction to pyscript
====================================================

| PyScript is a platform for Python in the browser.
| It combines html, css, and python in separate files.
| PyScript is designed to allow the running of Python in web browsers.
| PyScript apps can be hosted as a static web site.

----

Key references:
---------------------

| Docs https://docs.pyscript.net/2024.10.2/
| User guide: https://docs.pyscript.net/2024.10.2/user-guide/
| Developer blog on latest update changes: https://jeff.glass/tags/pyscript/

----

Sign up
----------

| Sign up is free.
| Go to https://pyscript.com/ and sign up.

----

New project
-------------

| To start a new project, on the dashboard, click the new project (plus) button.

.. image:: images/new_project.png
    :scale: 50%

----

Project files
--------------

| Making a new project in pyscript starts with 3 files.

.. image:: images/new_project_files.png
    :scale: 50%

| The **index.html** file is served to your browser. It has the interface elements and links to python code.
| The **main.py** is for python code that defines how your application works.
| The **pyscript.toml** file is used to configure the project.
| e.g specifying python modules via ``packages = ["numpy", "pandas"]``. It can be empty.

| The **pyscript.json** file is more efficient to use than the **pyscript.toml** file. An empty json file needs curly brackets as **{}**.
| For using comments and more complicated configurations use a toml file.
| See: https://docs.pyscript.net/2024.11.1/user-guide/configuration/

| A **main.css** file is often added to customize the html element appearance.

----

index.html
-----------------

| The **index.html** file starts as a basic template.
| The latest versions of the <link> and <script> tags have been inserted as shown below (as of Dec 2024).

.. code-block:: html


    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>App title</title>
        <!-- Recommended meta tags -->
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width,initial-scale=1.0">

        <!-- PyScript CSS -->
        <link rel="stylesheet" href="https://pyscript.net/releases/2024.11.1/core.css">

        <!-- This script tag bootstraps PyScript -->
        <script type="module" src="https://pyscript.net/releases/2024.11.1/core.js"></script>

        <!-- custom CSS only -->
        <link rel="stylesheet" href="main.css">
    </head>
    <body>
        <script type="py" src="./main.py" config="./pyscript.json></script>
    </body>
    </html>


----

Terminal
-----------------

To view the terminal as well use this script tag in the body:

.. code-block:: html

    ...
    <script type="py" src="./main.py" config="./pyscript.json" terminal></script>
    ...

