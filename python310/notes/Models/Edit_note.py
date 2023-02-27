from datetime import datetime
from python310.notes.Models.Note import Note
from python310.notes.Presenter.P_console.P_data.Show_data import Show_data
from python310.notes.Presenter.P_console.P_user_data.Printer import Printer
from python310.notes.UI.UInput.Input_console.Input_data import Input_console_data
from python310.notes.UI.UInterface.Interface_console.Text_interface import TxtInterface



class Edit_note(Note):
    def __init__(self, edition):
      self.edition = edition

    def edit(self):
        editor = Show_data(self.edition)
        editor.show()
        titler = Input_console_data()
        titler.input_data("Enter Title note for edit: ")
        temp = list(filter(lambda x: x.title.count(titler.input), self.edition)) # type: ignore
        for item in temp:
           Printer("текущий заголоdок: ").prints()
           Printer(item.title).prints()
           titler.input_data(TxtInterface.enter_title)
           item.title = titler.input
           Printer("текущяя заметка: ").prints()
           Printer(item.body).prints()
           titler.input_data(TxtInterface.enter_note)
           item.body = titler.input
