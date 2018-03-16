#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
import seaborn as sns
sns.set()

#3x3的随机数据
# uniform_data = np.random.rand(3, 3)
# print (uniform_data)
# heatmap = sns.heatmap(uniform_data)
#设置取值范围
#ax = sns.heatmap(uniform_data, vmin=0.2, vmax=0.5)

# normal_data = np.random.randn(3, 3)
# print (normal_data)
# #0为中心值
# ax = sns.heatmap(normal_data, center=0)

flights = sns.load_dataset("flights")
#Reshape data (produce a "pivot" table) based on column values. Uses
#unique values from index / columns to form axes of the resulting  DataFrame.
flights = flights.pivot("month", "year", "passengers")
#print (flights)
#ax = sns.heatmap(flights)
#annot:注释，linewidth：线的宽度，会有间隔的效果
#ax = sns.heatmap(flights, annot=True,fmt="d",linewidths=.5)
#diy your color
ax = sns.heatmap(flights, cmap="YlGnBu")
plt.show()