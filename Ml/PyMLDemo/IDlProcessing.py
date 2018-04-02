#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,AdaBoostClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import cross_val_score

Steps=10
DL=['DL']
IDL=['IDL']
DL_PC_Il=['DL','PC','IL']
DL_IDL_PC_Il=['DL','IDL','PC','IL']

idl=pd.read_csv('C:\\Users\\CHOSEN1\\Desktop\\Raw_data2.csv')
idl=idl.drop(["Project"],axis=1)
idl.loc[idl['Label'] == 'N', 'Label'] = 1
idl.loc[idl['Label'] == 'Y', 'Label'] = 0
train_label=list(idl['Label'].astype(int))
#print(idl)
#导入，训练，预测
rfc=RandomForestClassifier(random_state=1)
gbc=GradientBoostingClassifier(random_state=1)
abc=AdaBoostClassifier(random_state=1)
eclf = VotingClassifier(estimators=[('rfc', rfc), ('gbc', gbc), ('abc', abc)], voting='soft',weights=[1,1,1])

rfc.fit(idl[DL_IDL_PC_Il],train_label)
gbc.fit(idl[DL_IDL_PC_Il],train_label)
abc.fit(idl[DL_IDL_PC_Il],train_label)
eclf.fit(idl[DL_IDL_PC_Il],train_label)
scores=cross_val_score(eclf,idl[DL_IDL_PC_Il],train_label,cv=3)
print(scores.mean())



