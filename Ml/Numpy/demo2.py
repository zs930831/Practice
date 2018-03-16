#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
A=np.arange(3)
print(A)
print(np.exp(A))
random=10*np.random.random((2,2))
random1=10*np.random.random((2,2))
random2=np.floor(10*np.random.random((2,12)))
# floor=np.floor(random)#向下取整
# print(random)
# print(floor)
# vec=floor.ravel()#变成一个向量
# #print(vec)
# print(vec.reshape(6,2).T)#转置
# print(random)
# print(random1)
# print(np.hstack((random,random1)))#按列拼接
# print(np.vstack((random,random1)))#按行拼接
print(random2)
print(np.hsplit(random2,3))#按列切分
print(np.vsplit(random2.T,3))#按行切
