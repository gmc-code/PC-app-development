import tkinter as tk
import random

# General dictionary for the quiz

datatype_question = "Landmark"
datatype_questions = "Landmarks"
datatype_answer = "City"
quiz_data = {
    "Acropolis": "Athens",
    "Alhambra": "Granada",
    "Al-Khazneh": "Petra",
    "Angkor Wat": "Siem Reap",
    "Arc de Triomphe": "Paris",
    "Big Ben": "London",
    "Brandenburg Gate": "Berlin",
    "Buckingham Palace": "London",
    "Burj Khalifa": "Dubai",
    "Christ the Redeemer": "Rio de Janeiro",
    "Colosseum": "Rome",
    "Eiffel Tower": "Paris",
    "Empire State Building": "New York",
    "Forbidden City": "Beijing",
    "Golden Gate Bridge": "San Francisco",
    "Guggenheim Museum": "New York",
    "Hagia Sophia": "Istanbul",
    "Kremlin": "Moscow",
    "Leaning Tower of Pisa": "Pisa",
    "Louvre Museum": "Paris",
    "Mount Rushmore": "Keystone",
    "Notre-Dame Cathedral": "Paris",
    "Palace of Westminster": "London",
    "Petronas Towers": "Kuala Lumpur",
    "Pyramid of El Castillo": "Chichen Itza",
    "Pyramids of Giza": "Cairo",
    "Red Square": "Moscow",
    "Sistine Chapel": "Vatican City",
    "St. Basil's Cathedral": "Moscow",
    "St. Peter's Basilica": "Vatican City",
    "Statue of Liberty": "New York",
    "Stonehenge": "Wiltshire",
    "Sydney Opera House": "Sydney",
    "Taj Mahal": "Agra",
    "Times Square": "New York",
}


def on_return_key(event):
    check_answer()


def start_quiz():
    global score, current_question_index, questions
    score = 0
    current_question_index = 0
    feedback_label.config(text="")  # Clear the feedback field
    questions = list(quiz_data.keys())
    random.shuffle(questions)  # Randomize the questions each time the quiz starts
    next_question()


def next_question():
    if current_question_index < len(questions):
        question = questions[current_question_index]
        correct_answer = answers[question]
        options = [correct_answer]

        # Add three random incorrect options
        while len(options) < 4:
            option = random.choice(list(answers.values()))
            if option not in options:
                options.append(option)

        random.shuffle(options)

        question_label.config(text=f"Question {current_question_index + 1} of {len(questions)}")
        question_text.config(text=f"What {datatype_answer} is the {question} located in?")
        for i, option in enumerate(options):
            buttons[i].config(text=option, command=lambda opt=option: check_answer(opt))

        result_label.config(text="")
    else:
        end_game()


def check_answer(selected_option):
    global score, current_question_index
    correct_answer = answers[questions[current_question_index]]

    if selected_option == correct_answer:
        result_label.config(text="Correct!", fg="green")
        score += 1
        current_question_index += 1
        root.after(1000, next_question)
    else:
        result_label.config(text=f"Incorrect. The {questions[current_question_index]} is located in {correct_answer}.", fg="red")
        root.after(2000, end_game)


def end_game():
    if score == len(questions):
        feedback_label.config(text=f"Winner! You answered all {score} questions correctly!", fg="green")
    else:
        feedback_label.config(text=f"You answered {score} questions correctly in a row.", fg="blue")
    question_text.config(text="")
    for button in buttons:
        button.config(text="", command=lambda: None)
    result_label.config(text="")


def handle_key(event):
    keys = ["a", "b", "c", "d", "1", "2", "3", "4"]
    if event.char in keys:
        if event.char in "abcd":
            index = "abcd".index(event.char)
        else:
            index = "1234".index(event.char)

        if index < len(buttons):
            buttons[index].invoke()


# --------------------------------------------------
# UI helpers
# --------------------------------------------------
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    y = y if y < 50 else 30
    window.geometry(f"{width}x{height}+{x}+{y}")


root = tk.Tk()
# Make the window not resizable
root.resizable(False, False)
# Center the window
center_window(root)

root.title(f"{datatype_questions} Quiz Game")
score = 0
answers = quiz_data
questions = list(quiz_data.keys())
random.shuffle(questions)
current_question_index = 0

# Set the window size
root.geometry("700x800")

# Make the window resizable
root.resizable(True, True)

# Center the window
center_window(root)

welcome_text = f"Welcome to the {datatype_questions} Quiz Game!\n\nRules:\n1. Choose (click or type letter) the correct {datatype_answer} for each {datatype_question} from the options.\n2. If you choose correctly, you will be asked another question.\n3. The game continues until you answer incorrectly or all questions are done.\n4. Your score is the number of consecutive correct answers. Answer all correctly to win!\n\nClick 'Start Quiz' to begin."

label = tk.Label(root, text=welcome_text, wraplength=600, anchor="w", justify="left", font=("Helvetica", 12))
label.pack(pady=10)

start_button = tk.Button(root, text="Start Quiz", command=start_quiz, bg="blue", fg="white", width=20, height=2, font=("Helvetica", 14))
start_button.pack(pady=10)

question_frame = tk.Frame(root, bd=2, relief="solid")
question_frame.pack(pady=10, padx=10, fill="x")

question_label = tk.Label(question_frame, text="Question:", font=("Helvetica", 12))
question_label.pack(pady=5, padx=20, anchor="w")

question_text = tk.Label(question_frame, text="", font=("Helvetica", 12))
question_text.pack(pady=10, padx=20, anchor="w")

# Labels for A, B, C, D
option_labels = ["A", "B", "C", "D"]
buttons = []
pastel_colors = ["#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF"]  # Light pastel colors
for i in range(4):
    frame = tk.Frame(question_frame)
    frame.pack(pady=5, anchor="w")
    label = tk.Label(frame, text=option_labels[i], font=("Helvetica", 14))
    label.pack(side="left", padx=20)
    button = tk.Button(frame, text="", width=20, height=2, font=("Helvetica", 14), bg=pastel_colors[i % len(pastel_colors)])
    button.pack(side="left")
    buttons.append(button)

result_label = tk.Label(question_frame, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

feedback_frame = tk.Frame(root, bd=2, relief="solid")
feedback_frame.pack(pady=10, padx=10, fill="x")

feedback_label_title = tk.Label(feedback_frame, text="Game Over Feedback:", font=("Helvetica", 12))
feedback_label_title.pack(anchor="w")

feedback_label = tk.Label(feedback_frame, text="", font=("Helvetica", 12))
feedback_label.pack(pady=10)

root.bind("<Key>", handle_key)

root.mainloop()
