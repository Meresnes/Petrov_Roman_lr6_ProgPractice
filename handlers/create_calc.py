from cleanapi.server import BaseHandler

import requests
import tornado
import uuid
import sqlite3
url_tail = '/create_calc'



class Handler(tornado.web.RequestHandler):
    # Поиск площади ромба
    def post(self):
        # Получение первого аргумента
        a = self.get_argument('a', 'No data received')
        # Получение второго аргумента
        h = self.get_argument('h', 'No data received')
        # Вычисление площади ромба
        result = str(int(a) * int(h))

        # Генерация id
        id = str(uuid.uuid4())

        # Подключение к БД
        db = sqlite3.connect('calc_result/results.db')
        sql = db.cursor()

        # Создание таблицы с данными
        try:
            sql.execute("""CREATE TABLE data(
            
            uuid TEXT,
            result TEXT
            )""")
            db.commit()
        except:
            print('Table alredy exist')

        # Запись данных в таблицу
        sql.execute(f"INSERT INTO data VALUES (?,?)", (id, result))
        # Подгрузка в базу данных
        db.commit()

        # Вывод таблицы
        # for value in sql.execute("SELECT * FROM data"):
        #     print(value)

        db.close()

        self.write({'uuid': id})
        self.write({'result': result})




