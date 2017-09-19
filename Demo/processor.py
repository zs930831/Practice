#!/usr/bin/python
# -*- coding: UTF-8 -*-
import multiprocessing
import threading
def thread_run():
    print(threading._get_ident())
def run(n):
    print("processor", n)
    t=threading.Thread(target=thread_run,)
    t.start()



if __name__ == '__main__':
    for i in range(10):
        p=multiprocessing.Process(target=run,args=("%s"%i,))
        p.start()
