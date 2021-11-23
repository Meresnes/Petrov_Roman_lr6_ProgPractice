from cleanapi import server

server.start('http', 8080, '/', './handlers', './static_html')