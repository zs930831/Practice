#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
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

idl=pd.read_csv('C:\\Users\\CHOSEN1\\Desktop\\Raw_data1.csv')
idl_labels=idl['Label']
idl=idl.drop(["Project","Label"],axis=1)
idl[DL_IDL_PC_Il]=np.array(idl[DL_IDL_PC_Il],dtype=np.float64).reshape(-1,4)
idl_labels[idl_labels=="N"]=1
idl_labels[idl_labels=="Y"]=0
#idl = StandardScaler().fit_transform(np.float32(float(idl.values)))  # Convert the dataframe to a numpy array

idl_labels=np.array(idl_labels,dtype=np.float64)

rfc=RandomForestClassifier(random_state=1)
gbc=GradientBoostingClassifier(random_state=1)
abc=AdaBoostClassifier(random_state=1)
eclf = VotingClassifier(estimators=[('rfc', rfc), ('gbc', gbc), ('abc', abc)], voting='soft',weights=[1,1,1])

rfc.fit(idl[DL_IDL_PC_Il],idl_labels)
gbc.fit(idl[DL_IDL_PC_Il],idl_labels)
abc.fit(idl[DL_IDL_PC_Il],idl_labels)
eclf.fit(idl[DL_IDL_PC_Il],idl_labels)

y_train_pred = eclf.predict(np.array(idl[DL_IDL_PC_Il],dtype=np.float64))
print(y_train_pred)
#print(y_train_pred)
vote_train = cross_val_score(eclf,y_train_pred,idl_labels)
print(vote_train)


