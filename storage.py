import json

def load_notes(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(filename, notes):
    with open(filename, 'w') as file:
        json.dump(notes, file, indent=4)