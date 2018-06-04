#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np
#绘制直线cv2.line（img,Point pt1,Point pt2,color,thickness=1,line_type=8 shift=0）
#无符号8位（1字节）整数类型
#灰色
# img = np.zeros((512,512),np.uint8)#生成一个空灰度图像
# cv2.line(img,(0,0),(511,511),color=255,thickness=5)
# plt.imshow(img,'gray')

#彩色
# img = np.zeros((512,512,3),np.uint8)#生成一个空彩色图像
# cv2.line(img,(0,0),(511,511),(55,255,155),5)
# plt.imshow(img,'brg')
# plt.show()


#绘制矩形，需要确定的就是矩形的两个点（左上角与右下角），颜色，线的类型（不设置就默认）。
# img = np.zeros((512,512,3),np.uint8)#生成一个空彩色图像
# cv2.rectangle(img,(20,20),(411,411),(55,255,155),5)
# plt.imshow(img,'brg')
# plt.show()

#绘制圆形也很简单，只需要确定圆心与半径，函数：
#cv2.circle (img,(380,0),63,(255,0,0),3)
# img = np.zeros((512,512,3),np.uint8)#生成一个空彩色图像
# cv2.circle(img,(200,200),50,(55,255,155),8)#修改最后一个参数
# plt.imshow(img,'brg')

#绘制椭圆
img = np.zeros((512,512,3),np.uint8)#生成一个空彩色图像
cv2.ellipse(img,(256,256),(150,100),0,0,180,250,-1)
#注意最后一个参数-1，表示对图像进行填充，默认是不填充的，如果去掉，只有椭圆轮廓了
plt.imshow(img,'brg')

plt.show()