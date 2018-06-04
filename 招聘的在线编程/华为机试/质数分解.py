#!/usr/bin/python
# -*- coding: UTF-8 -*-
a = int(input())


def qiuzhishu(x):
    iszhi = 1
    for i in range(2, int(x ** 0.5 + 2)):
        if x % i == 0:
            iszhi = 0
            print(str(i), end=" ")
            qiuzhishu(x // i)
            break
    if iszhi == 1:
        print(str(x), end=" ")


qiuzhishu(a)