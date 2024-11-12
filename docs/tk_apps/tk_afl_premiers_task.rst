====================================================
AFL premiers task
====================================================

Python terminal game
-------------------------

This Python script implements a quiz game about AFL premierships, written for the terminal. Below is a summary of its key components:

- **Imports**:

  - `random`: For selecting a random team.
  - `os`: For clearing the terminal screen.

- **Functions**:

  - `clear_screen()`: Clears the terminal screen. Uses `cls` for Windows and `clear` for macOS/Linux.

- **Data**:

  - `premiers`: A dictionary containing AFL teams and their respective number of premierships.

- **Main Program**:

  - Displays the list of AFL premiers.
  - Prompts the user to start the quiz.
  - If the user agrees, the screen is cleared, and the quiz begins.
  - The quiz randomly selects a team and asks the user to guess the number of premierships.
  - The user's guess is checked against the correct number.
  - The user is informed if their guess is correct or incorrect.
  - The user can choose to continue or exit the quiz.
  - Finally, the program prints the list of teams and their premierships.


Code:

.. code-block:: python

    import random
    import os

    # Function to clear the terminal screen
    def clear_screen():
        # For Windows
        if os.name == 'nt':
            _ = os.system('cls')
        # For macOS and Linux
        else:
            _ = os.system('clear')

    # Dictionary of premiers with full team names
    premiers = {
        "Essendon": 16,
        "Collingwood": 16,
        "Carlton": 16,
        "Melbourne": 13,
        "Richmond": 13,
        "Hawthorn": 13,
        "Geelong": 10,
        "Sydney Swans": 5,  # Linked to South Melbourne
        "Brisbane Lions": 4,  # Linked to Fitzroy
        "West Coast Eagles": 4,
        "North Melbourne": 4,
        "Western Bulldogs": 2,
        "Adelaide": 2,
        "Port Adelaide": 1,
        "St Kilda": 1,
        "Fremantle": 0,
        "Greater Western Sydney": 0,
        "Gold Coast": 0,
        "Fitzroy": 8,
        "South Melbourne": 3
    }

    # Display the list of premiers for study
    print("List of AFL Premiers:\n")
    for team, premierships in premiers.items():
        print(f"{team}: {premierships} premierships")

    # Prompt to start the quiz
    start_quiz = input("\nDo you want to start the quiz? (Y/N): ").strip().upper()

    if start_quiz == "Y":
        clear_screen()  # Clear the terminal screen before starting the quiz
        while True:
            # Randomly select a team
            team = random.choice(list(premiers.keys()))

            # Ask the user to guess the number of premierships
            user_guess = input(f"How many premierships has {team} won? ").strip()

            # Get the correct number of premierships
            correct_premierships = premiers[team]

            # Check if the user's guess is correct
            if user_guess.isdigit() and int(user_guess) == correct_premierships:
                print("Correct!\n")
            else:
                print(f"Incorrect. {team} has won {correct_premierships} premierships.\n")

            # Ask the user if they want to continue or exit
            user_input = input("Press Enter to continue or any other key to exit: ").strip()
            if user_input != "":
                print("Exiting the program.\n")
                break

    print("\nFinal list of teams and their premierships:\n", premiers,"\n")

----

.. admonition:: Task

    #. Convert the terminal game above to a tkinter quiz game.
