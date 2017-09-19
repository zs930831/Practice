#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 高阶函数+函数嵌套==》装饰器
import time

#当函数的参数不确定时，可以使用*args 和**kwargs，*args 没有key值，**kwargs有key值
def timer(func):
    def dec(*args,**kwargs):
        starttime = time.time()
        func(*args,**kwargs)
        endtime = time.time()
        print "It has spended %s" % (endtime - starttime)

    return dec


# 第二种调用方式
@timer
def test1():
    print "in test1"
    time.sleep(1)

@timer
def test2(name):
    print "test2:",name



# 第一种调用方式
# test1=timer(test1)
# test1()

test1()
test2("wxs")
