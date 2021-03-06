#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tensorflow as tf
import numpy as np

#save to file
#remember to define the same dtype and shape when restore

# W=tf.Variable([[1,2,3],[3,4,5]],dtype=tf.float32,name='weights')
# bias=tf.Variable([[1,2,3]],dtype=tf.float32,name='biases')
#
# init=tf.global_variables_initializer()
#
# saver=tf.train.Saver()
#
# with tf.Session() as mySess:
#     mySess.run(init)
#     save_path=saver.save(mySess,"my_net/save_net.ckpt")
#     print("Save to path:",save_path)

#restore variable
#redefine the same dtype and shape for your variable

W=tf.Variable(np.arange(6).reshape((2,3)),dtype=tf.float32,name='weights')
bias=tf.Variable(np.arange(3).reshape((1,3)),dtype=tf.float32,name='biases')

#not need init step
saver=tf.train.Saver()

with tf.Session() as mySess:
    saver.restore(mySess,"my_net/save_net.ckpt")
    print('weights:',mySess.run(W))
    print('bias:', mySess.run(bias))
