from datetime import datetime
from note import Note
from storage import load_notes, save_notes

class NoteManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = self.load()

    def load(self):
        data = load_notes(self.filename)
        return [Note.from_dict(note_data) for note_data in data]

    def save(self):
        save_notes(self.filename, [note.to_dict() for note in self.notes])

    def add_note(self, title, message):
        new_id = max([note.id for note in self.notes], default=0) + 1
        new_note = Note(title, message, new_id)
        self.notes.append(new_note)
        self.save()
        print(f"Заметка с ID {new_id} добавлена.")

    def list_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}, Title: {note.title}, Date: {note.date}\n{note.message}\n")

    def edit_note(self, note_id, title, message):
        for note in self.notes:
            if note.id == note_id:
                note.title = title
                note.message = message
                note.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save()
                print(f"Заметка с ID {note_id} обновлена.")
                return
        print(f"Заметка с ID {note_id} не найдена.")

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save()
        print(f"Заметка с ID {note_id} удалена.")