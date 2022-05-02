import psycopg2


class CRUD:

    connection = psycopg2.connect(user="postgres",
                                       # пароль, который указали при установке PostgreSQL
                                       password="qwerty",
                                       host="127.0.0.1",
                                       port="5432",
                                       database="Accounting")
    cursor = connection.cursor()

    def __init__(self):
        create_table_query = '''CREATE TABLE IF NOT EXISTS operations
                              (НОМЕР_СЧЕТА  TEXT    NOT NULL,
                              НАИМЕНОВАНИЕ  TEXT    NOT NULL,
                              ДЕБЕТ         TEXT    NOT NULL,
                              КРЕДИТ        TEXT    NOT NULL);'''
        self.cursor.execute(create_table_query)
        self.connection.commit()
        print("Таблица успешно создана в PostgreSQL")

    def create(self, acc_number, name, debit, credit):
        insert_query = """ INSERT INTO operations VALUES (""" + str(acc_number)\
                       + """, """ + str(name) + """, """ + str(debit) + """, """ + str(credit) + """)"""
        self.cursor.execute(insert_query)
        self.connection.commit()
        print("Запись успешно вставлена")

    def read(self):
        self.cursor.execute("SELECT * from operations")
        for row in self.cursor.fetchall():
            print("НОМЕР_СЧЕТА =", row[0], )
            print("НАИМЕНОВАНИЕ =", row[1])
            print("ДЕБЕТ =", row[2])
            print("КРЕДИТ =", row[3], "\n")

    def update(self, acc_number, field, new):
        update_query = """Update operations set """ + field + """ = """ + new + """ where НОМЕР_СЧЕТА = """ + acc_number
        self.cursor.execute(update_query)
        self.connection.commit()
        count = self.cursor.rowcount
        print(count, "Запись успешно изменена")

    def delete(self, acc_number):
        delete_query = """Delete from operations where НОМЕР_СЧЕТА = """ + acc_number
        self.cursor.execute(delete_query)
        self.connection.commit()
        count = self.cursor.rowcount
        print(count, "Запись успешно удалена")

    def __del__(self):
        self.cursor.close()
        self.connection.close()
