#  pip install anvil-uplink

import anvil.server
import anvil.media
from pathlib import Path

help(anvil.media.from_file)


ANVIL_UPLINK_KEY = "server_VFBM6MHSDYVIEOKYSBPFGWM5-R7KYIKWSQ7RXEGII"

print("Connecting to Anvil...")
anvil.server.connect(ANVIL_UPLINK_KEY)
print("Connected.")

# Folder containing MP3s is the same folder as this script
MP3_FOLDER = Path(__file__).resolve().parent
print("Looking for MP3s in:", MP3_FOLDER)

for mp3_file in MP3_FOLDER.glob("*.mp3"):
    title = mp3_file.stem
    print(f"Processing: {title}")

    # Convert MP3 to Anvil Media
    media = anvil.media.from_file(
        mp3_file,
        mime_type="audio/mpeg",
        name=mp3_file.name
    )

    # Upload to server (overwrite if exists)
    anvil.server.call("add_or_update_tune", title, media)
    print(f"Uploaded/Updated '{title}' successfully.")

print("All MP3 files processed.")
