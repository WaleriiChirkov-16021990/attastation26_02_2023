import os
from datetime import datetime


class Note:
    id = 0

    def __init__(self, id, title, body): # type: ignore
        self.id_note = id
        self.age = title
        self.body = body
        self.date_create = datetime.now()

    def __init__(self):
       self.id_note = Note.id + 1
       self.title = 'Empty'
       self.body = 'Empty'
       self.date_create = datetime.now()
       Note.id +=1