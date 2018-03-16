#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
unrate=pd.read_csv('F:\\GoBig.avi\\tyd_ml_material\\Visualization_matpltlib\\UNRATE.csv')
unrate["DATE"]=pd.to_datetime(unrate["DATE"])#转换成日期格式
# print(unrate.head(5))
# 画折线图
first_twelve=unrate[0:12]
plt.plot(first_twelve["DATE"],first_twelve["VALUE"])
#x轴坐标变换45%
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends,1948")
plt.show()