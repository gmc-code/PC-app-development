import anvil.server
from anvil.tables import app_tables

# Replace with your Anvil Uplink key
ANVIL_UPLINK_KEY = "server_2LPC4YBQWDFEIMFBEHUGYT6I-LKHZZ6NUK3YOTG4K"

# Connect to the Anvil server
print("Connecting to Anvil...")
anvil.server.connect(ANVIL_UPLINK_KEY)
print("Uplink connected successfully.")  # Confirm connection

@anvil.server.callable
def test_connection():
    return "Uplink is working!"

print(anvil.server.call('test_connection'))  # Test connection

@anvil.server.callable
def add_joke_to_database(joke, reply):
    """
    Adds a joke and its reply to the Anvil database.
    """
    print(f"Attempting to add joke: {joke}, reply: {reply}")
    try:
        app_tables.jokes.add_row(joke=joke, reply=reply)
        print("Joke added successfully.")
    except Exception as e:
        print(f"Error occurred while adding joke: {e}")
        raise

# Test direct database interaction
try:
    app_tables.jokes.add_row(joke="Direct Test Joke", reply="Direct Test Reply")
    print("Direct database test: Row added successfully.")
except Exception as e:
    print(f"Direct database test failed: {e}")

# Call server function to add a joke
try:
    anvil.server.call('add_joke_to_database',
                      "Why did the chicken cross the road?",
                      "To get to the other side.")
    print("Server call: Joke added successfully.")
except Exception as e:
    print(f"Server call failed: {e}")
