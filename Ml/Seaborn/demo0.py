#!/usr/bin/python
# -*- coding: UTF-8 -*-
#seaborn 在 matplotlib上进行了封装
import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def sinplot(flip=1):
    x=np.linspace(0,14,100)
    for i in range(1,7):
        #.5=0.5
        plt.plot(x,np.sin(x+i*.5)*(7-i)*flip)

#采用seaborn设置
# sns.set()
# sinplot()

#sns里面共有darkgrid,whitegrid,dark,white,ticks这5个style
# sns.set_style("ticks")
# data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
# sns.boxplot(data=data)

# sinplot()
#去掉上面和右边的线条,左边的axe隐藏
# sns.despine(offset=10,left=True)

#打开一中背景风格
# with sns.axes_style("darkgrid"):
#     #添加子图
#     plt.subplot(211)
#     sinplot()
# plt.subplot(212)
# sinplot(-1)

# The base context is "notebook", and the other contexts are "paper", "talk", and "poster",
# which are version of the notebook parameters scaled by .8, 1.3, and 1.6,respectively.
sns.set_context("paper")
plt.figure(figsize=(8, 6))
sinplot()

#代替%matplotlib inline
plt.show()