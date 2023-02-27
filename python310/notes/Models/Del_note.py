



from python310.notes.Presenter.P_console.P_data.Show_data import Show_data
from python310.notes.Presenter.P_console.P_user_data.Printer import Printer
from python310.notes.UI.UInput.Input_console.Input_data import Input_console_data


class Del_note:
    def __init__(self, cookies):
      self.cookies = cookies

    def delete(self):
        show_must_go_on = Show_data(self.cookies)
        show_must_go_on.show()
        number = Input_console_data()
        number.input_data("Enter ID note for delete: ")
        find = None
        for note in range(len(self.cookies)):# type: ignore
            if self.cookies[note].id_note == number.input :
                find = note
                break
        self.cookies.pop(find)
        Printer("Note deleted").prints()