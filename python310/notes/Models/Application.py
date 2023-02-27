# Задание
# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания
# или последнего изменения заметки. Сохранение заметок необходимо сделать
# в формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.
#


from python310.notes.DataBase.Export_data.Export_on_file_csv.Export_csv import Export_csv
from python310.notes.DataBase.Import_data.Import_on_file_csv.Import_csv import Import_csv
from python310.notes.DataBase.db.Db import DB
from python310.notes.Models.Add_note import Add_new_note
from python310.notes.Presenter.P_console.P_data.Show_data import Show_data
from python310.notes.Presenter.P_console.P_user_data.printer import printer
from python310.notes.UI.UInterface.Interface_console.Text_interface import TxtInterface


class Application(object):

    def main(self):
        alpha = DB("alpha")
        flag = True
        printer(TxtInterface().greeting).prints()
        while (flag):
            printer(TxtInterface().first_menu).prints()
            command = input(TxtInterface().enter_command)
            if command == "1":
                import_c = Import_csv()
                alpha.dbase = import_c.importFromFile()
            elif command == "2":
                export_c = Export_csv(alpha.dbase)
                export_c.writeToFile()
            elif command =="3":
                new_note = Add_new_note()
                new_note.add_note() # type: ignore
                alpha.dbase.append(new_note.note) # type: ignore
                printer(TxtInterface().not_save).prints()
            # elif command =="3":
                    # printAllData(notes)
                # print("33333")
            elif command =="4":
                show_must_go_on = Show_data(alpha.dbase)
                show_must_go_on.show()
                print("44444")
            elif command =="5":
                    # printSpecificData(notes)
                print("5555")
            elif command =="6":
                    # seeNotesAmount(notes)
                print("6666")
            elif command =="7":
                    # editNote(notes)
                print("77777")
            elif command =="8":
                    # deleteNote(notes)
                print("8888")
            elif command =="0":
                    printer(TxtInterface().goodbye).prints()
                    flag = False
            else:
                    printer(TxtInterface.incorrect_input).prints()