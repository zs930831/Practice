#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time


def run(n):
   lock.acquire()
   global num
   num+=1
   #time.sleep(0.1)
   print num
   lock.release()
num=0
lock=threading.Lock()
st = time.time()
res = []
# 直接调用的形式运行多线程,主线程不会等待子线程结束在运行
for i in range(50):
    t = threading.Thread(target=run, args=("t" + str(i),))
    t.start()
    res.append(t)
# for r in res:
#     r.join()  # 线程暂停
print("----Main Thread Is Over-----")
print("Cost %s" % (time.time() - st))  # 50个并行线程耗费的时间
