#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

#load data
digits=load_digits()
X=digits.data
y=digits.target
y=LabelBinarizer().fit_transform(y)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.3)




def add_layer(inputs, in_size, out_size,layer_name, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]), name="W")
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    #dropout解决过拟合，hidden units过少的时候用的话会欠拟合。
    Wx_plus_b=tf.nn.dropout(Wx_plus_b,keep_prob)

    if activation_function is None:
        outputs = Wx_plus_b  # no need to activate
    else:
        outputs = activation_function(Wx_plus_b)
        tf.summary.histogram(layer_name + "/outputs", outputs)
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
keep_prob=tf.placeholder(tf.float32)#keep some not to drop out
xs=tf.placeholder(tf.float32,[None,64])#8x8
ys=tf.placeholder(tf.float32,[None,10])

#add output layer
l1=add_layer(xs,64,100,"hidden_layer1",activation_function=tf.nn.tanh)#hidden layer
prediction=add_layer(l1,100,10,"output_layer",activation_function=tf.nn.softmax)

#the error between prediction and real data
#using softmax and cross_entropy to solve classification problem
cross_entropy=tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=[1]))
tf.summary.scalar("loss",cross_entropy)#scalar：纯量（只有大小没有方向）
train_step=tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init=tf.global_variables_initializer()

with tf.Session() as mySess:
    #summary writer goes in here
    merged = tf.summary.merge_all()
    train_writer = tf.summary.FileWriter("logs/train", mySess.graph)
    test_writer = tf.summary.FileWriter("logs/test", mySess.graph)
    mySess.run(init)
    for i in range(1000):
        mySess.run(train_step,feed_dict={xs:X_train,ys:y_train,keep_prob:0.5})#
        if i%50==0:
            #record loss
            train_result=mySess.run(merged, feed_dict={xs: X_train, ys: y_train,keep_prob:1})
            test_result=mySess.run(merged,feed_dict={xs:X_test,ys:y_test,keep_prob:1})
            train_writer.add_summary(train_result,i)
            test_writer.add_summary(test_result,i)

