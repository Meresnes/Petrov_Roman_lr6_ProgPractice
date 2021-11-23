from cleanapi.server import BaseHandler

import tornado
import uuid
import sqlite3

url_tail = '/delete_one_calc'


class Handler(tornado.web.RequestHandler):
    # Поиск площади ромба
    def post(self):
        # Получение первого аргумента
        id = self.get_argument('uuid', 'No data received')

        # Вычисление площади ромба
        status = 'False'

        # Подключение к БД
        db = sqlite3.connect('calc_result/results.db')
        sql = db.cursor()

        # Поиск id в БД
        sql.execute(f"SELECT result FROM data WHERE uuid = '{id}' ")
        if sql.fetchone():
            try:
                # Удаление данных в таблице
                sql.execute(f"DELETE FROM data WHERE uuid = '{id}'")
                db.commit()
                print('Delete successful!')
                # Установка нового статуса
                status = 'True'
            except:
                print('Some error')
        else:
            print('Id not found!')

        db.close()
        self.write({'result': status})




