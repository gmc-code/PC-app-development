import tkinter as tk
import random

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
    "South Melbourne": 3,
}

class QuizGame:

    def __init__(self, root):
        self.root = root
        self.window.title("AFL Premiership Quiz Game")
        self.score = 0
        self.teams = list(premiers.keys())
        random.shuffle(self.teams)
        self.current_team_index = 0

        # Set the window size to 600x800 pixels
        self.window.geometry("600x800")

        # Make the window resizable
        self.window.resizable(True, True)

        # Long text stored in a variable
        welcome_text = (
            "Welcome to the AFL Premiership Quiz Game!\n\n"
            "Rules:\n"
            "1. Guess the number of premierships won by each team.\n"
            "2. If you guess correctly, you will be asked another question.\n"
            "3. The game continues until you answer incorrectly or all teams are done.\n"
            "4. Your score is the number of consecutive correct answers. Answer all correctly to win!\n\n"
            "Click 'Start Quiz' to begin."
        )

        self.label = tk.Label(
            root,
            text=welcome_text,
            wraplength=550,
            anchor="w",
            justify="left",
            font=("Helvetica", 14),
        )
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz, bg="blue", fg="white", width=20, height=2, font=("Helvetica", 14))
        self.start_button.pack(pady=10)

        self.question_frame = tk.Frame(root, bd=2, relief="solid")
        self.question_frame.pack(pady=10, padx=10, fill="x")

        self.question_label = tk.Label(self.question_frame, text="Question:", font=("Helvetica", 14))
        self.question_label.pack(anchor="w")

        self.team_label = tk.Label(self.question_frame, text="", font=("Helvetica", 16))
        self.team_label.pack(pady=10)

        self.entry = tk.Entry(self.question_frame, width=5, font=("Helvetica", 16), justify="center")
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.on_return_key)

        self.submit_button = tk.Button(self.question_frame, text="Submit", command=self.check_answer, bg="lime green", fg="white", width=20, height=2, font=("Helvetica", 14))
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(self.question_frame, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        self.feedback_frame = tk.Frame(root, bd=2, relief="solid")
        self.feedback_frame.pack(pady=10, padx=10, fill="x")

        self.feedback_label_title = tk.Label(self.feedback_frame, text="Game Over Feedback:", font=("Helvetica", 14))
        self.feedback_label_title.pack(anchor="w")

        self.feedback_label = tk.Label(self.feedback_frame, text="", font=("Helvetica", 14))
        self.feedback_label.pack(pady=10)

    def on_return_key(self, event):
        self.check_answer()

    def start_quiz(self):
        self.score = 0
        self.current_team_index = 0
        self.feedback_label.config(text="")  # Clear the feedback field
        self.next_question()

    def next_question(self):
        if self.current_team_index < len(self.teams):
            self.team_label.config(text=f"How many premierships has {self.teams[self.current_team_index]} won?")
            self.entry.delete(0, tk.END)
            self.entry.focus()  # Set focus to the entry field
            self.result_label.config(text="")
        else:
            self.end_game()

    def check_answer(self):
        user_guess = self.entry.get().strip()
        correct_premierships = premiers[self.teams[self.current_team_index]]

        if user_guess.isdigit() and int(user_guess) == correct_premierships:
            self.result_label.config(text="Correct!", fg="green")
            self.score += 1
            self.current_team_index += 1
            self.window.after(1000, self.next_question)
        else:
            self.result_label.config(text=f"Incorrect. {self.teams[self.current_team_index]} has won {correct_premierships} premierships.", fg="red")
            self.window.after(2000, self.end_game)

    def end_game(self):
        if self.score == len(self.teams):
            self.feedback_label.config(text=f"Congratulations! You answered all {self.score} questions correctly and are a winner!", fg="green")
        else:
            self.feedback_label.config(text=f"You answered {self.score} questions correctly in a row.", fg="blue")
        self.team_label.config(text="")
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    window.mainloop()
