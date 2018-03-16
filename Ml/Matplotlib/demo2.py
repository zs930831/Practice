#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

reviews=pd.read_csv('F:\\GoBig.avi\\tyd_ml_material\\Visualization_matpltlib\\fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews[cols]

#画柱形图
# plt.xlabel('sex')
# plt.ylabel('number')
# plt.xticks((0,1),('male','female'))
# #width为矩形bar的宽度
# plt.bar(x=(0,1),height=(0.8,0.5),width=0.25)
# plt.show()

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

# #ix根据索引查找
# bar_widths = norm_reviews.ix[0, num_cols].values
# bar_positions = np.arange(5) + 0.75
# tick_positions = range(1,6)
# fig, ax = plt.subplots()
# #横着画bar图
# ax.barh(bar_positions, bar_widths, 0.5)
#
# ax.set_yticks(tick_positions)
# ax.set_yticklabels(num_cols)
# ax.set_ylabel('Rating Source')
# ax.set_xlabel('Average Rating')
# ax.set_title('Average User Rating For Avengers: Age of Ultron (2015)')
# plt.show()

#散点图
fig, ax = plt.subplots()
ax.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
ax.set_xlabel('Fandango')
ax.set_ylabel('Rotten Tomatoes')
plt.show()