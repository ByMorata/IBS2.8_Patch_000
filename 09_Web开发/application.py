# 00_application.py

def application(encion, start_response):
    start_response("200 OK", [("Content-type", "text/html")])
    body = "<h1>Hello %s!</h1>" % (encion["PATH_INFO"][1:] or "web")

    return [body.encode("utf-8")]
