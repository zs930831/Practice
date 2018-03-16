#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
#利用np.random.seed()函数设置相同的seed，每次生成的随机数相同。如果不设置seed，则每次会生成不同的随机数
np.random.seed(sum(map(ord, "distributions")))

#x = np.random.normal(size=100)
#sns.distplot(x,kde=False)
#sns的柱形图
#sns.distplot(x, bins=20, kde=False)

mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])
#print(df)
#jointplot可以画出单变量的散点图以及直方图
#sns.jointplot(x="x", y="y", data=df)

# x, y = np.random.multivariate_normal(mean, cov, 1000).T
# with sns.axes_style("white"):
#     sns.jointplot(x=x, y=y, kind="hex", color="k")

#读取数据中4个特征俩俩的关系，画出,在线读取的，不需要本机的绝对路径
iris = sns.load_dataset("iris")
sns.pairplot(iris)

plt.show()