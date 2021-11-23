from cleanapi.server import BaseHandler
import json
import requests
import tornado
url_tail = '/diamond_area'

class Handler(tornado.web.RequestHandler):
    # Поиск площади ромба
    def post(self):
        # Получение первого аргумента
        a = self.get_argument('a', 'No data received')
        # Получение второго аргумента
        h = self.get_argument('h', 'No data received')
        # Вычисление площади ромба
        s = str(int(a) * int(h))

        self.write({'success': 'success'})
        self.write({'version': '0.0.0.2'})
        self.write({'result': s})