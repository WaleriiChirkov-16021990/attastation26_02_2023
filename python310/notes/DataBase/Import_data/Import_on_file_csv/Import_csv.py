# Класс чтения базы данных из файла csv

import csv
from python310.notes.Models.Note import Note
from python310.notes.Presenter.P_console.P_user_data.Printer import Printer
from python310.notes.UI.UInterface.Interface_console.Path import Path
from python310.notes.UI.UInterface.Interface_console.Text_interface import TxtInterface

class Import_csv:

    def __init__(self):
        self.path = Path().PATH_CSV # для исключения ошибок сделаю пока так


    def importFromFile(self):
        notes = []
        with open(self.path, 'r') as f:
            reader = csv.reader(f, delimiter=";")
            for row in reader:
                note = Note()
                note.set(row[0], row[1], row[2], row[3]) # type: ignore
                notes.append(note)
        Printer(TxtInterface().notes_imported).prints()
        return notes
