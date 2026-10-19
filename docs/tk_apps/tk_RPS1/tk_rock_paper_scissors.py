import tkinter as tk
import random

# Constants
BG_COLOR = "#ffffff"
TEXT_COLOR = "#333333"
BUTTON_BG_COLOR = "#6750a4"  # purple
BUTTON_FG_COLOR = "#ffffff"
WIN_COLOR = "#4caf50"  # green
LOSE_COLOR = "#f44336"  # red
TIE_COLOR = "#9e9e9e"  # grey
TITLE_FONT = ("Arial", 26, "bold")
FONT_STYLE = ("Arial", 16)
CHOICE_FONT = ("Arial", 20, "bold")

# Game data
CHOICES = ["Rock", "Paper", "Scissors"]
RESULT_COLORS = {"Win": WIN_COLOR, "Lose": LOSE_COLOR, "Tie": TIE_COLOR}
RESULT_MESSAGES = {"Win": "You win!", "Lose": "You lose!",
                   "Tie": "It's a tie!"}


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


def play(user_choice):
    """Plays one round against a random computer choice and shows it."""
    computer_choice = random.choice(CHOICES)
    computer_result, user_result = determine_winner(user_choice,
                                                    computer_choice)
    user_choice_label.config(text=user_choice,
                             bg=RESULT_COLORS[user_result])
    computer_choice_label.config(text=computer_choice,
                                 bg=RESULT_COLORS[computer_result])
    result_label.config(text=RESULT_MESSAGES[user_result])


def rock_click():
    play("Rock")


def paper_click():
    play("Paper")


def scissors_click():
    play("Scissors")


# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("520x320")
root.configure(bg=BG_COLOR)

# Create widgets
title_label = tk.Label(root, text="Rock Paper Scissors", bg=BG_COLOR,
                       fg=TEXT_COLOR, font=TITLE_FONT)
rock_button = tk.Button(root, text="Rock", width=9, bg=BUTTON_BG_COLOR,
                        fg=BUTTON_FG_COLOR, font=FONT_STYLE,
                        command=rock_click)
paper_button = tk.Button(root, text="Paper", width=9, bg=BUTTON_BG_COLOR,
                         fg=BUTTON_FG_COLOR, font=FONT_STYLE,
                         command=paper_click)
scissors_button = tk.Button(root, text="Scissors", width=9, bg=BUTTON_BG_COLOR,
                            fg=BUTTON_FG_COLOR, font=FONT_STYLE,
                            command=scissors_click)
you_label = tk.Label(root, text="You", bg=BG_COLOR, fg=TEXT_COLOR,
                     font=FONT_STYLE)
computer_label = tk.Label(root, text="Computer", bg=BG_COLOR, fg=TEXT_COLOR,
                          font=FONT_STYLE)
# width and height of a Label are measured in characters and text rows
user_choice_label = tk.Label(root, text="?", width=9, height=2, bg=TIE_COLOR,
                             fg=BUTTON_FG_COLOR, font=CHOICE_FONT)
vs_label = tk.Label(root, text="vs", bg=BG_COLOR, fg=TEXT_COLOR,
                    font=FONT_STYLE)
computer_choice_label = tk.Label(root, text="?", width=9, height=2,
                                 bg=TIE_COLOR, fg=BUTTON_FG_COLOR,
                                 font=CHOICE_FONT)
result_label = tk.Label(root, text="Choose rock, paper or scissors.",
                        bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_STYLE)

# Share any spare width equally between the 3 columns,
# so the widgets stay centred
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# Place widgets in the window
title_label.grid(row=0, column=0, columnspan=3, pady=(15, 10))
rock_button.grid(row=1, column=0, padx=5, pady=10)
paper_button.grid(row=1, column=1, padx=5, pady=10)
scissors_button.grid(row=1, column=2, padx=5, pady=10)
you_label.grid(row=2, column=0)
computer_label.grid(row=2, column=2)
user_choice_label.grid(row=3, column=0, pady=5)
vs_label.grid(row=3, column=1)
computer_choice_label.grid(row=3, column=2, pady=5)
result_label.grid(row=4, column=0, columnspan=3, pady=15)

# Start the main event loop
root.mainloop()
