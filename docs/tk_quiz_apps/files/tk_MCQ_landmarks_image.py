import tkinter as tk
from PIL import Image, ImageTk
import random
from pathlib import Path

# --------------------------------------------------
# Quiz configuration
# --------------------------------------------------
datatype_question = "Landmark"
datatype_questions = "Landmarks"
datatype_answer = "City"

quiz_data = quiz_data = {
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


# Image directory (pathlib)
IMAGE_DIR = Path("docs/tk_quiz_apps/files/landmark_images")


# --------------------------------------------------
# Quiz logic
# --------------------------------------------------
def on_return_key(event):
    check_answer()


def start_quiz():
    global score, current_question_index, questions
    score = 0
    current_question_index = 0
    feedback_label.config(text="")
    questions = list(quiz_data.keys())
    random.shuffle(questions)
    next_question()


def next_question():
    if current_question_index < len(questions):
        question = questions[current_question_index]
        correct_answer = answers[question]
        options = [correct_answer]

        while len(options) < 4:
            option = random.choice(list(answers.values()))
            if option not in options:
                options.append(option)

        random.shuffle(options)

        question_label.config(text=f"Question {current_question_index + 1} of {len(questions)}")
        question_text.config(text=f"What {datatype_answer} is the {question} located in?")

        for i, option in enumerate(options):
            buttons[i].config(text=option, command=lambda opt=option: check_answer(opt))

        load_image(question)
        result_label.config(text="")
    else:
        end_game()


def load_image(question):
    image_path = IMAGE_DIR / f"{question}.jpg"

    if image_path.exists():
        img = Image.open(image_path)

        if img.width > 350:
            img = img.resize((350, int(img.height * (350 / img.width))), Image.LANCZOS)

        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img
    else:
        image_label.config(image="")
        image_label.image = None


def check_answer(selected_option):
    global score, current_question_index
    correct_answer = answers[questions[current_question_index]]

    if selected_option == correct_answer:
        result_label.config(text="Correct!", fg="green")
        score += 1
        current_question_index += 1
        root.after(1000, next_question)
    else:
        result_label.config(text=f"Incorrect. The {questions[current_question_index]} " f"is located in {correct_answer}.", fg="red")
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


# --------------------------------------------------
# UI setup
# --------------------------------------------------
root = tk.Tk()
root.title(f"{datatype_questions} Quiz Game")

score = 0
answers = quiz_data
questions = list(quiz_data.keys())
random.shuffle(questions)
current_question_index = 0

root.geometry("1000x800")
# Make the window not resizable
root.resizable(False, False)
# Center the window
center_window(root)

welcome_text = (
    f"Welcome to the {datatype_questions} Quiz Game!\n\n" "Rules:\n" f"1. Choose the correct {datatype_answer} for each {datatype_question}.\n" "2. Correct answers continue the game.\n" "3. One wrong answer ends the game.\n" "4. Answer all correctly to win!\n\n" "Click 'Start Quiz' to begin."
)

label = tk.Label(root, text=welcome_text, wraplength=600, anchor="w", justify="left", font=("Helvetica", 12))
label.grid(row=0, column=0, columnspan=2, pady=10, padx=20, sticky="w")

start_button = tk.Button(root, text="Start Quiz", command=start_quiz, bg="blue", fg="white", width=20, height=2, font=("Helvetica", 14))
start_button.grid(row=1, column=0, columnspan=2, pady=10)

parent_frame = tk.Frame(root)
parent_frame.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)

# Image frame
image_frame = tk.Frame(parent_frame, width=400, bd=2, relief="solid")
image_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

image_label = tk.Label(image_frame, width=390)
image_label.grid(padx=10, pady=10)

# Question frame
question_frame = tk.Frame(parent_frame, bd=2, relief="solid")
question_frame.grid(row=0, column=1, sticky="nsew")

question_label = tk.Label(question_frame, font=("Helvetica", 12))
question_label.grid(row=0, column=0, pady=5, padx=20, sticky="w")

question_text = tk.Label(question_frame, font=("Helvetica", 12), wraplength=400, justify="left", width=60, anchor="w")  # ← left-align text within the label
question_text.grid(row=1, column=0, pady=10, padx=20, sticky="w")

buttons = []
option_labels = ["A", "B", "C", "D"]
pastel_colors = ["#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9"]

for i in range(4):
    frame = tk.Frame(question_frame)
    frame.grid(row=2 + i, column=0, pady=5, sticky="w")

    tk.Label(frame, text=option_labels[i], font=("Helvetica", 14)).grid(row=0, column=0, padx=20)

    button = tk.Button(frame, text="", width=20, height=2, font=("Helvetica", 14), bg=pastel_colors[i])
    button.grid(row=0, column=1)
    buttons.append(button)

result_label = tk.Label(question_frame, font=("Helvetica", 12))
result_label.grid(row=6, column=0, pady=10)

feedback_frame = tk.Frame(root, bd=2, relief="solid")
feedback_frame.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

tk.Label(feedback_frame, text="Game Over Feedback:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w")

feedback_label = tk.Label(feedback_frame, font=("Helvetica", 12))
feedback_label.grid(row=1, column=0, pady=10)

root.bind("<Key>", handle_key)
root.mainloop()
