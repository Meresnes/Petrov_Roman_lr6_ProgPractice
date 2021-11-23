from cleanapi.server import BaseHandler

import requests
import tornado
import uuid
import sqlite3

url_tail = '/update_calc'

class Handler(tornado.web.RequestHandler):
    # Поиск площади ромба
    def post(self):
        # Получение первого аргумента
        a = self.get_argument('a', 'No data received')
        # Получение второго аргумента
        h = self.get_argument('h', 'No data received')
        # Получение id
        id = self.get_argument('uuid', 'No data received')
        # Вычисление площади ромба
        result = str(int(a) * int(h))
        status = 'False'

        # Подключение к БД
        db = sqlite3.connect('calc_result/results.db')
        sql = db.cursor()

        # Поиск id в БД
        sql.execute(f"SELECT result FROM data WHERE uuid = '{id}' ")
        if sql.fetchone():
            try:
                # Обновление данных в таблице
                sql.execute(f"UPDATE data set result = '{result}'WHERE uuid = '{id}'")
                db.commit()
                print('Table updated !')
                # Установка нового статуса
                status = 'True'
            except:
                print('Some error')
        else:
            print('Id not found!')

        db.close()
        self.write({'result': status})




