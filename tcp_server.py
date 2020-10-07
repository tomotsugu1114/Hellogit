import socket

PORT = 8080
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('192.168.128.201', PORT))
    s.listen()
    while True:
        (connection, client) = s.accept()
        try:
            print('Client connected', client)
            data = connection.recv(BUFFER_SIZE)
            print('クライアントからの情報:' + data.decode())
            data2 = input('クライアントに送る情報 > ')
            connection.send(data2.encode())
        finally:
            connection.close()