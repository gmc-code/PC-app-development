from pathlib import Path
import json

def convert_txt_to_json(input_path: str, output_path: str):
    """
    Convert a tab-separated text file of jokes into JSON.

    Args:
        input_path (str): Full path to the input text file.
        output_path (str): Full path to the output JSON file.
    """
    in_file = Path(input_path)
    out_file = Path(output_path)

    # Read lines from the text file
    with in_file.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    jokes = []
    for line in lines:
        parts = line.strip().split("\t")
        if len(parts) == 2:
            q, a = parts
            jokes.append({"question": q, "answer": a})

    # Write JSON output
    with out_file.open("w", encoding="utf-8") as f:
        json.dump(jokes, f, indent=2, ensure_ascii=False)

    print(f"Converted {in_file} → {out_file}")


input_path = r"C:\Users\gmccarthy\Documents\PC_RTD_GITHUB_resources\PC-app-development\docs\pyscript\files\christmas_jokes.txt"
output_path = r"C:\Users\gmccarthy\Documents\PC_RTD_GITHUB_resources\PC-app-development\docs\pyscript\files\christmas_jokes.json"

convert_txt_to_json(input_path, output_path)