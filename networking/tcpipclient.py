import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 4000))
msg = s.recv(1024)

while msg:
    print("Received: ", msg.decode())
    msg = s.recv(1024)

s.close()