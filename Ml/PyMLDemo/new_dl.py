#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import seaborn as sns
from scipy.stats import norm, skew
from scipy import stats
import matplotlib.pyplot as plt
path='C:\\Users\\CHOSEN1\\Desktop\\Raw_data.csv'
data=pd.read_csv(path)

# #print(data.describe())
# sns.distplot(data['BugNums'] , fit=norm)
#
# # Get the fitted parameters used by the function
# (mu, sigma) = norm.fit(data['BugNums'])
# print( '\n mu = {:.2f} and sigma = {:.2f}\n'.format(mu, sigma))
#
# #Now plot the distribution
# plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu, sigma)],loc='best')
# plt.ylabel('Frequency')
# plt.title('BugNums distribution')
#
# #Get also the QQ-plot
# fig = plt.figure()
# res = stats.probplot(data['BugNums'], plot=plt)
# plt.show()

import numpy as np
from sklearn.model_selection import KFold,cross_val_score
from sklearn.ensemble import GradientBoostingRegressor,RandomForestRegressor
from sklearn.svm import SVR


data['BugNums']=np.log1p(data['BugNums'])
y_train=data['BugNums']
#print(y_train)
data=data.drop(['Project','BugNums','IDL'],axis=1).astype(float)
print(data)

#Validation function
n_folds = 5

def rmsle_cv(model):
    kf = KFold(n_folds, shuffle=True, random_state=42).get_n_splits(data.values)
    rmse= np.sqrt(-cross_val_score(model, data.values, y_train, scoring="neg_mean_squared_error", cv = kf))
    return(rmse.mean())

model_gb=GradientBoostingRegressor()
model_rf=RandomForestRegressor()
model_svr=SVR()
print("neg_mean_squared_error for gb,rf,svm is {} {} {}".format(rmsle_cv(model_gb),rmsle_cv(model_rf),rmsle_cv(model_svr)))