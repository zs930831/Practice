#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd


titanic_train_data=pd.read_csv("titanic_survive/train.csv")
#print(titanic.head())
#print(titanic.describe())

'''- 冗余信息删除
- 缺失值处理
- 非数值型数据转换成数据值
- 异常值处理 
'''
def dataPreprocessing(titanicCsvData,dropList):
    #分析数据每一列，可知'PassengerId'是冗余信息，以及'Name','Ticket','Cabin'三者较为复杂，选择删除四列
    titanic=titanicCsvData.drop(dropList,axis=1)#1为一列，默认是行

    #Sex二值化
    titanic.loc[titanic['Sex']=='male','Sex']=0
    titanic.loc[titanic['Sex']=='female','Sex']=1

    #添加age的缺省值
    #用平均数添加
    titanic['Age']=titanic['Age'].fillna(titanic['Age'].median())

    #Embarked用值替代
    titanic.loc[titanic['Embarked']=='S','Embarked']=0
    titanic.loc[titanic['Embarked']=='C','Embarked']=1
    titanic.loc[titanic['Embarked']=='Q','Embarked']=2
    titanic['Embarked']=titanic['Embarked'].fillna(2)
    titanic['Fare'] = titanic['Fare'].fillna(0)
    #print (titanic['Embarked'].unique() )

    #print(np.where(titanic['Fare']==0)[0])#[179 263 271 277 302 413 466 481 597 633 674 732 806 815 822]
    #titanic['Fare'][np.where(titanic['Fare']==0)[0] ] = titanic['Fare'][ titanic['Fare'].nonzero()[0] ].min() / 10
    return titanic

from sklearn.linear_model import LogisticRegression
from sklearn import model_selection #交叉验证库，将测试集进行切分交叉验证取平均



features=['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']   #用到的特征
droplist=['Name','PassengerId','Ticket','Cabin']
droplist1=['Name','Ticket','Cabin']
titanic_train_data=dataPreprocessing(titanic_train_data,droplist)

#导入，训练，预测
alg=LogisticRegression(random_state=1,penalty='l2')
#CV
kf=model_selection.KFold(titanic_train_data.shape[0],shuffle=False,random_state=1)
alg.fit(titanic_train_data[features],titanic_train_data['Survived'])
#scores=model_selection.cross_val_score(alg,titanic_train_data[features],titanic_train_data['Survived'],cv=3)
#print(scores.mean())
#print(alg)

#test
titanic_test_data=pd.read_csv("titanic_survive/test.csv")
titanic_test_data=dataPreprocessing(titanic_test_data,droplist1)

#print(titanic_test_data.describe())
predictions=alg.predict(titanic_test_data[features])
result=pd.DataFrame({'PassengerId':titanic_test_data['PassengerId'],'Survived':predictions.astype(np.int32)})
result.to_csv("titanic_survive/result.csv",index=False)

