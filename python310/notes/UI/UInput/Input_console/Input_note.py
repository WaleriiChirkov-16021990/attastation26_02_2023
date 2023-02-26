


from python310.notes.UI.UInput.Input_console.input_data import Input_console_data
from python310.notes.UI.UInterface.interface_console.text_interface import txtInterface


class Input_console_note:
    def __init__(self):
      self.title = 'empty'
      self.body = 'empty'

    def input_note(self):
        input_user = Input_console_data()
        self.title = input_user.input_data(txtInterface.enter_title) # type: ignore
        self.body = input_user.input_data(txtInterface.enter_note) # type: ignore