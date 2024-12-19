import tkinter as tk
from PIL import Image, ImageTk
import random
import os

# General dictionary for the quiz
datatype_question = "Landmark"
datatype_questions = "Landmarks"
datatype_answer = "City"
quiz_data = {"Acropolis": "Athens", "Alhambra": "Granada", "Al-Khazneh": "Petra", "Angkor Wat": "Siem Reap", "Arc de Triomphe": "Paris"}


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

        load_image(question)

        result_label.config(text="")
    else:
        end_game()


def load_image(question):
    image_path = os.path.join("docs/tk_apps/files/landmark_images", f"{question}.jpg")
    if os.path.exists(image_path):
        img = Image.open(image_path)
        # Check if the image width is greater than 350 pixels
        if img.width > 350:
            img = img.resize((350, int(img.height * (350 / img.width))), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img  # Keep a reference to avoid garbage collection


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


# Center the window on the screen
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    y = y if y < 50 else 30
    window.geometry(f"{width}x{height}+{x}+{y}")


root = tk.Tk()
root.title(f"{datatype_questions} Quiz Game")
score = 0
answers = quiz_data
questions = list(quiz_data.keys())
random.shuffle(questions)
current_question_index = 0

# Set the window size
root.geometry("1000x800")

# Make the window resizable
root.resizable(True, True)

# Center the window
center_window(root)

welcome_text = f"Welcome to the {datatype_questions} Quiz Game!\n\nRules:\n1. Choose (click or type letter) the correct {datatype_answer} for each {datatype_question} from the options.\n2. If you choose correctly, you will be asked another question.\n3. The game continues until you answer incorrectly or all questions are done.\n4. Your score is the number of consecutive correct answers. Answer all correctly to win!\n\nClick 'Start Quiz' to begin."

label = tk.Label(root, text=welcome_text, wraplength=600, anchor="w", justify="left", font=("Helvetica", 12))
label.grid(row=0, column=0, columnspan=2, pady=10)

start_button = tk.Button(root, text="Start Quiz", command=start_quiz, bg="blue", fg="white", width=20, height=2, font=("Helvetica", 14))
start_button.grid(row=1, column=0, columnspan=2, pady=10)

# Question frame and image frame in a parent frame
# parent frame will expand to fill window
parent_frame = tk.Frame(root)
parent_frame.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

# Configure grid weights
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=2)

# Image frame
image_frame = tk.Frame(parent_frame, width=400, bd=2, relief="solid")
image_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

# Add image label to display the pictures
image_label = tk.Label(image_frame, width=390)
image_label.grid(padx=10, pady=10)

# Question frame
question_frame = tk.Frame(parent_frame, bd=2, relief="solid")
question_frame.grid(row=0, column=1, padx=(0, 10), sticky="nsew")

question_label = tk.Label(question_frame, text="Question:", font=("Helvetica", 12))
question_label.grid(row=0, column=0, sticky="w", pady=5)

question_text = tk.Label(question_frame, text="", font=("Helvetica", 12), wraplength=400, justify="left", width=60)
question_text.grid(row=1, column=0, pady=10)

# Labels for A, B, C, D
option_labels = ["A", "B", "C", "D"]
buttons = []
pastel_colors = ["#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF"]  # Light pastel colors
for i in range(4):
    frame = tk.Frame(question_frame)
    frame.grid(row=2 + i, column=0, pady=5, sticky="w")
    label = tk.Label(frame, text=option_labels[i], font=("Helvetica", 14))
    label.grid(row=0, column=0, padx=20)
    button = tk.Button(frame, text="", width=20, height=2, font=("Helvetica", 14), bg=pastel_colors[i % len(pastel_colors)])
    button.grid(row=0, column=1)
    buttons.append(button)

result_label = tk.Label(question_frame, text="", font=("Helvetica", 12))
result_label.grid(row=6, column=0, pady=10)

feedback_frame = tk.Frame(root, bd=2, relief="solid")
feedback_frame.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

feedback_label_title = tk.Label(feedback_frame, text="Game Over Feedback:", font=("Helvetica", 12))
feedback_label_title.grid(row=0, column=0, sticky="w")

feedback_label = tk.Label(feedback_frame, text="", font=("Helvetica", 12))
feedback_label.grid(row=1, column=0, pady=10)

root.bind("<Key>", handle_key)

root.mainloop()
