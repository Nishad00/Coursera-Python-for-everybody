import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('info.cern.ch',80))
cmd = 'GET http://info.cern.ch/hypertext/WWW/TheProject.html HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(5120)
    if(len(data) < 1): break
    print(data.decode())
    d = data.decode()
mysock.close()

print(d.count("Pointers"))