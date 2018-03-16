#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

unrate=pd.read_csv('F:\\GoBig.avi\\tyd_ml_material\\Visualization_matpltlib\\UNRATE.csv')

#图的大小，长为3，宽为4
# fig=plt.figure(figsize=(3,4))
# #表示ax1为2x2图里面的第一个子图
# ax1=fig.add_subplot(2,2,1)
# ax2=fig.add_subplot(2,2,2)
# ax3=fig.add_subplot(2,2,4)
#
# ax1.plot(np.arange(5),np.arange(5))
# ax2.plot(np.arange(5)*2,np.arange(5))
# plt.show()

#画出俩条折线
unrate["DATE"]=pd.to_datetime(unrate["DATE"])#转换成日期格式
unrate["Month"]=unrate["DATE"].dt.month
fig=plt.figure(figsize=(6,3))
plt.plot(unrate[0:12]["Month"],unrate[0:12]["VALUE"],c="red",label='RED')
plt.plot(unrate[12:24]["Month"],unrate[12:24]["VALUE"],c="blue",label="BLUE")
#添加线的标签
plt.legend(loc='best')
#print(help(plt.legend))
plt.show()