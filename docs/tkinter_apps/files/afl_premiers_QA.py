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
