#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('image/wxs.jpg',0) #直接读为灰度图像

#关于腐蚀就是将图像的边界腐蚀掉，或者说使得图像整体上看起来变瘦了。
# 它的操作原理就是卷积核沿着图像滑动，如果与卷积核对应的原图像的所有像素值都是1，
# 那么中心元素保持原来的值，否则就变为0。这对于去除白噪声很有用，也可以用于断开两个连载一起的物体
# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.erode(img,kernel,1)
# plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
# plt.subplot(1,2,2),plt.imshow(erosion,'gray')
# plt.show()

#膨胀原理与腐蚀相同，只不过膨胀的时候与卷积核对应的原图像的像素值只要有一个为1，
# 那么中心元素就是1。这么做带来的变化就是图像膨胀了，或者说图像变胖了。
# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.dilate(img,kernel,1)
# plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
# plt.subplot(1,2,2),plt.imshow(erosion,'gray')
# plt.show()

#先进行腐蚀再进行膨胀的运算就是开运算，腐蚀可以让那些在图像外面的小点点去掉，
# 然后把主图像膨胀回去，实现去除图像外噪声
# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
# plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
# plt.subplot(1,2,2),plt.imshow(erosion,'gray')
# plt.show()

#先进行膨胀再进行腐蚀的运算就是闭运算，
# 膨胀可以让那些在图像里面的小点点去掉，然后把主图像腐蚀回去，实现去除图像内噪声。
# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
# plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
# plt.subplot(1,2,2),plt.imshow(erosion,'gray')
# plt.show()

#形态学梯度:膨胀与腐蚀的组合使用，使得结果看上去是提取了物体的轮廓一样。
# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
# plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
# plt.subplot(1,2,2),plt.imshow(erosion,'gray')
# plt.show()

#礼帽:原始图像与其进行开运算后的图像进行一个差。
# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
# plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
# plt.subplot(1,2,2),plt.imshow(erosion,'gray')
# plt.show()

#黑帽:原始图像与其进行闭运算后的图像进行一个差
kernel = np.ones((5,5),np.uint8)
erosion = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(erosion,'gray')
plt.show()
