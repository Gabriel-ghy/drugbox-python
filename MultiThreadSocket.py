import socket
import threading
import time
import uuid


class myThread1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("开始发送心跳")
        a = "HeartBeat"
        a = a.encode()
        # mac = hex(uuid.getnode())[2:]
        # mac = '-'.join(mac[i:i + 2] for i in range(0, len(mac), 2))
        mac = '11-11-11-11-11-11'
        s.send(mac.encode())
        time.sleep(1)
        while True:
            s.send(a)
            time.sleep(3)


class myThread2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("开始接收信息")
        while True:
            str = s.recv(1024).decode()
            print(str)


mac = hex(uuid.getnode())[2:]
mac = '-'.join(mac[drug:drug + 2] for drug in range(0, len(mac), 2))
print(mac)

s = socket.socket()
host = "127.0.0.1"
port = 8086
s.connect((host, port))

# 创建新线程
thread1 = myThread1()
# thread2 = myThread2()

# 开启新线程
thread1.start()
# thread2.start()
thread1.join()
# thread2.join()
print("退出主线程")
