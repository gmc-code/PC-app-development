# Science Glossary - a Tkinter app that modifies a dictionary
# Keys are science words, values are their meanings.

import tkinter as tk

# The dictionary we will change while the app runs
glossary = {
    "atom": "The smallest particle of an element",
    "cell": "The basic unit of all living things",
    "force": "A push or a pull",
}


def show_glossary():
    """Rebuild the text in the display label from the dictionary."""
    text = ""
    for word in sorted(glossary):
        text = text + word + ": " + glossary[word] + "\n"
    display_label.config(text=text)


def add_word():
    """Add a new word, or change the meaning of an existing word."""
    word = word_entry.get().strip().lower()
    meaning = meaning_entry.get().strip()

    if word == "" or meaning == "":
        message_label.config(text="Type a word and a meaning first.")
        return

    if word in glossary:
        message_label.config(text="Updated the meaning of '" + word + "'.")
    else:
        message_label.config(text="Added '" + word + "' to the glossary.")

    glossary[word] = meaning      # add a new key OR change an existing value
    show_glossary()


def delete_word():
    """Remove a word from the dictionary."""
    word = word_entry.get().strip().lower()

    if word in glossary:
        del glossary[word]
        message_label.config(text="Deleted '" + word + "'.")
        show_glossary()
    else:
        message_label.config(text="'" + word + "' is not in the glossary.")


def look_up_word():
    """Find a word and put its meaning in the meaning box."""
    word = word_entry.get().strip().lower()

    if word in glossary:
        meaning_entry.delete(0, tk.END)
        meaning_entry.insert(0, glossary[word])
        message_label.config(text="Found '" + word + "'.")
    else:
        message_label.config(text="'" + word + "' is not in the glossary.")


# ---------- Build the window ----------
window = tk.Tk()
window.title("Science Glossary")
window.geometry("460x420")

tk.Label(window, text="Word:").pack()
word_entry = tk.Entry(window, width=30)
word_entry.pack()

tk.Label(window, text="Meaning:").pack()
meaning_entry = tk.Entry(window, width=50)
meaning_entry.pack()

tk.Button(window, text="Add / Update", command=add_word).pack(pady=2)
tk.Button(window, text="Look up", command=look_up_word).pack(pady=2)
tk.Button(window, text="Delete", command=delete_word).pack(pady=2)

message_label = tk.Label(window, text="", fg="blue")
message_label.pack(pady=5)

display_label = tk.Label(window, text="", justify="left", wraplength=420)
display_label.pack(pady=5)

show_glossary()     # show the starting dictionary

window.mainloop()
