#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

#slect best neighbors num
k_range=range(1,31)
k_scores=list()
for k in k_range:
    knn=KNeighborsClassifier(n_neighbors=k)
    #分成5组的train data（4/5） and test data（1/5），也可以调试选用设么model
    loss=-cross_val_score(knn,iris_X,iris_y,cv=10,scoring='neg_mean_squared_error')#for regression,越低越好
    # scores=cross_val_score(knn,iris_X,iris_y,cv=10,scoring='accuracy')#for classification，越高越好
    # k_scores.append(scores.mean())
    k_scores.append(loss.mean())

plt.plot(k_range,k_scores)
plt.xlabel("Value of K for KNN")
plt.ylabel('CV Accuracy')
plt.show()