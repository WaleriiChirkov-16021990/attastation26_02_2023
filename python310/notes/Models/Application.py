
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


from python310.notes.DataBase.db.db import DB
from python310.notes.Models.Add_note import Add_new_note
from python310.notes.Presenter.P_console.P_user_data.printer import printer


class Application(object):

    def main(self):
        alpha = DB("alpha")
        # alpha.dbase = []
        flag = True
        printer("Добро пожаловать не в Notepad--\nДля работы со мной выберите опцию ниже :\n").prints()
        while (flag):
            printer("\n\
            1 - Import Notes from file;\n\
            2 - Export Notes to file;\n\
            3 - Create a new Note;\n\
            4 - View all notes;\n\
            5 - View all notes with the latest showing first;\n\
            6 - View a specific note;\n\
            7 - Check how many notes you have;\n\
            8 - Edit a Note;\n\
            9 - Delete a Note;\n\
            0 - Exit.").prints()
            command = input("Enter command: ")
            if command == "1":
                # notes = importFromFile()
                print("1111")
            elif command == "2":
                # writeToFile(notes)
                print("2")
            elif command =="3":
                new_note = Add_new_note()
                new_note.add_note() # type: ignore
                alpha.dbase.append(new_note.note()) # type: ignore
                printer("Not saved note!").prints()
            # elif command =="3":
                    # printAllData(notes)
                # print("33333")
            elif command =="4":
                    # printSortedData(notes)
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
                    printer("Goodbye!").prints()
                    flag = False
            else:
                    printer("Incorrect unput").prints()