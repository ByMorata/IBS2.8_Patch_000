from wsgiref.simple_server import make_server

from application import application

http_00 = make_server("", 8000, application)
print("Serving HTTP on port 8000 ...")
http_00.serve_forever()
