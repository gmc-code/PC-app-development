import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parent

def check_codec(path: Path):
    """
    Uses ffprobe to check the audio codec, sample rate, and channels.
    Returns a dict with codec info.
    """
    cmd = [
        "ffprobe",
        "-v", "error",
        "-select_streams", "a:0",
        "-show_entries", "stream=codec_name,sample_rate,channels",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(path)
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    lines = result.stdout.strip().splitlines()

    if len(lines) >= 3:
        codec, sample_rate, channels = lines[:3]
        return {
            "codec": codec,
            "sample_rate": int(sample_rate),
            "channels": int(channels)
        }
    elif lines:
        return {"codec": lines[0]}
    else:
        return {"codec": "unknown"}

print("Checking MP3 files in:", BASE)

for mp3 in BASE.glob("*.mp3"):
    info = check_codec(mp3)
    codec = info.get("codec", "unknown")
    sample_rate = info.get("sample_rate", "N/A")
    channels = info.get("channels", "N/A")

    # Chrome-compatible check
    if codec.lower() in ("mp3", "mp3float", "libmp3lame") and sample_rate == 44100:
        print(f"✔ OK: {mp3.name} — codec={codec}, {sample_rate}Hz, {channels}ch")
    else:
        print(f"❌ WARNING: {mp3.name} — codec={codec}, {sample_rate}Hz, {channels}ch (May not play in Chrome!)")
