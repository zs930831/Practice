#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#默认的6种color
# sns.set(rc={"figure.figsize": (6, 6)})
# current_palette = sns.color_palette()
# sns.palplot(current_palette)

#超过6个颜色，用下面的
# sns.palplot(sns.color_palette("hls", 8))

#random.normal():随机的高斯分布
# data = np.random.normal(size=(20, 8)) + np.arange(8) / 2
# sns.boxplot(data=data,palette=sns.color_palette("hls", 8))

#一对一对对比的颜色
# sns.palplot(sns.color_palette("Paired",8))

#xkcd
# plt.plot([0, 1], [0, 1], sns.xkcd_rgb["pale red"], lw=3)
# plt.plot([0, 1], [0, 2], sns.xkcd_rgb["medium green"], lw=3)
# plt.plot([0, 1], [0, 3], sns.xkcd_rgb["denim blue"], lw=3)

#连续色板，由浅到深
#sns.palplot(sns.color_palette("Blues"))

#连续色板，由深到浅
# sns.palplot(sns.color_palette("Blues_r"))
#
# #light由浅到深
# sns.palplot(sns.light_palette("green"))
# #dark由浅到深
# sns.palplot(sns.dark_palette("purple"))
#由深到浅
# sns.palplot(sns.light_palette("navy", reverse=True))

x, y = np.random.multivariate_normal([0, 0], [[1, -.5], [-.5, 1]], size=300).T
pal = sns.dark_palette("green", as_cmap=True)
sns.kdeplot(x, y, cmap=pal)

plt.show()
