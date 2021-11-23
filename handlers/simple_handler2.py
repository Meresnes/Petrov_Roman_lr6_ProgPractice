from cleanapi.server import BaseHandler

url_tail = '/example2.json'

class Handler(BaseHandler):
    async def get(self):
        self.set_status(200)
        self.write({'success': 'success'})
        self.write({'result': 'Hello World!'})
        self.write({'version': '0.0.0.1'})