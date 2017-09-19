#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time


def run(n):
    print("task " + n)
    time.sleep(2)
    print ("task %s done \n" % n)


st = time.time()
res = []
# 直接调用的形式运行多线程,主线程不会等待子线程结束在运行
for i in range(50):
    t = threading.Thread(target=run, args=("t" + str(i),))
    t.setDaemon(True)#设置为守护进程，程序不会等待守护进程的结束，即主线程结束，程序就结束了
    t.start()
    res.append(t)
# for r in res:
#     r.join()  # 线程暂停
print("----Main Thread Is Over-----")
print("Cost %s" % (time.time() - st))  # 50个并行线程耗费的时间
# run("t1")
# run("t2")
