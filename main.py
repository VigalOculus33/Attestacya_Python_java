import argparse
from note_manager import NoteManager

def main():
    parser = argparse.ArgumentParser(description="Notes management system")
    parser.add_argument("command", choices=['add', 'list', 'edit', 'delete'])
    parser.add_argument("--title")
    parser.add_argument("--message")
    parser.add_argument("--id", type=int)
    args = parser.parse_args()

    manager = NoteManager('notes.json')

    # Реализуйте логику работы с командами и менеджером заметок

if __name__ == "__main__":
    main()