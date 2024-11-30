import tkinter as tk


def on_validate(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    output_text.set(
        f"Action: {action}\n"
        f"Index: {index}\n"
        f"Value if allowed: {value_if_allowed}\n"
        f"Prior value: {prior_value}\n"
        f"Text: {text}\n"
        f"Validation type: {validation_type}\n"
        f"Trigger type: {trigger_type}\n"
        f"Widget name: {widget_name}"
    )
    return True


window = tk.Tk()
window.title("Validation Example")
window.geometry("500x350")

output_text = tk.StringVar()
output_label = tk.Label(window, font=("Arial",16), textvariable=output_text, justify="left")
output_label.pack(pady=10)

entry_var = tk.StringVar()
entry_field = tk.Entry(window, font=("Arial",24), textvariable=entry_var, validate="key", validatecommand=(window.register(on_validate), "%d", "%i", "%P", "%s", "%S", "%v", "%V", "%W"))
entry_field.pack(pady=10)


window.mainloop()
