#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 图像的平移,仿射函数cv2.warpAffine()接受三个参数，
# 需要变换的原始图像，移动矩阵M 以及变换的图像大小（这个大小如果不和原始图像大小相同，那么函数会自 动通过插值来调整像素间的关系）。
img = cv2.imread('image/wxs.jpg')
# H=np.float32([[1,0,200],
#              [0,1,200]])
# rows,cols=img.shape[:2]
# #print(rows,cols)
# #dsize=cols,rows
# res=cv2.warpAffine(img,H,(cols,rows))
# plt.subplot(121)
# plt.imshow(img)
# plt.subplot(122)
# plt.imshow(res)
# plt.show()



# 图像的扩大与缩小
# 图像的扩大与缩小有专门的一个函数，cv2.resize()，那么关于伸缩需要确定的就是缩放比例，可以是x与y方向相同倍数，也可以单独设置x与y的缩放比例。
# 另外一个就是在缩放以后图像必然就会变化，这就又涉及到一个插值问题。
# 那么这个函数中，缩放有几种不同的插值（interpolation）方法，
# 在缩小时推荐cv2.INTER_ARER,扩大是推荐cv2.INTER_CUBIC和cv2.INTER_LINEAR。默认都是cv2.INTER_LINEAR
# 插值：interpolation
# None本应该是放图像大小的位置的，后面设置了缩放比例，
# 所有就不要了
# res1 = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
# #直接规定缩放大小，这个时候就不需要缩放因子
# height,width = img.shape[:2]
# res2 = cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)
# plt.subplot(131)
# plt.imshow(img)
# plt.subplot(132)
# plt.imshow(res1)
# plt.subplot(133)
# plt.imshow(res2)
# plt.show()



# cv2.getRotationMatrix2D()，这个函数需要三个参数，旋转中心，旋转角度（逆时针），旋转后图像的缩放比例
# rows,cols = img.shape[:2]
# #第一个参数旋转中心，第二个参数旋转角度，第三个参数：缩放比例
# M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
# #第三个参数：变换后的图像大小
# res = cv2.warpAffine(img,M,(cols,rows))
#
# plt.subplot(121)
# plt.imshow(img)
# plt.subplot(122)
# plt.imshow(res)




# 图像的旋转加上拉升就是图像仿射变换
# M=cv2.getAffineTransform(pos1,pos2),其中两个位置就是变换前后的对应位置关系。
# 输出的就是仿射矩阵M。然后在使用函数cv2.warpAffine()
# rows,cols=img.shape[:2]
# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[10,100],[200,50],[100,250]])
# M = cv2.getAffineTransform(pts1,pts2)
# #第三个参数：变换后的图像大小
# res = cv2.warpAffine(img,M,(cols,rows))
# plt.subplot(121)
# plt.imshow(img)
# plt.subplot(122)
# plt.imshow(res)
# plt.show()

#图像的透射
#这个函数是M = cv2.getPerspectiveTransform(pts1,pts2)，其中pts需要变换前后的4个点对应位置。
# 得到M后在通过函数cv2.warpPerspective(img,M,(200,200))进行
rows,cols = img.shape[:2]
pts1 = np.float32([[56,65],[238,52],[28,237],[239,240]])
pts2 = np.float32([[0,0],[200,0],[0,200],[200,200]])
M = cv2.getPerspectiveTransform(pts1,pts2)
res = cv2.warpPerspective(img,M,(200,200))
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(res)
plt.show()