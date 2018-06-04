#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
#读取0:gray,1:color,default=1
img=cv2.imread('image/wxs.jpg',0)
import matplotlib.pyplot as plt
plt.imshow(img,cmap='gray')
#plt.xlabel('1')
#plt.ylabel('2')
plt.xticks([]),plt.yticks([]) #隐藏坐标线
plt.show()