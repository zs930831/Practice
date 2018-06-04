#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
from sklearn.ensemble import AdaBoostRegressor


test = pd.read_csv('E:\\python\\Practice\\Ml\\KaggleLearning\\house-prices-advanced-regression-techniques\\test.csv')
train = pd.read_csv('E:\\python\\Practice\\Ml\\KaggleLearning\\house-prices-advanced-regression-techniques\\train.csv')

