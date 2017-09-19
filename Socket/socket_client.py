#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
client=socket.socket()
client.connect(('localhost',6969))
client.send("你好")
data=client.recv(1024)
print("recv",data)
client.close()