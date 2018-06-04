#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

datapath = "E:\\python\\Practice\\Ml\\KaggleLearning\\spam-classification\\spam.csv"
df = pd.read_csv(datapath, delimiter=',', encoding='latin-1')
# df.head()

df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
df.describe()

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(df.v1)
plt.xlabel('Label')
plt.title('Number of ham and spam messages')

'''
le = preprocessing.LabelEncoder()
>>> le.transform([1, 1, 2, 6]) 
array([0, 0, 1, 2]...)


lb = preprocessing.LabelBinarizer()
>>> lb.fit_transform([1, 6])
array([[1, 0, 0, 0],
       [0, 0, 0, 1]])
>>> lb.fit_transform(['yes', 'no', 'no', 'yes'])
array([[1],
       [0],
       [0],
       [1]])
'''
from sklearn.preprocessing import LabelEncoder, LabelBinarizer
from sklearn.model_selection import train_test_split

Y = df.v1
X = df.v2
le = LabelEncoder()
Y = le.fit_transform(Y)
Y = Y.reshape(-1, 1)
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.15)

from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence

max_words = 1000
max_len = 150
tok = Tokenizer(num_words=max_words)
tok.fit_on_texts(train_X)
sequences = tok.texts_to_sequences(train_X)
sequences_matrix = sequence.pad_sequences(sequences, maxlen=max_len)

from keras.layers import Embedding, LSTM, Dropout, Activation, Dense, Input
from keras.optimizers import RMSprop
from keras.models import Model
from keras.callbacks import EarlyStopping


def RNN():
    inputs = Input(shape=[max_len], name='inputs')
    layer = Embedding(input_dim=max_words, output_dim=50, input_length=max_len)(inputs)
    layer = LSTM(64)(layer)
    layer = Dense(256, name="FC1")(layer)
    layer = Activation(activation='relu')(layer)
    # dropout激活函数的后面
    layer = Dropout(rate=0.5)(layer)
    layer = Dense(1, name='output_layer')(layer)
    layer = Activation(activation='relu')(layer)
    model = Model(inputs=inputs, outputs=layer)
    return model


model = RNN()
model.summary()
model.compile(optimizer=RMSprop(), loss='binary_crossentropy', metrics=['accuracy'])

model.fit(sequences_matrix, train_Y, batch_size=128, epochs=10,
          validation_split=0.2, callbacks=[EarlyStopping(monitor='val_loss', min_delta=0.0001)])

test_sequences = tok.texts_to_sequences(test_X)
test_sequences_matrix = sequence.pad_sequences(test_sequences, maxlen=max_len)

accr = model.evaluate(test_sequences_matrix, test_Y)
# 0.886
print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accr[0], accr[1]))
