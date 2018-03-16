#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(color_codes=True)

np.random.seed(sum(map(ord, "regression")))

tips = sns.load_dataset("tips")
#print(tips.head())
#regplot和lmplot都可以花回归图
# sns.regplot(x="total_bill", y="tip", data=tips)
# sns.lmplot(x="total_bill", y="tip", data=tips)

#原始数据偏移一点
sns.regplot(x="size", y="tip", data=tips, x_jitter=.05)


plt.show()