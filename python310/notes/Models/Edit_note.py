# Класс редактор заметок
# Сначала отображается весь список заметок, но если их очень много, достаточно
# внести заголовок заметки и он вас моментально отправит на ее редактирование.
# Даже если вы забыли точный заголовок, достаточно ввести символьное вхождение,
# но в этом случае поисковик выдаст все заметки где найдет вхождения заголовков.


from python310.notes.Presenter.P_console.P_data.Show_data import Show_data
from python310.notes.Presenter.P_console.P_user_data.Printer import Printer
from python310.notes.UI.UInput.Input_console.Input_data import Input_console_data
from python310.notes.UI.UInterface.Interface_console.Text_interface import TxtInterface



class Edit_note():
    def __init__(self, edition):
      self.edition = edition # this database

    def edit(self):
        if len(self.edition) > 0:
            editor = Show_data(self.edition)
            editor.show()
            titler = Input_console_data()
            titler.input_data(TxtInterface.edit_note)
            temp = list(filter(lambda x: x.title.count(titler.input), self. edition)) # type: ignore
            for item in temp:
               Printer(TxtInterface.current_title).prints()
               Printer(item.title).prints()
               titler.input_data(TxtInterface.enter_title)
               item.title = titler.input
               Printer(TxtInterface.current_note).prints()
               Printer(item.body).prints()
               titler.input_data(TxtInterface.enter_note)
               item.body = titler.input
        else:
           Printer(TxtInterface.notes_empty).prints()