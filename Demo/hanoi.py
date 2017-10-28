#!/usr/bin/python
# -*- coding: UTF-8 -*-

def dohanoi(n,origion,to,other):
    if n == 1:
        print (origion + "-->" + to)
    else:
        dohanoi(n-1,origion,other,to)
        dohanoi(1,origion,to,other)
        dohanoi(n-1,other,to,origion)

dohanoi(3,"A","C","B")
