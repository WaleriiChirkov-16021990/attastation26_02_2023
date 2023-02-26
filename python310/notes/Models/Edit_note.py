from datetime import datetime
from python310.notes.Models.Note import Note
from python310.notes.Presenter.P_console.P_user_data.printer import printer



class Edit_note(Note):
    def edit(self):
        printer.prints(self.title) # type: ignore
