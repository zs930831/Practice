#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
from sklearn.ensemble import AdaBoostRegressor


df_test = pd.read_csv('C:\\Users\CHOSEN1\\.kaggle\\competitions\\house-prices-advanced-regression-techniques\\test.csv')
df_train = pd.read_csv('C:\\Users\CHOSEN1\\.kaggle\\competitions\\house-prices-advanced-regression-techniques\\train.csv')


# print(df_train .describe()

def dataPreprocessing(dataName):
    # missing data
    total = dataName.isnull().sum().sort_values(ascending=False)
    percent = (dataName.isnull().sum() / dataName.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])

    #dealing with missing data
    df_train = dataName.drop((missing_data[missing_data['Total'] > 1]).index,1)
    df_train = df_train.drop(df_train.loc[df_train['Electrical'].isnull()].index)

# kf=KFold(n_splits=5,random_state=1)
# rfc = RandomForestRegressor(random_state=1)
# rfc.fit(x_train,y_train)
# y_test_pred = rfc.predict(df_test)
# scores = model_selection.cross_val_score(rfc, x_train, y_train)
print(np.exp([2],2))