import tkinter as tk
from tkinter import ttk, messagebox

class AdvancedTextProcessor:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Text Widget Interface")
        self.root.geometry("550x400")

        # Configure overall grid weights for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        self._create_controls()
        self._create_text_area()
        self._setup_tags()
        self._insert_initial_data()

    def _create_controls(self):
        """Creates the search bar and action buttons at the top."""
        control_frame = ttk.Frame(self.root, padding=10)
        control_frame.grid(row=0, column=0, sticky="ew")

        ttk.Label(control_frame, text="Search Term:").pack(side=tk.LEFT, padx=5)

        self.search_entry = ttk.Entry(control_frame, width=15)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.insert(0, "important")

        ttk.Button(control_frame, text="Highlight Match", command=self.search_and_highlight).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Extract Line 2", command=self.get_specific_line).pack(side=tk.LEFT, padx=5)

    def _create_text_area(self):
        """Creates a scrollable text area container using a frame layout."""
        text_frame = ttk.Frame(self.root, padding=10)
        text_frame.grid(row=1, column=0, sticky="nsew")
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(0, weight=1)

        # Create Text widget with undo tracking enabled
        self.text_widget = tk.Text(text_frame, wrap="word", undo=True, maxundo=10, font=("Courier New", 11))
        self.text_widget.grid(row=0, column=0, sticky="nsew")

        # Attach an integrated Scrollbar
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self.text_widget.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.text_widget.configure(yscrollcommand=scrollbar.set)

    def _setup_tags(self):
        """Defines style configurations for specific text regions (Tags)."""
        self.text_widget.tag_configure("header", font=("Courier New", 12, "bold"), foreground="#0d6efd")
        self.text_widget.tag_configure("search_match", background="#fff3cd", foreground="#856404", font=("Courier New", 11, "bold"))
        self.text_widget.tag_configure("widget_zone", background="#e2e8f0")

    def _insert_initial_data(self):
        """Demonstrates advanced inserting using mixed indices, tags, and embedded window elements."""
        # 1. Standard index string additions utilizing tagged regions
        self.text_widget.insert("1.0", "=== SYSTEM METRICS LOG ===\n", "header")
        self.text_widget.insert("2.0", "[10:00 AM] Status: Operational. All nodes stable.\n")
        self.text_widget.insert("3.0", "[10:15 AM] Notice: Run an important diagnostic update soon.\n")
        self.text_widget.insert("4.0", "[10:30 AM] Warning: High memory pressure detected in Node 4.\n")

        # 2. Add structural spacing dynamically using line expressions
        self.text_widget.insert("end", "\nInteract directly with this stream: ")

        # 3. Create and embed a live Tkinter widget inline into the text structure
        inline_btn = ttk.Button(self.text_widget, text="Clear Highlights", command=self.clear_highlights)

        # "end - 1 chars" avoids appending past the trailing newline boundary
        self.text_widget.window_create("end - 1 chars", window=inline_btn)
        self.text_widget.insert("end", "\n\n[End of File]")

    def get_specific_line(self):
        """Retrieves and processes a precise row segment via fractional expressions."""
        # "2.0" to "2.end" safely extracts line 2 without grasping its structural newline
        line2_content = self.text_widget.get("2.0", "2.end")
        messagebox.showinfo("Line 2 Contents", f"Extracted text:\n\n{line2_content}")

    def search_and_highlight(self):
        """Uses programmatic string matching across the entire lines map matrix."""
        self.clear_highlights()
        search_query = self.search_entry.get()
        if not search_query:
            return

        start_index = "1.0"
        while True:
            # Perform a coordinate-based index lookup within the string matrix
            match_index = self.text_widget.search(search_query, start_index, stopindex="end", nocase=True)
            if not match_index:
                break

            # Compute exact end offset based on matching characters
            end_index = f"{match_index} + {len(search_query)} chars"

            # Layer the visual highlight configuration tag onto the index range
            self.text_widget.tag_add("search_match", match_index, end_index)

            # Advance pointer past current match loop sequence
            start_index = end_index

    def clear_highlights(self):
        """Removes the specific tag styling from all text regions."""
        self.text_widget.tag_remove("search_match", "1.0", "end")


if __name__ == "__main__":
    app_root = tk.Tk()
    app = AdvancedTextProcessor(app_root)
    app_root.mainloop()
