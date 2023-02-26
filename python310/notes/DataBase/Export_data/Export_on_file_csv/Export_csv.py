import csv
from python310.notes.Presenter.P_console.P_user_data.printer import printer
# from python310.notes.Models import Note

class Write_csv:
    def __init__(self, notes):
      self.notes = notes

    def writeToFile(self):
        if (len(self.notes) > 0):
            with open('python310/notes/DataBase/Data/data_csv/db.csv', 'w') as data:
                writer = csv.writer(data, delimiter=";", lineterminator="\r")
                for x in self.notes:
                    writer.writerow([x.id_note, x.title, x.body, x.date])
            printer("Notes saved!").prints()
        else:
            printer("Notes are empty!").prints()