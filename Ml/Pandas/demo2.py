#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd  # 数据处理的库
import numpy as np

# food_info=pd.read_csv('F:\\GoBig.avi\\tyd_ml_material\\data_processing_pandas\\food_info.csv')
# food_info.sort_values("Iron_(mg)",inplace=True)#升序排列，却省的为NAN
# print(food_info["Iron_(mg)"])
# food_info.sort_values("Iron_(mg)",inplace=True,ascending=False)#降序排列，却省的为NAN
# print(food_info["Iron_(mg)"])

titanic_survival = pd.read_csv('F:\\GoBig.avi\\tyd_ml_material\\data_processing_pandas\\titanic_train.csv')
# print(titanic_survival.head(5))

# 寻找缺省值
# age_column=titanic_survival["Age"]
# age_is_null=pd.isnull(age_column)#!
# age_null_true=age_column[age_is_null]
# age_null_count=len(age_null_true)
# print(age_is_null)
# print(age_null_true)
# print(age_null_count)

# 算平均数要先排除NAN
# mean_age=sum(age_column[age_is_null==False])/len(age_column[age_is_null==False])
# print(mean_age)
# 这种不推荐
# current_mean_age=titanic_survival["Age"].mean()
# print(current_mean_age)

# 根据某个index用aggfunc计算所对应的values的值
# passenger_survival = titanic_survival.pivot_table(index="Pclass",values="Survived",aggfunc=np.mean)
# print(passenger_survival)
# passenger_survival_age = titanic_survival.pivot_table(index="Pclass",values="Age")#默认的是算平均
# print(passenger_survival_age)
# passenger_survival = titanic_survival.pivot_table(index="Embarked",values=["Survived","Fare"],aggfunc=np.sum)
# print(passenger_survival)

new_titanic_survival=titanic_survival.dropna(axis=0,subset=["Age","Sex"])#有NAN的行被丢弃
print(new_titanic_survival)