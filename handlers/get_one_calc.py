from cleanapi.server import BaseHandler
import tornado
import sqlite3


url_tail = '/get_one_calc'
import urllib.parse


class Handler(tornado.web.RequestHandler):
    # Поиск площади ромба
    def post(self):
        # Получение id
        id = self.get_argument('uuid', 'No data received')
        result = ''

        # Подключение к БД
        db = sqlite3.connect('calc_result/results.db')
        sql = db.cursor()

        # Поиск Результата в БД по id
        sql.execute(f"SELECT result FROM data WHERE uuid = '{id}' ")

        data = sql.fetchone()
        if data:
            # Запись значение результата из БД в переменную
            for value in data:
                result = value
        else:
            result = 'not exist'

        db.close()
        self.write({'uuid': id})
        self.write({'result': result})