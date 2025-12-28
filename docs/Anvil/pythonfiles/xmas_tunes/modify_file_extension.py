from pathlib import Path

# Get the folder where THIS script is located
folder = Path(__file__).parent

for file in folder.iterdir():
    if file.suffix.lower() == ".2mp3":
        new_file = file.with_suffix(".mp3")
        print(f"Renaming: {file.name} → {new_file.name}")
        file.rename(new_file)

print("Done.")
