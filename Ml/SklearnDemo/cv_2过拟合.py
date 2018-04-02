#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import learning_curve

digits=load_digits()
X=digits.data
y=digits.target

#默认为高斯核，gamma过大会过拟合
train_sizes,train_loss,test_loss=learning_curve(SVC(gamma=0.001),X,y,cv=10,scoring='neg_mean_squared_error',
                                                train_sizes=[.1,.25,.5,.75,1])
#输出是负值
train_loss_mean=-np.mean(train_loss,axis=1)
test_loss_mean=-np.mean(test_loss,axis=1)

plt.plot(train_sizes,train_loss_mean,'o-',color='r',label='Training')
plt.plot(train_sizes,test_loss_mean,'o-',color='g',label='Cross_Validation')
plt.legend(loc="best")
plt.xlabel('Training Example')
plt.ylabel('Loss')
plt.show()