#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
设有n个正整数，将他们连接成一排，组成一个最大的多位整数。
如:n=3时，3个整数13,312,343,连成的最大整数为34331213。
如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。
'''
def sc(scList):
    scList=[str(s) for s in scList]
    scList=sorted(scList,key=lambda x:len(x))
    lensc=len(scList[-1])
    sdict={}
    for s in scList:
        if len(s)<lensc:
            s1=str(s)+(lensc-len(s))*'0'
            sdict[s]=s1
        else:
            sdict[s] = s
    #scList为key的list
    scList=sorted(sdict,key=lambda x:x,reverse=True)
    result=''
    for i in scList:
        result+=i
    return int(result)

scList=[7,13,4,246]
print(sc(scList))
