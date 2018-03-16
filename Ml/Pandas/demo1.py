#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd#数据处理的库

food_info=pd.read_csv('F:\\GoBig.avi\\tyd_ml_material\\data_processing_pandas\\food_info.csv')
col_names_list=food_info.columns.tolist()
print(col_names_list)

# gram_columns=[]
# for c in col_names_list:
#     if c.endswith("(g)"):
#         gram_columns.append(c)#选取到feature name 带有“(g)”的列
# gram_df=food_info[gram_columns]
# print(gram_df.head(3))

# iron_grams=food_info["Iron_(mg)"]/1000
# food_info["Iron_(g)"]=iron_grams#在原来的数据上添加一个新的列
# print(food_info.head(3))

#print(food_info["Iron_(mg)"]/food_info["Iron_(mg)"].max())#归一化操作