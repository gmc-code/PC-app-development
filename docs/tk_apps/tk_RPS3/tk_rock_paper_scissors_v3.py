import tkinter as tk
import random
from pathlib import Path

# Constants
BG_COLOR = "#ffffff"
TEXT_COLOR = "#333333"
BUTTON_BG_COLOR = "#6750a4"  # purple
BUTTON_FG_COLOR = "#ffffff"
TITLE_FONT = ("Arial", 26, "bold")
FONT_STYLE = ("Arial", 16)
SCORE_FONT = ("Arial", 24, "bold")
# The images are in the rps_images folder, next to this file
IMAGE_FOLDER = Path(__file__).parent / "rps_images"

# Game data
CHOICES = ["Rock", "Paper", "Scissors"]
RESULTS = ["Win", "Lose", "Tie"]
RESULT_MESSAGES = {"Win": "You win this round!",
                   "Lose": "You lose this round!",
                   "Tie": "It's a tie! Tied rounds do not count."}
MATCH_LENGTHS = [1, 3, 5]

# Scores for the current match
user_score = 0
computer_score = 0


def determine_winner(user, computer):
    """Returns the computer's result, then the user's result.

    Each result is "Win", "Lose" or "Tie".
    """
    if user == computer:
        return "Tie", "Tie"
    elif ((user == "Rock" and computer == "Scissors") or
          (user == "Paper" and computer == "Rock") or
          (user == "Scissors" and computer == "Paper")):
        return "Lose", "Win"
    else:
        return "Win", "Lose"


def get_image(choice, result):
    """Returns the image for a choice and result, e.g. "Rock" and "Win"."""
    return images[f"{choice}_{result}"]


def update_score():
    """Shows the current score in the score label."""
    score_label.config(text=f"{user_score} - {computer_score}")


def set_choice_buttons(state):
    """Turns the three choice buttons on ("normal") or off ("disabled")."""
    rock_button.config(state=state)
    paper_button.config(state=state)
    scissors_button.config(state=state)


def new_match():
    """Resets the scores and images so a new match can start."""
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_score()
    user_image_label.config(image=question_image)
    computer_image_label.config(image=question_image)
    result_label.config(text=f"First to {target.get()} wins. Choose a move.")
    set_choice_buttons("normal")
    new_match_button.config(state="disabled")


def play(user_choice):
    """Plays one round, updates the score and checks for a match winner."""
    global user_score, computer_score
    computer_choice = random.choice(CHOICES)
    computer_result, user_result = determine_winner(user_choice,
                                                    computer_choice)
    user_image_label.config(image=get_image(user_choice, user_result))
    computer_image_label.config(image=get_image(computer_choice,
                                                computer_result))
    if user_result == "Win":
        user_score += 1
    elif user_result == "Lose":
        computer_score += 1
    update_score()

    if user_score == target.get():
        result_label.config(text="You win the match!")
    elif computer_score == target.get():
        result_label.config(text="The computer wins the match!")
    else:
        result_label.config(text=RESULT_MESSAGES[user_result])
        return
    # The match is over: stop play until a new match starts
    set_choice_buttons("disabled")
    new_match_button.config(state="normal")


def rock_click():
    play("Rock")


def paper_click():
    play("Paper")


def scissors_click():
    play("Scissors")


# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("520x560")
root.configure(bg=BG_COLOR)

# Load the images (this must happen after the main window is created)
# icons: small pictures for the buttons; images: the 9 game pictures
images = {}
icons = {}
for choice in CHOICES:
    icons[choice] = tk.PhotoImage(
        file=IMAGE_FOLDER / f"{choice.lower()}_icon.png")
    for result in RESULTS:
        file_name = f"{choice.lower()}_{result.lower()}.png"
        images[f"{choice}_{result}"] = tk.PhotoImage(
            file=IMAGE_FOLDER / file_name)
question_image = tk.PhotoImage(file=IMAGE_FOLDER / "question.png")

# The number of wins needed to win the match (1, 3 or 5)
target = tk.IntVar(value=3)

# Create widgets
title_label = tk.Label(root, text="Rock Paper Scissors", bg=BG_COLOR,
                       fg=TEXT_COLOR, font=TITLE_FONT)
# A frame holds the "First to" label and the three radio buttons in one row
match_frame = tk.Frame(root, bg=BG_COLOR)
first_to_label = tk.Label(match_frame, text="First to:", bg=BG_COLOR,
                          fg=TEXT_COLOR, font=FONT_STYLE)
first_to_label.pack(side="left", padx=5)
for wins in MATCH_LENGTHS:
    tk.Radiobutton(match_frame, text=str(wins), variable=target, value=wins,
                   bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_STYLE,
                   command=new_match).pack(side="left", padx=5)
# A button with an image measures its width in pixels, not characters
rock_button = tk.Button(root, text="Rock", image=icons["Rock"],
                        compound="top", width=110, bg=BUTTON_BG_COLOR,
                        fg=BUTTON_FG_COLOR, font=FONT_STYLE,
                        command=rock_click)
paper_button = tk.Button(root, text="Paper", image=icons["Paper"],
                         compound="top", width=110, bg=BUTTON_BG_COLOR,
                         fg=BUTTON_FG_COLOR, font=FONT_STYLE,
                         command=paper_click)
scissors_button = tk.Button(root, text="Scissors", image=icons["Scissors"],
                            compound="top", width=110, bg=BUTTON_BG_COLOR,
                            fg=BUTTON_FG_COLOR, font=FONT_STYLE,
                            command=scissors_click)
you_label = tk.Label(root, text="You", bg=BG_COLOR, fg=TEXT_COLOR,
                     font=FONT_STYLE)
score_label = tk.Label(root, text="0 - 0", bg=BG_COLOR, fg=TEXT_COLOR,
                       font=SCORE_FONT)
computer_label = tk.Label(root, text="Computer", bg=BG_COLOR, fg=TEXT_COLOR,
                          font=FONT_STYLE)
user_image_label = tk.Label(root, image=question_image, bg=BG_COLOR)
vs_label = tk.Label(root, text="vs", bg=BG_COLOR, fg=TEXT_COLOR,
                    font=FONT_STYLE)
computer_image_label = tk.Label(root, image=question_image, bg=BG_COLOR)
result_label = tk.Label(root, text="First to 3 wins. Choose a move.",
                        bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_STYLE)
new_match_button = tk.Button(root, text="New match", bg=BUTTON_BG_COLOR,
                             fg=BUTTON_FG_COLOR, font=FONT_STYLE,
                             state="disabled", command=new_match)

# Share any spare width equally between the 3 columns,
# so the widgets stay centred
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# Place widgets in the window
title_label.grid(row=0, column=0, columnspan=3, pady=(15, 5))
match_frame.grid(row=1, column=0, columnspan=3, pady=5)
rock_button.grid(row=2, column=0, padx=5, pady=10)
paper_button.grid(row=2, column=1, padx=5, pady=10)
scissors_button.grid(row=2, column=2, padx=5, pady=10)
you_label.grid(row=3, column=0)
score_label.grid(row=3, column=1)
computer_label.grid(row=3, column=2)
user_image_label.grid(row=4, column=0, pady=5)
vs_label.grid(row=4, column=1)
computer_image_label.grid(row=4, column=2, pady=5)
result_label.grid(row=5, column=0, columnspan=3, pady=10)
new_match_button.grid(row=6, column=0, columnspan=3)

# Start the main event loop
root.mainloop()
