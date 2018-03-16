#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt

sns.set(style="ticks")
np.random.seed(sum(map(ord, "axis_grids")))
tips = sns.load_dataset("tips")

# 对于俩种不同的时间进行画图
# g = sns.FacetGrid(tips, col="time")
# g.map(plt.hist, "tip")

# alpha越小越透明
# g = sns.FacetGrid(tips, col="sex", hue="smoker")
# g.map(plt.scatter, "total_bill", "tip", alpha=.7)
# #显示hue的类别
# g.add_legend()

# fit_reg=True表示画出回归
# g = sns.FacetGrid(tips, row="smoker", col="time", margin_titles=True)
# g.map(sns.regplot, "size", "total_bill", color=".1", fit_reg=True, x_jitter=.1)


# from pandas import Categorical
# ordered_days = tips.day.value_counts().index
# print (ordered_days)
# ordered_days = Categorical(['Thur', 'Fri', 'Sat', 'Sun'])
# g = sns.FacetGrid(tips, row="day", row_order=ordered_days,
#                   size=1.7, aspect=4,)
# g.map(sns.boxplot, "total_bill")

# s为数据点的大小,edge为点周围的颜色
# pal = dict(Lunch="seagreen", Dinner="gray")
# g = sns.FacetGrid(tips, hue="time", palette=pal, size=5)
# g.map(plt.scatter, "total_bill", "tip", s=50, alpha=.7, linewidth=.5, edgecolor="red")
# g.add_legend()

# g = sns.FacetGrid(tips, hue="sex", palette="Set1", size=5, hue_kws={"marker": ["^", "v"]})
# g.map(plt.scatter, "total_bill", "tip", s=100, linewidth=.5, edgecolor="white")
# g.add_legend()

# with sns.axes_style("white"):
#     g = sns.FacetGrid(tips, row="sex", col="smoker", margin_titles=True, size=2.5)
# g.map(plt.scatter, "total_bill", "tip", color="#334488", edgecolor="white", lw=.5);
# g.set_axis_labels("Total bill (US Dollars)", "Tip")
# g.set(xticks=[10, 30, 50], yticks=[2, 6, 10])
# #子图之间的距离
# g.fig.subplots_adjust(wspace=.02, hspace=.02)
#g.fig.subplots_adjust(left  = 0.125,right = 0.5,bottom = 0.1,top = 0.9, wspace=.02, hspace=.02)

#对图
iris = sns.load_dataset("iris")
# g = sns.PairGrid(iris)
# #对角线柱状图
# g.map_diag(plt.hist)
# #其他散点图
# g.map_offdiag(plt.scatter)

#选取俩个属性进行画对图
# g = sns.PairGrid(iris, vars=["sepal_length", "sepal_width"], hue="species")
# g.map(plt.scatter)


plt.show()
