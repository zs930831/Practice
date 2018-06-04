#!/usr/bin/python
# -*- coding: UTF-8 -*-
from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np
'''
一个RNN是状态RNN，意味着训练时每个batch的状态都会被重用于初始化下一个batch的初始状态。

当使用状态RNN时，有如下假设

所有的batch都具有相同数目的样本
如果X1和X2是两个相邻的batch，那么对于任何i，X2[i]都是X1[i]的后续序列
要使用状态RNN，我们需要

显式的指定每个batch的大小。可以通过模型的首层参数batch_input_shape来完成。batch_input_shape是一个整数tuple，
例如(32,10,16)代表一个具有10个时间步，每步向量长为16，每32个样本构成一个batch的输入数据格式。
在RNN层中，设置stateful=True
'''
data_dim = 16
timesteps = 8
num_classes = 10
batch_size = 32

# Expected input batch shape: (batch_size, timesteps, data_dim)
# Note that we have to provide the full batch_input_shape since the network is stateful.
# the sample of index i in batch k is the follow-up for the sample i in batch k-1.
model = Sequential()
model.add(LSTM(32, return_sequences=True, stateful=True,
               batch_input_shape=(batch_size, timesteps, data_dim)))
model.add(LSTM(32, return_sequences=True, stateful=True))
model.add(LSTM(32, stateful=True))
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# Generate dummy training data
x_train = np.random.random((batch_size * 10, timesteps, data_dim))
y_train = np.random.random((batch_size * 10, num_classes))

# Generate dummy validation data
x_val = np.random.random((batch_size * 3, timesteps, data_dim))
y_val = np.random.random((batch_size * 3, num_classes))

model.fit(x_train, y_train,
          batch_size=batch_size, epochs=5, shuffle=False,
          validation_data=(x_val, y_val))