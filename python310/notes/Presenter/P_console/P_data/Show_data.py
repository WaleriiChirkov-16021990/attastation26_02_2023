# Класс отображает всю базу в консоль, либо последнюю заметку из базы

from python310.notes.Presenter.P_console.P_note.Show_note import Show_note
from python310.notes.Presenter.P_console.P_user_data.Printer import Printer
from python310.notes.UI.UInterface.Interface_console.Text_interface import TxtInterface


class Show_data:
    def __init__(self, notes):
        self.stringi = notes #this data

    def show(self):
        if len(self.stringi) > 0:
            Printer(TxtInterface().show_notes).prints()
            for member in self.stringi:
                flash = Show_note(member)
                Printer(flash.printNote()).prints()
        else:
            Printer(TxtInterface().notes_empty).prints()


    def show_last_note(self):
        if len(self.stringi) > 0:
            Printer(TxtInterface().show_last).prints()
            last = Show_note(self.stringi[-1])
            Printer(last.printNote()).prints()
        else:
            Printer(TxtInterface().notes_empty).prints()
