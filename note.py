from datetime import datetime

class Note:
    def __init__(self, title, message, note_id=None, date=None):
        self.id = note_id
        self.title = title
        self.message = message
        self.date = date or datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'message': self.message,
            'date': self.date
        }

    @staticmethod
    def from_dict(data):
        return Note(data['title'], data['message'], data['id'], data['date'])