import tkinter as tk
import random

# Dictionary of countries with their capital cities
capitals = {
    "Australia": "Canberra",
    "Canada": "Ottawa",
    "China": "Beijing",
    "France": "Paris",
    "Germany": "Berlin",
    "India": "New Delhi",
    "Italy": "Rome",
    "Japan": "Tokyo",
    "Mexico": "Mexico City",
    "Russia": "Moscow",
    "South Africa": "Pretoria",
    "United Kingdom": "London",
    "United States": "Washington, D.C.",
    "Brazil": "Brasilia",
    "Argentina": "Buenos Aires",
    "Egypt": "Cairo",
    "Nigeria": "Abuja",
    "Kenya": "Nairobi",
    "Saudi Arabia": "Riyadh",
    "South Korea": "Seoul",
}

def on_return_key(event):
    check_answer()

def start_quiz():
    global score, current_country_index
    score = 0
    current_country_index = 0
    feedback_label.config(text="")  # Clear the feedback field
    next_question()

def next_question():
    if current_country_index < len(countries):
        country = countries[current_country_index]
        correct_capital = capitals[country]
        options = [correct_capital]

        # Add three random incorrect options
        while len(options) < 4:
            option = random.choice(list(capitals.values()))
            if option not in options:
                options.append(option)

        random.shuffle(options)

        country_label.config(text=f"What is the capital of {country}?")
        for i, option in enumerate(options):
            buttons[i].config(text=option, command=lambda opt=option: check_answer(opt))

        result_label.config(text="")
    else:
        end_game()

def check_answer(selected_option):
    global score, current_country_index
    correct_capital = capitals[countries[current_country_index]]

    if selected_option == correct_capital:
        result_label.config(text="Correct!", fg="green")
        score += 1
        current_country_index += 1
        root.after(1000, next_question)
    else:
        result_label.config(text=f"Incorrect. The capital of {countries[current_country_index]} is {correct_capital}.", fg="red")
        root.after(2000, end_game)

def end_game():
    if score == len(countries):
        feedback_label.config(
            text=f"Winner! You answered all {score} questions correctly!",
            fg="green")
    else:
        feedback_label.config(
            text=f"You answered {score} questions correctly in a row.",
            fg="blue")
    country_label.config(text="")
    for button in buttons:
        button.config(text="", command=lambda: None)
    result_label.config(text="")

root = tk.Tk()
root.title("Capital Cities Quiz Game")
score = 0
countries = list(capitals.keys())
random.shuffle(countries)
current_country_index = 0

# Set the window size to 600x800 pixels
root.geometry("600x850")

# Make the window resizable
root.resizable(True, True)

welcome_text = "Welcome to the Capital Cities Quiz Game!\n\nRules:\n1. Choose the correct capital city of each country from the options.\n2. If you guess correctly, you will be asked another question.\n3. The game continues until you answer incorrectly or all countries are done.\n4. Your score is the number of consecutive correct answers. Answer all correctly to win!\n\nClick 'Start Quiz' to begin."

label = tk.Label(root, text=welcome_text, wraplength=550, anchor="w", justify="left", font=("Helvetica", 12))
label.pack(pady=20)

start_button = tk.Button(root, text="Start Quiz", command=start_quiz, bg="blue", fg="white", width=20, height=2, font=("Helvetica", 14))
start_button.pack(pady=10)

question_frame = tk.Frame(root, bd=2, relief="solid")
question_frame.pack(pady=10, padx=10, fill="x")

question_label = tk.Label(question_frame, text="Question:", font=("Helvetica", 12))
question_label.pack(anchor="w")

country_label = tk.Label(question_frame, text="", font=("Helvetica", 12))
country_label.pack(pady=10)

buttons = [tk.Button(question_frame, text="", width=20, height=2, font=("Helvetica", 14)) for _ in range(4)]
for button in buttons:
    button.pack(pady=5)

result_label = tk.Label(question_frame, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

feedback_frame = tk.Frame(root, bd=2, relief="solid")
feedback_frame.pack(pady=10, padx=10, fill="x")

feedback_label_title = tk.Label(feedback_frame, text="Game Over Feedback:", font=("Helvetica", 12))
feedback_label_title.pack(anchor="w")

feedback_label = tk.Label(feedback_frame, text="", font=("Helvetica", 12))
feedback_label.pack(pady=10)

root.mainloop()
