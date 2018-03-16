#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)

np.random.seed(sum(map(ord, "categorical")))
titanic = sns.load_dataset("titanic")
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

#数据较多的时候会重叠
#sns.stripplot(x="day", y="total_bill", data=tips)
#jitter=True会左右偏移
#sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)
#像树一样
#sns.swarmplot(x="day", y="total_bill", data=tips)
#在分类中，同时把sex也进行分类
#sns.swarmplot(x="day", y="total_bill", hue="sex",data=tips)

#boxplot
#sns.boxplot(x="day", y="total_bill", hue="time", data=tips)
#横着画的boxplot
#sns.boxplot(data=iris,orient="h")

#小提琴图
#sns.violinplot(x="total_bill", y="day", hue="time", data=tips)
#把hue左右分开
#sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True)

#结合俩种图
# sns.violinplot(x="day", y="total_bill", data=tips, inner=None)
# sns.swarmplot(x="day", y="total_bill", data=tips, color="w", alpha=.5)

#条形图可以很好的看到每个类别的差异
#sns.barplot(x="sex", y="survived", hue="class", data=titanic)

#点图可以很好的看到各自的变化
#sns.pointplot(x="sex", y="survived", hue="class", data=titanic)
# sns.pointplot(x="class", y="survived", hue="sex", data=titanic,
#               palette={"male": "g", "female": "m"},
#               markers=["^", "o"], linestyles=["-", "--"])

#多层面板分类图，默认为点图
# sns.factorplot(x="day", y="total_bill", hue="smoker", data=tips, kind="bar")
# sns.factorplot(x="day", y="total_bill", hue="smoker",
#                col="time", data=tips, kind="swarm")
#aspect长宽比
sns.factorplot(x="time", y="total_bill", hue="smoker",
               col="day", data=tips, kind="box", size=4, aspect=.5)
# seaborn.factorplot(x=None, y=None, hue=None, data=None,
# row=None, col=None, col_wrap=None, estimator=<function mean>, ci=95, n_boot=1000, units=None,
#  order=None, hue_order=None, row_order=None, col_order=None, kind='point', size=4, aspect=1, orient=None,
#  color=None, palette=None, legend=True, legend_out=True, sharex=True, sharey=True, margin_titles=False, facet_kws=None, **kwargs)
#
# Parameters：
#
# x,y,hue 数据集变量 变量名
# date 数据集 数据集名
# row,col 更多分类变量进行平铺显示 变量名
# col_wrap 每行的最高平铺数 整数
# estimator 在每个分类中进行矢量到标量的映射 矢量
# ci 置信区间 浮点数或None
# n_boot 计算置信区间时使用的引导迭代次数 整数
# units 采样单元的标识符，用于执行多级引导和重复测量设计 数据变量或向量数据
# order, hue_order 对应排序列表 字符串列表
# row_order, col_order 对应排序列表 字符串列表
# kind : 可选：point 默认, bar 柱形图, count 频次, box 箱体, violin 提琴, strip 散点，swarm 分散点（具体图形参考文章前部的分类介绍）
# size 每个面的高度（英寸） 标量
# aspect 纵横比 标量
# orient 方向 "v"/"h"
# color 颜色 matplotlib颜色
# palette 调色板 seaborn颜色色板或字典
# legend hue的信息面板 True/False
# legend_out 是否扩展图形，并将信息框绘制在中心右边 True/False
# share{x,y} 共享轴线 True/False
# facet_kws FacetGrid的其他参数 字典

plt.show()