import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 6767))

file_name = input("Enter a filename: ")
s.send(file_name.encode())

content = s.recv(1024)
print(content.decode())

s.close()