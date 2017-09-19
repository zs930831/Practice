#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading

#继承的方式运行多线程
class Mythred(threading.Thread):
    def __init__(self, n):
        super(Mythred, self).__init__()
        self.n = n

    def run(self):
        print ("task: ", self.n)


t1 = Mythred("t1")
t2 = Mythred("t2")
t1.start()
t2.start()
