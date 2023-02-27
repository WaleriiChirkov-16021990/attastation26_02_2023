# Класс компонента которого принимает БД
# которая для удаления выводит в консоль
# весь список заметок, и пользоватлеб остается
# только ввести нужный ID для удаления заметки.

from python310.notes.Presenter.P_console.P_data.Show_data import Show_data
from python310.notes.Presenter.P_console.P_user_data.Printer import Printer
from python310.notes.UI.UInput.Input_console.Input_data import Input_console_data
from python310.notes.UI.UInterface.Interface_console.Text_interface import TxtInterface


class Del_note:
    def __init__(self, cookies):
        self.cookies = cookies #this DB

    def delete(self):
        if len(self.cookies) > 0:
            show_must_go_on = Show_data(self.cookies)
            show_must_go_on.show()
            number = Input_console_data()
            number.input_data(TxtInterface.enter_ID)
            find = None
            for note in range(len(self.cookies)):# type: ignore
                if self.cookies[note].id_note == number.input :
                    find = note
                    break
            self.cookies.pop(find)
            Printer(TxtInterface.note_deleted).prints()
        else:
            Printer(TxtInterface.notes_empty).prints()
