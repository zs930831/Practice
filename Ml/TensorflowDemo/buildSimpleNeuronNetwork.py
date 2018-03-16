#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# Weights x X with activation function etc:sigmond function
def add_layer(inputs, in_size, out_size,n_layer, activation_function=None):
    layer_name='layer%s'%n_layer
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name="W")
            tf.summary.histogram(layer_name+"/weights",Weights)
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
            tf.summary.histogram(layer_name + "/biases", biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b  # no need to activate
        else:
            outputs = activation_function(Wx_plus_b)
            tf.summary.histogram(layer_name + "/outputs", outputs)
        return outputs


# 构造等差数列np.newaxis增加了维度放在后面，x_data变成300x1
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.005, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

# [None,1]:1column,unknow rows
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')

# input layer
l1 = add_layer(xs, 1, 10, n_layer=1,activation_function=tf.nn.relu)
# output layer
prediction = add_layer(l1, 10, 1, n_layer=2,activation_function=None)

# reduction_indices=[1] : sum by row
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))  # cost function
    tf.summary.scalar("loss",loss)#scalar：纯量（只有大小没有方向）

with tf.name_scope('train'):
    # alpha=0.1
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss=loss)

init = tf.global_variables_initializer()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)
# not block after plot
plt.ion()

with tf.Session() as mySess:
    merged=tf.summary.merge_all()
    writer=tf.summary.FileWriter("logs/",mySess.graph)
    mySess.run(init)
    for i in range(1000):
        # batch gradient descent
        mySess.run(train_step, feed_dict={xs: x_data, ys: y_data})
        if i % 50 == 0:
            # to see the step improvement
            # print(mySess.run(loss,feed_dict={xs:x_data,ys:y_data}))
            result=mySess.run(merged, feed_dict={xs: x_data, ys: y_data})
            writer.add_summary(result,i)
            try:
                ax.lines.remove(lines[0])
            except Exception:
                pass
            prediction_value = mySess.run(prediction, feed_dict={xs: x_data})
            lines = ax.plot(x_data, prediction_value, "r-", lw=5)
            # timeout 0.1s
            plt.pause(0.1)
