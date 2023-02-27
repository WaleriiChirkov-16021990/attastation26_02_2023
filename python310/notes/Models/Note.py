import os
from datetime import datetime


class Note:
    id = 0

    def __init__(self):
       self.id_note = Note.id + 1
       self.title = 'Empty'
       self.body = 'Empty'
       self.date_create = datetime.today()
       Note.id +=1

    def set(self, id, title, body, date):
        self.id_note = id
        self.title = title
        self.body = body
        self.date_create = date
