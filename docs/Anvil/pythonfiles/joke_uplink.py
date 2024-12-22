# Connect to your Anvil app

import anvil.server
import csv
from anvil.tables import app_tables

# Replace with your Anvil Uplink key
ANVIL_UPLINK_KEY = "server_2LPC4YBQWDFEIMFBEHUGYT6I-LKHZZ6NUK3YOTG4K"

# Connect to the Anvil server

anvil.server.connect(ANVIL_UPLINK_KEY)
print("Uplink connected successfully.")  # Confirm connection


@anvil.server.callable
def add_joke_to_database(joke, reply):
    """
    Adds a joke and its reply to the Anvil database.
    """
    app_tables.jokes.add_row(joke=joke, reply=reply)



def read_jokes_from_file(file_path):
    """
    Reads jokes and replies from a tab-delimited file and returns them as a list of tuples.
    """
    jokes = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if len(row) >= 2:  # Ensure the row has at least 2 columns
                jokes.append((row[0], row[1]))
    return jokes

def upload_jokes(file_path):
    """
    Reads jokes from a file and uploads them to the Anvil database.
    """
    jokes = read_jokes_from_file(file_path)
    for joke, reply in jokes:
        anvil.server.call('add_joke_to_database', joke, reply)
        print(f"Uploaded joke: {joke}")

# Specify the path to your tab-delimited text file
file_path = 'docs/Anvil/pythonfiles/christmas_jokes.txt'

# Upload jokes to the database
upload_jokes(file_path)

# # Disconnect from the Anvil server
# anvil.server.disconnect()
