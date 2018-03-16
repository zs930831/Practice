#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tensorflow as tf
state=tf.Variable(0,name='counter')
#print(state.name)
one=tf.constant(1)
#variable + constant=variable
new_value=tf.add(state,one)
update=tf.assign(state,new_value)

#variable needs to initialization
init=tf.global_variables_initializer()#must have if define variable

with tf.Session() as sess:
    #notice!
    sess.run(init)
    for i in range(3):
        sess.run(update)
        print(sess.run(state))