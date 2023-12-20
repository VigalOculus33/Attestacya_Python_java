import argparse
from note_manager import NoteManager

def get_user_input():
    command = input("Введите команду (add, list, edit, delete, exit): ")
    title = message = note_id = None
    if command in ['add', 'edit']:
        title = input("Введите заголовок заметки: ")
        message = input("Введите текст заметки: ")
    if command in ['edit', 'delete']:
        note_id = int(input("Введите ID заметки: "))
    return command, title, message, note_id

def main():
    parser = argparse.ArgumentParser(description="Notes management system")
    parser.add_argument("command", nargs='?', default=None, choices=['add', 'list', 'edit', 'delete', 'exit'])
    parser.add_argument("--title")
    parser.add_argument("--message")
    parser.add_argument("--id", type=int)
    args = parser.parse_args()

    manager = NoteManager('notes.json')

    if args.command:
        command = args.command
        title = args.title
        message = args.message
        note_id = args.id
    else:
        command, title, message, note_id = get_user_input()

    while command != 'exit':
        if command == 'add':
            manager.add_note(title, message)
        elif command == 'list':
            manager.list_notes()
        elif command == 'edit':
            manager.edit_note(note_id, title, message)
        elif command == 'delete':
            manager.delete_note(note_id)

        command, title, message, note_id = get_user_input()

if __name__ == "__main__":
    main()