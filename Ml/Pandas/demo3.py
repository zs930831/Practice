#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd  # 数据处理的库
import numpy as np

titanic_survival = pd.read_csv('F:\\GoBig.avi\\tyd_ml_material\\data_processing_pandas\\titanic_train.csv')
# new_titanic_survival = titanic_survival.sort_values("Age", ascending=False)
# print(new_titanic_survival.reset_index(drop=False)[0:10])


# 自定义函数
def h_row(column):
    h_item = column.loc[100]
    return h_item

print(titanic_survival.apply(h_row))
