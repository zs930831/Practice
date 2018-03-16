#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd  # 数据处理的库
import numpy as np

#DataFrame由一系列Series组成
fandago=pd.read_csv('F:\\GoBig.avi\\tyd_ml_material\\data_processing_pandas\\fandango_score_comparison.csv')
#在pandas一列就相当于一个series
series_film=fandago["FILM"]
series_rt=fandago['RottenTomatoes']
print(type(series_film))
print(series_film[0:5])

film_name=series_film.values
#封装在np上
#print(type(film_name))
rt_scores=series_rt.values
#print(rt_scores)
#根据index,找到对应的rt_scores
series_custom=pd.Series(rt_scores,index=film_name)
print(series_custom)
print(series_custom[['Cinderella (2015)','Do You Believe? (2015)']])

fandago_films=fandago.set_index('FILM',drop=False)
#print(fandago_films.index)

#print(fandago_films["Avengers: Age of Ultron (2015)":"Hot Pursuit (2015)"])