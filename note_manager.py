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

    # Дополните методами добавления, чтения, редактирования и удаления заметок