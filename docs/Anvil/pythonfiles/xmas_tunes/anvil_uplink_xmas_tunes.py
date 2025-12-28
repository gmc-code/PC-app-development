#  pip install anvil-uplink
# pip install anvil-uplink

import anvil.server
import anvil.media
from pathlib import Path

# for classic anvil version
# ANVIL_UPLINK_KEY = "server_4Z52IC63RNKV77COBWA4MHMW-W6XJSJDF2JX2UXWE"

ANVIL_UPLINK_KEY = "server_VFBM6MHSDYVIEOKYSBPFGWM5-R7KYIKWSQ7RXEGII"
# Connect to Anvil
print("Connecting to Anvil...")
anvil.server.connect(ANVIL_UPLINK_KEY)
print("Connected.")

# Folder containing MP3s is the same folder as this script
MP3_FOLDER = Path(__file__).resolve().parent
print("Looking for MP3s in:", MP3_FOLDER)

for mp3_file in MP3_FOLDER.glob("*.mp3"):
    title = mp3_file.stem
    print(f"Processing: {title}")

    media = anvil.media.from_file(
        mp3_file,
        mime_type="audio/mpeg",
        name=mp3_file.name
    )


    anvil.server.call("add_tune", title, media)
    print(f"Uploaded '{title}' successfully.")


print("All MP3 files processed.")
