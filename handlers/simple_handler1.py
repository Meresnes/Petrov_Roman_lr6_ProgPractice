from cleanapi.server import BaseHandler

url_tail = '/'

class Handler(BaseHandler):
    async def get(self):
        self.set_status(200)
        self.write({'result': 'Hello World!'})