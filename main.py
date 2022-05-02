import numpy

import dbcrud as db
import pandas as pd


def add_record(database):
    print("Введите номер счета:")
    acc_number = input()
    print("Введите наименование:")
    name = input()
    print("Введите дебет:")
    debit = input()
    print("Введите кредит:")
    credit = input()
    database.create("\'" + acc_number + "\'", "\'" + name + "\'", "\'" + debit + "\'", "\'" + credit + "\'")
    print("Запись добавлена")


def show_records(database):
    database.read()


def upd_record(database):
    print("Введите номер счета")
    acc_number = input()
    print("Введите поле, которое хотите изменить"
          "(НОМЕР_СЧЕТА, НАИМЕНОВАНИЕ, ДЕБЕТ, КРЕДИТ")
    field = input()
    if field != "НОМЕР_СЧЕТА" and field != "НАИМЕНОВАНИЕ" and field != "ДЕБЕТ" and field != "КРЕДИТ":
        print("Неверный ввод")
        return
    print("Введите значение")
    new = input()
    database.update("\'" + acc_number + "\'", field, "\'" + new + "\'")

def del_record(database):
    print("Введите номер счета")
    acc_number = input()
    database.delete("\'" + acc_number + "\'" )


def download_table(database):
    print("Введите путь: ")
    # считываем строку
    table_path = input()
    data = pd.read_excel(table_path, skiprows=1)
    i = 0
    while i < len(data.to_numpy()) - 1:
        if str(data.to_numpy()[i, 2]) == "nan":
            data.to_numpy()[i, 2] = 0
        if str(data.to_numpy()[i, 3]) == "nan":
            data.to_numpy()[i, 3] = 0
        database.create("\'" + str(data.to_numpy()[i, 0]) + "\'", "\'" + str(data.to_numpy()[i, 1]) + "\'",
                        "\'" + str(data.to_numpy()[i, 2]) + "\'", "\'" + str(data.to_numpy()[i, 3]) + "\'")
        i += 1


if __name__ == "__main__":
    print("Если вы хотите загрузить существующую таблицу Excel, нажмите 1")
    symbol = input()

    database = db.CRUD()

    if symbol == '1':
        download_table(database)

    while 1:
        print("Выберите опцию:\n"
              "1) Добавить запись\n"
              "2) Вывести таблицу\n"
              "3) Обновить запись\n"
              "4) Удалить запись\n"
              "0) Выход\n")

        symbol = input()
        if symbol == '1':
            add_record(database)
        elif symbol == '2':
            show_records(database)
        elif symbol == '3':
            upd_record(database)
        elif symbol == '4':
            del_record(database)
        elif symbol == '0':
            exit(symbol)
        else:
            print("Неверный ввод. Попробуйте ещё раз.")
