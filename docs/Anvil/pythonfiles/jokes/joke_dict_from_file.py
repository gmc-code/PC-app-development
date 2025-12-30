from pathlib import Path
import pprint
import json


currfile_dir = Path(__file__).parent
file_path = currfile_dir / "christmas_jokes.txt"
json_file_path = currfile_dir / "christmas_jokes.json"

# Function to convert tab-delimited text file to dictionary with numeric keys
def convert_to_dict(file_path):
    joke_reply_dict = {}
    with open(file_path, 'r') as file:
        for index, line in enumerate(file, start=1):
            joke, reply = line.strip().split('\t')
            joke_reply_dict[index] = {'joke': joke, 'reply': reply}
    return joke_reply_dict

joke_reply_dict = convert_to_dict(file_path)

# Pretty-print the resulting dictionary
pprint.pprint(joke_reply_dict)

# Dump the dictionary to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(joke_reply_dict, json_file, indent=4)

print(f"Dictionary has been dumped to {json_file_path}")
