import tkinter as tk
from tkinter import ttk


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # root window
        self.title('Theme Demo')
        self.geometry('400x400+200+200')
        self.style = ttk.Style(self)

        # label
        label = ttk.Label(self, text='Name:')
        label.grid(column=0, row=0, padx=10, pady=10, sticky='w')

        # entry
        self.textbox = ttk.Entry(self)
        self.textbox.grid(column=1, row=0, padx=10, pady=10, sticky='w')
        self.textbox.bind('<Return>', self.show_theme)  # Bind Enter key
        # When you bind an event (such as pressing the Enter key) to a method, the method is called with an event object as an argument.

        # button
        btn = ttk.Button(self, text='Show', command=self.show_theme)
        btn.grid(column=2, row=0, padx=10, pady=10, sticky='w')

        # radio button
        self.selected_theme = tk.StringVar()
        theme_frame = ttk.LabelFrame(self, text='Themes')
        theme_frame.grid(padx=10, pady=10, ipadx=20, ipady=20, sticky='w')

        for theme_name in self.style.theme_names():
            rb = ttk.Radiobutton(theme_frame,
                                 text=theme_name,
                                 value=theme_name,
                                 variable=self.selected_theme,
                                 command=self.change_theme)
            rb.pack(expand=True, fill='both')

    def change_theme(self):
        curr_theme = self.selected_theme.get()
        self.style.theme_use(curr_theme)
        self.textbox.delete(0, "end")
        self.textbox.insert(0, curr_theme)

    def show_theme(self, event=None):  # Add event parameter
        curr_theme = self.textbox.get()  # Get the theme name from the entry
        self.selected_theme.set(curr_theme)  # Set the selected theme
        self.style.theme_use(curr_theme)  # Apply the theme

app = App()
app.mainloop()
