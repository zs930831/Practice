#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas#数据处理的库

food_info=pandas.read_csv('F:\\GoBig.avi\\tyd_ml_material\\data_processing_pandas\\food_info.csv')

#print(type(food_info))
#print(food_info.dtypes)#里面每个feature的类型,字符类型的为object
#print(help(pandas.read_csv))

# food_rows=food_info.head(3)#默认显示前5条数据
# food_tails=food_info.tail(3)#默认显示后5条数据
#print(food_rows)
#print(food_tails)

#print(food_info.columns)#显示列名
#print(food_info.shape)#数据的行数（第一行不算）以及feature的个数
#print(food_info.loc[0:4])#显示第0到4行数据
# two_five_ten=[2,5,10]
# print(food_info.loc[two_five_ten])

ndb_col=food_info["NDB_No"]#取到对应的列
print(ndb_col)

