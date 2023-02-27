# Класс записи базы данных в файл csv

import csv
from python310.notes.Presenter.P_console.P_user_data.Printer import Printer
from python310.notes.UI.UInterface.Interface_console.Path import Path
from python310.notes.UI.UInterface.Interface_console.Text_interface import TxtInterface

class Export_csv:
    def __init__(self, notes):
      self.notes = notes
      self.path = Path().PATH_CSV

    def writeToFile(self):
        if (len(self.notes) > 0):
            with open(self.path, 'w') as data:
                writer = csv.writer(data, delimiter=";", lineterminator="\r")
                for x in self.notes:
                    writer.writerow([x.id_note, x.title, x.body, x.date_create])
            Printer(TxtInterface().notes_saved).prints()
        else:
            Printer(TxtInterface().notes_empty).prints()
