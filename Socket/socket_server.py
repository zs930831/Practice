#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
server=socket.socket()
server.bind(('127.0.0.1',6969))#binding port
server.listen(5)#listen need parameter!
print("waitting for connecting.........")
conn,addr=server.accept()
print(conn,addr)
print("connecting come")
data=conn.recv(1024)
conn.send(data.upper())
server.close()
