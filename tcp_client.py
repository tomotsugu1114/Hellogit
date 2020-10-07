import socket

PORT = 8080
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('192.168.128.201', PORT))
    data = input('サーバに送る情報 > ')
    s.send(data.encode())
    print('サーバからの情報：'+s.recv(BUFFER_SIZE).decode())