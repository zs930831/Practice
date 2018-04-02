#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# 从我网上下载数据
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

#hyperparameters
lr=0.001
batch_size=128

n_input=28#img shape:28x28
n_steps=28#time steps
n_hidden_units=128#neurons in hidden layer
n_classes=10#MNIST classes(0-9digits)


#tf Graph input
xs=tf.placeholder(tf.float32,[None,n_steps,n_input])
ys=tf.placeholder(tf.float32,[None,n_classes])

#Define weights
weights={
    #28x128
    'in':tf.Variable(tf.random_normal([n_input,n_hidden_units])),
    #128x10
    'out':tf.Variable(tf.random_normal([n_hidden_units,n_classes]))
}

biases={
    #(128,1)
    'in':tf.Variable(tf.constant(0.1,shape=[n_hidden_units,])),
    #10
    'out':tf.Variable(tf.constant(0.1,shape=[n_classes,]))
}



def RNN(X,weights,biases):
    #hidden layer for input to cell
    #X(128batch,28steps,28inputs)=>(128*28,28)
    X=tf.reshape(X,[-1,n_input])
    # ==>(128batch*28steps,128hidden)
    X_in=tf.matmul(X,weights['in'])+biases['in']
    #==>(128batch,28steps,128hidden)
    X_in=tf.reshape(X_in,[-1,n_steps,n_hidden_units])

    #cell
    lstm_cell=tf.nn.rnn_cell.BasicLSTMCell(n_hidden_units,forget_bias=1.0,state_is_tuple=True)
    #lstm cell is divided into two parts(c_state,m_state):cell被分成主线和分线的一个元组
    _init_state=lstm_cell.zero_state(batch_size=batch_size,dtype=tf.float32)
    #time_major表示time_step是不是在X_in的第0个位置
    outputs,states=tf.nn.dynamic_rnn(lstm_cell,X_in,initial_state=_init_state,time_major=False)

    #hidden layer for output to the final results
    #states[1]:m_state
    results = tf.matmul(states[1], weights['out']) + biases['out']
    return results


prediction=RNN(xs,weights,biases)
#cross_entropy=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=prediction,logits=ys))
cross_entropy=tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(lr).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(ys, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

init = tf.global_variables_initializer()

# accuracy:86%
with tf.Session() as mySess:
    mySess.run(init)
    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        batch_xs=batch_xs.reshape([batch_size,n_steps,n_input])
        mySess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys})
        if i % 50 == 0:
            print(mySess.run(accuracy,feed_dict={xs: batch_xs, ys: batch_ys}))