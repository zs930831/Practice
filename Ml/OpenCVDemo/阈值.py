#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import matplotlib.pyplot as plt

#图像的阈值处理一般使得图像的像素值更单一、图像更简单

#这个函数有四个参数，第一个原图像，第二个进行分类的阈值，第三个是高于（低于）阈值时赋予的新值，第四个是一个方法选择参数，常用的有：
#• cv2.THRESH_BINARY（黑白二值）
#• cv2.THRESH_BINARY_INV（黑白二值反转）
#• cv2.THRESH_TRUNC （得到的图像为多像素值）
#• cv2.THRESH_TOZERO
#• cv2.THRESH_TOZERO_INV
#该函数有两个返回值，第一个retVal（得到的阈值值（在后面一个方法中会用到）），第二个就是阈值化后的图像。
img = cv2.imread('image/1.jpg',0) #直接读为灰度图像
# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
# titles = ['img','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]
# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()



#前面看到简单阈值是一种全局性的阈值，只需要规定一个阈值值，整个图像都和这个阈值比较。
# 而自适应阈值可以看成一种局部性的阈值，通过规定一个区域大小，
# 比较这个点与区域大小里面像素点的平均值（或者其他特征）的大小关系确定这个像素点是属于黑或者白（如果是二值情况）。
# 使用的函数为：cv2.adaptiveThreshold（）

#该函数需要填6个参数：
#第一个原始图像
#第二个像素值上限
#第三个自适应方法Adaptive Method:
#— cv2.ADAPTIVE_THRESH_MEAN_C ：领域内均值
#—cv2.ADAPTIVE_THRESH_GAUSSIAN_C ：领域内像素点加权和，权 重为一个高斯窗口
#第四个值的赋值方法：只有cv2.THRESH_BINARY 和cv2.THRESH_BINARY_INV
#第五个Block size:规定领域大小（一个正方形的领域）
#第六个常数C，阈值等于均值或者加权值减去这个常数（为0相当于阈值 就是求得领域内均值或者加权值）
#这种方法理论上得到的效果更好，相当于在动态自适应的调整属于自己像素点的阈值，而不是整幅图像都用一个阈值。

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
cv2.THRESH_BINARY,11,2) #换行符号 \
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv2.THRESH_BINARY,11,2) #换行符号 \
images = [img,th1,th2,th3]
plt.figure()
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
plt.show()


#Otsu滤波
#简单滤波
#那么经过Otsu’s得到的那个阈值就是函数cv2.threshold的第一个参数了。因为Otsu’s方法会产生一个阈值，那么函数cv2.threshold的的第二个参数（设置阈值）就是0了，
# 并且在cv2.threshold的方法参数中还得加上语句cv2.THRESH_OTSU。那么什么是双峰图像（只能是灰度图像才有），就是图像的灰度统计图中可以明显看出只有两个波峰
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#Otsu 滤波
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print (ret1,ret2)
plt.figure()
plt.subplot(221),plt.imshow(img,'gray')
plt.subplot(222),plt.hist(img.ravel(),256)#.ravel方法将矩阵转化为一维
plt.subplot(223),plt.imshow(th1,'gray')
plt.subplot(224),plt.imshow(th2,'gray')