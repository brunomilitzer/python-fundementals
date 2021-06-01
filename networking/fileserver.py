import socket

host = "localhost"
port = 6767

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print("Server listening on port: ", port)
s.listen(1)
c, addr = s.accept()

file_name = c.recv(1024)

try:
    f = open(file_name, 'rb')
    content = f.read()
    c.send(content)
    f.close()
except FileNotFoundError:
    c.send(b"File does not exist")

c.close()
