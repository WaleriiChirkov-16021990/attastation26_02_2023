

from python310.notes.Presenter.P_console.P_note.Show_note import Show_note
from python310.notes.Presenter.P_console.P_user_data.printer import printer
from python310.notes.UI.UInterface.Interface_console.Text_interface import TxtInterface


class Show_data:
    def __init__(self, notes):
        self.stringi = notes

    def show(self):
        printer(TxtInterface().show_notes).prints()
        for member in self.stringi:
            flash = Show_note(member)
            printer(flash.printNote()).prints()