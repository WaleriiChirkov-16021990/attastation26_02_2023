# Класс заметки, конструктор автоматически ведет отсчет при его вызове,
# каждый запуск приложения счет идет с 0 как при создании пустой базы так и
# при считывании базы из файла, он не допустит повторения ID у двух
# и более заметок.


from datetime import datetime
from python310.notes.UI.UInterface.Interface_console.Text_interface import TxtInterface


class Note:
    id = 0   # статичный счётчик

    def __init__(self):
       self.id_note = Note.id + 1
       self.title = TxtInterface.is_empty
       self.body = TxtInterface.is_empty
       self.date_create = datetime.today()
       Note.id +=1

    def set(self, id, title, body, date):
        self.id_note = id
        self.title = title
        self.body = body
        self.date_create = date
        if int(id) > Note.id:
            Note.id = int(id)
