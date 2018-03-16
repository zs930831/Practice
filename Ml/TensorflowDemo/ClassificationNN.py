#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# 从我网上下载数据
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]), name="W")
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b  # no need to activate
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

def compute_accuracy(v_xs,v_ys):
    global prediction
    #get an 1x10 vector distribution from 0 to 1,最大的概率的地方表示为要预测的数据
    y_pre=mySess.run(prediction,feed_dict={xs:v_xs})
    correct_prediction=tf.equal(tf.arg_max(y_pre,1),tf.arg_max(v_ys,1))
    accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    result=mySess.run(accuracy,feed_dict={xs:v_xs,ys:v_ys})
    return result


#define placeholder for inputs
xs=tf.placeholder(tf.float32,[None,784])
ys=tf.placeholder(tf.float32,[None,10])

#add output layer
prediction=add_layer(xs,784,10,activation_function=tf.nn.softmax)

#the error between prediction and real data
#using softmax and cross_entropy to solve classification problem
cross_entropy=tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=[1]))

train_step=tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init=tf.global_variables_initializer()

#accuracy:86%
with tf.Session() as mySess:
    mySess.run(init)
    for i in range(1000):
        batch_xs,batch_ys=mnist.train.next_batch(100)
        mySess.run(train_step,feed_dict={xs:batch_xs,ys:batch_ys})
        if i%50==0:
            print(compute_accuracy(mnist.test.images,mnist.test.labels))
