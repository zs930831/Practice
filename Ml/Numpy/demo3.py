#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np

# a=np.ones((3,4),dtype=int)
# #b=a.view()#浅拷贝,拷贝完成后的b的值得改变会影响原来的a
# c=a.copy()#深拷贝,拷贝完成后的c的值得改变不会影响原来的a
# print(c is a)
# #b.shape=2,6
# #b[0,3]=999
# c[0,3]=999
# print(a.shape)
# print("----")
# print(a)
# print(c)
# print("----")
# print(id(a))#a的地址
# #print(id(b))
# print(id(c))

# data=np.sin(np.arange(20).reshape(5,4))
# print(data)
# index=data.argmax(axis=0)#0为列
# print(index)
# print(data.shape[1])#取列的维度
# data_max=data[index,range(data.shape[1])]
# print(data_max)

# a=np.arange(0,40,10)
# b=np.tile(a,(2,2))#扩展
# print(a,"\n",b)

a=np.array([[1,3,2],[4,2,3]])
print(a)
print("-----")
print(np.sort(a,axis=1))#按行排列
print("-----")
print(np.sort(a,axis=0))#按列排列
a=np.array([4,3,1,2])
j=np.argsort(a)
print("-----")
print(j)
print("-----")
print(a[j])