#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sklearn import svm, datasets

#clf = svm.SVC()
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
#clf.fit(iris_X, iris_y)

'''
pickle提供了一个简单的持久化功能。可以将对象以文件的形式存放在磁盘上。

pickle模块只能在Python中使用，python中几乎所有的数据类型（列表，字典，集合，类等）都可以用pickle来序列化，

pickle序列化后的数据，可读性差，人一般无法识别。
'''
# method 1 pickle
#import pickle

#存入
# with open('save/clf.pickle', 'wb') as f:
#    pickle.dump(clf,f)

#读取
# with open('save/clf.pickle','rb') as f:
#     clf2=pickle.load(f)
#     print(clf2.predict(iris_X[:1]))


#method 2: joblib
from sklearn.externals import joblib

#存入
#joblib.dump(clf,'save/clf.pkl')

#读取
clf3=joblib.load('save/clf.pkl')
print(clf3.predict(iris_X[:1]))