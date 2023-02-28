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
#                       Application


import os.path
from python310.notes.DataBase.Export_data.Export_on_file_csv.Export_csv import Export_csv
from python310.notes.DataBase.Export_data.Export_on_file_json.Export_json import Export_json
from python310.notes.DataBase.Import_data.Import_on_file_csv.Import_csv import Import_csv
from python310.notes.DataBase.Import_data.Import_on_file_json.Import_json import Import_json
from python310.notes.DataBase.db.Db import DB
from python310.notes.Models.Add_note import Add_new_note
from python310.notes.Models.Del_note import Del_note
from python310.notes.Models.Edit_note import Edit_note
from python310.notes.Presenter.P_console.P_data.Show_data import Show_data
from python310.notes.Presenter.P_console.P_user_data.Printer import Printer
from python310.notes.UI.UInterface.Interface_console.Path import Path
from python310.notes.UI.UInterface.Interface_console.Text_interface import TxtInterface


class Application(object):

    def main(self):
        alpha = DB("alpha")
        flag = True
        Printer(TxtInterface().greeting).prints()
        while (flag):
            Printer(TxtInterface().first_menu).prints()
            command = input(TxtInterface().enter_command)
            if command == "1":
                if os.path.isfile(Path().PATH_CSV):
                    importer = Import_csv()
                    alpha.dbase = importer.importFromFile()
                else:
                    Printer(TxtInterface.not_file).prints()
            elif command == "2":
                if os.path.isfile(Path().PATH_CSV):
                    exporter = Export_csv(alpha.dbase)
                    exporter.writeToFile()
                else:
                    Printer(TxtInterface.not_file).prints()
            elif command =="3":
                adder = Add_new_note()
                adder.add_note()
                alpha.dbase.append(adder.note)
                Printer(TxtInterface().not_save).prints()
            elif command =="4":
                show_must_go_on = Show_data(alpha.dbase)
                show_must_go_on.show()
            elif command =="5":
                shower = Show_data(alpha.dbase)
                shower.show_last_note()
            elif command =="6":
                editor = Edit_note(alpha.dbase)
                editor.edit()
            elif command =="7":
                deleter = Del_note(alpha.dbase)
                deleter.delete()
            elif command =="8":
                if os.path.isfile(Path.PATH_JSON):
                    exporter = Export_json(alpha.dbase)
                    exporter.write()
                else:
                    Printer(TxtInterface.not_file).prints()
            elif command =="9":
                if os.path.isfile(Path.PATH_JSON):
                    importer = Import_json()
                    importer.read_file()
                    importer.parse_input()
                    alpha.dbase = importer.parse_data
                else:
                    Printer(TxtInterface.not_file).prints()
            elif command =="0":
                    Printer(TxtInterface().goodbye).prints()
                    flag = False
            else:
                    Printer(TxtInterface().incorrect_input).prints()