#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

loaded_data=datasets.load_boston()

loaded_data_X=loaded_data.data
loaded_data_y=loaded_data.target


X_train,X_test,y_train,y_test=train_test_split(loaded_data_X,loaded_data_y,test_size=0.3)

alg=LinearRegression()
alg.fit(X_train,y_train)
#print(alg.predict(X_test))

#y=ax+b
# print(alg.coef_)#a
# print(alg.intercept_)#b

#alg的参数
# print(alg.get_params())

print(alg.score(X_test,y_test))#R^2