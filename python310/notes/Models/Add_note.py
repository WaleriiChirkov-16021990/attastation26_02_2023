

from python310.notes.Models.Note import Note
from python310.notes.UI.UInput.Input_console.Input_note import Input_console_note


class Add_new_note:

    def __init__(self):
        self.note = Note()

    def add_note(self):
        note_input = Input_console_note()
        note_input.input_note()
        self.title = note_input.title
        self.body = note_input.body