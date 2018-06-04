#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

#对于图形的平滑与滤波，但从滤波角度来讲，一般主要的目的都是为了实现对图像噪声的消除，增强图像的效果。
#统一的2D滤波器cv2.filter2D类似于卷积核
img = cv2.imread('image/1.jpg',0) #直接读为灰度图像
img1=np.float32(img)
kernel=np.ones((5,5),dtype=np.float32)/25

dst=cv2.filter2D(img1,-1,kernel)