# ttk Notebook - A complete Notebook app

import tkinter as tk
from tkinter import ttk


def convert():
    try:
        celsius = float(celsius_entry.get())
        result_label.config(text=f"{celsius * 9 / 5 + 32:.1f} °F")
    except ValueError:
        result_label.config(text="Please type a number")


def save_name():
    about_label.config(text="Made by " + name_entry.get())
    notebook.select(about_page)


root = tk.Tk()
root.geometry("320x220")
root.title("Science tools")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Tab 1: converter
convert_page = ttk.Frame(notebook, padding=15)
notebook.add(convert_page, text="Converter")
ttk.Label(convert_page, text="Temperature in °C:").pack()
celsius_entry = ttk.Entry(convert_page, width=10)
celsius_entry.pack(pady=5)
ttk.Button(convert_page, text="Convert", command=convert).pack()
result_label = ttk.Label(convert_page, text="", font=("Arial", 16))
result_label.pack(pady=5)

# Tab 2: settings
settings_page = ttk.Frame(notebook, padding=15)
notebook.add(settings_page, text="Settings")
ttk.Label(settings_page, text="Your name:").pack()
name_entry = ttk.Entry(settings_page)
name_entry.pack(pady=5)
ttk.Button(settings_page, text="Save", command=save_name).pack()

# Tab 3: about
about_page = ttk.Frame(notebook, padding=15)
notebook.add(about_page, text="About")
about_label = ttk.Label(about_page, text="Made by ???", font=("Arial", 14))
about_label.pack(pady=20)

root.mainloop()
