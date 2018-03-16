#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy

vector=numpy.array([5,10,15,20])
matric=numpy.array([[5,10,15,20],[5,10,15,20],[5,10,15,20]])
#print(vector)
#print(matric)
print(matric[:,0:2])
#print(matric.shape)
#equal_five_ten=(vector==10)|(vector==5)
vector=vector.astype(float)
min=vector.min()
#print(vector,min)
#print(help(numpy.array))
print(matric.sum(axis=0))#0是列