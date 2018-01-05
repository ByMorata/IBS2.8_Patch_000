import socket

socket_00 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_00.connect((r"www.sina.com", 80))
socket_00.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer_00 = []

while True:

    data_00 = socket_00.recv(1024)
    if data_00:
        buffer_00.append(data_00)
    else:
        break

socket_00.close()
data_00 = b"".join(data_00)
print(data_00)
html = data_00.split(b'\r\n\r\n',1)
with open(r"..\0001.html",r"wb") as file_00:

    print(file_00.name)
    for value_00 in html:
        file_00.write(value_00)
