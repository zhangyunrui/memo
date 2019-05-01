import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9999))
print(s.recv(1024).decode("utf-8"))


def loop():  # 报错，bad file descriptor
    for i in range(10):
        s.send(b"come")
        print(s.recv(1024).decode("utf-8"))


t = threading.Thread(target=loop)
t.start()
s.send(b'exit')
s.close()
