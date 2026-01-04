import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parent
print("Looking for MP3 files in:", BASE)

def mp3_to_mp3(input_path: Path):
    temp_output = input_path.with_suffix(".tmp.mp3")

    cmd = [
        "ffmpeg",
        "-y",
        "-i", str(input_path),
        "-vn",
        "-map", "0:a",
        "-ar", "44100",
        "-ac", "2",
        "-codec:a", "libmp3lame",
        "-b:a", "192k",
        "-f", "mp3",
        str(temp_output)
    ]

    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)

    # Replace original file
    input_path.unlink()          # delete old file, otherwise ffmpeg may not convert the tune but just reuse it
    temp_output.rename(input_path)  # rename new file
    print("Replaced:", input_path.name)

for mp3_file in BASE.glob("*.mp3"):
    print("Converting:", mp3_file.name)
    mp3_to_mp3(mp3_file)

print("All conversions complete.")
