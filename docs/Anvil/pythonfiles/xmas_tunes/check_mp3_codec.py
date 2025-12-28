import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parent

def check_codec(path: Path):
    cmd = [
        "ffprobe",
        "-v", "error",
        "-select_streams", "a:0",
        "-show_entries", "stream=codec_name",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(path)
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    codec = result.stdout.strip()

    return codec

print("Checking MP3 codecs in:", BASE)

for mp3 in BASE.glob("*.mp3"):
    codec = check_codec(mp3)

    if codec == "mp3":
        print(f"✔ OK: {mp3.name} — codec={codec}")
    else:
        print(f"❌ ERROR: {mp3.name} — codec={codec} (NOT Layer III!)")
