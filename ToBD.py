#pip install pysqlite3
import sqlite3
from sqlite3 import Error

class SQLITE:

    def __init__(self):
        try:
            self.con = sqlite3.connect("./StatusPorts.db")          #поднимаем соединение с бд
            print('Connection is established: Database is created')
        except Exception as ex:                                     #или выводим текст ошбки
            print(ex)
        # finally:
        #     con.close()

    def sql_create_table(self):                                     #создаем таблицу для даных о портах коммутатора
        cursorObj = self.con.cursor()
        cursorObj.execute("CREATE TABLE employees (id integer PRIMARY KEY, name text, speed float , status text)")
        self.con.commit()

    def insert_port_data(self, name_l, speed_l, status_l):          #записываем данные о портах в таблицу
        print('here2')
        cursorObj = self.con.cursor()
        sql = ("INSERT INTO employees (name, speed, status) VALUES (?, ?, ?) ")
        cursorObj.execute(sql, [(name_l), (speed_l), (status_l)])
        self.con.commit()

    def update_port_data(self, name_l, speed_l, status_l):          #обновляем данные в таблице ориентируясь на имя порта
        cursorObj = self.con.cursor()
        sql = ("UPDATE employees SET speed = ?, status = ? WHERE name = ?")
        cursorObj.execute(sql, [(speed_l), (status_l), (name_l)])
        self.con.commit()

    def select_port_more_100(self):                                 #вывод имен портов, чья скорость выше 100
        cursorObj = self.con.cursor()
        cursorObj.execute('SELECT name FROM employees WHERE speed > 100.0')
        rows = cursorObj.fetchall()
        return rows

