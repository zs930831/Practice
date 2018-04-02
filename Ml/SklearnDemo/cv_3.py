#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import validation_curve

digits = load_digits()
X = digits.data
y = digits.target

param_range=np.logspace(-6,-2.3,5)
# 默认为高斯核，gamma过大会过拟合
train_loss, test_loss = validation_curve(SVC(),X, y, param_name='gamma', param_range=param_range,
                                         cv=10,scoring='neg_mean_squared_error')
# 输出是负值
train_loss_mean = -np.mean(train_loss, axis=1)
test_loss_mean = -np.mean(test_loss, axis=1)

plt.plot(param_range,train_loss_mean, 'o-', color='r', label='Training')
plt.plot(param_range,test_loss_mean, 'o-', color='g', label='Cross_Validation')
plt.legend(loc="best")
plt.xlabel('Gamma')
plt.ylabel('Loss')
plt.show()
