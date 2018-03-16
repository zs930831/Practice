#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np

# a=np.arange(1,10,1).reshape(3,3)#左闭右开
# print(a)
# print(a.ndim)#矩阵的维度
# zero=np.zeros((3,4))#传入元组格式，就是（3,4）
# print(zero)
# one=np.ones((3,4),dtype=int)#传入元组格式，就是（3,4）
# print(one)
# random=np.random.random((2,3))#-1到1的随机
# print(random)
#print(np.linspace(-1,10,10))#-1到10，等间距分为10分
# print(random**3)#**为方
A=np.array([[1,1],
            [2,2]])
B=np.array([[3,3],
            [4,2]])
print(A*B)#对应位置相乘
print(A.dot(B))#内积
print(np.dot(A,B))#内积