from note import Note
from storage import load_notes, save_notes

class NoteManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = [Note.from_dict(note_data) for note_data in load_notes(self.filename)]

    def add_note(self, title, message):
        new_note = Note(title, message, len(self.notes) + 1)
        self.notes.append(new_note)
        self.save()

    def list_notes(self):
        return self.notes

    def edit_note(self, note_id, title, message):
        for note in self.notes:
            if note.id == note_id:
                note.title = title
                note.message = message
                note.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save()
                return True
        return False

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save()

    def save(self):
        save_notes(self.filename, [note.to_dict() for note in self.notes])