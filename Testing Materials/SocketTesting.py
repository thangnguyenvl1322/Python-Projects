import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('youtube.com', 80))
cmd = 'GET hhttps://www.youtube.com/watch?v=WAxxfzdcNdA&ab_channel=B%C3%8DCHPH%C6%AF%C6%A0NG HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)< 1):
        break
    print(data.decode())
mysock.close()
