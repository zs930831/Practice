#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

# 从我网上下载数据
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# Visualize decoder setting
# paremeters
learning_rate = 0.001
training_epochs = 5
batch_size = 256
display_step = 1
examples_to_show = 10

# Network Parameters
n_input = 784  # img shape:28x28

# tf Graph input(only pictures)
X = tf.placeholder(tf.float32, [None, n_input])

# hidden layer settings
n_hidden_1 = 128  # 1st layer num features
n_hidden_2 = 64  # 2nd layer num features
n_hidden_3 = 10
n_hidden_4 = 2

weights = {
    'encoder_h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'encoder_h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'encoder_h3': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_3])),
    'encoder_h4': tf.Variable(tf.random_normal([n_hidden_3, n_hidden_4])),

    'decoder_h1': tf.Variable(tf.random_normal([n_hidden_4, n_hidden_3])),
    'decoder_h2': tf.Variable(tf.random_normal([n_hidden_3, n_hidden_2])),
    'decoder_h3': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_1])),
    'decoder_h4': tf.Variable(tf.random_normal([n_hidden_1, n_input]))
}

biases = {
    'encoder_h1': tf.Variable(tf.random_normal([n_hidden_1])),
    'encoder_h2': tf.Variable(tf.random_normal([n_hidden_2])),
    'encoder_h3': tf.Variable(tf.random_normal([n_hidden_3])),
    'encoder_h4': tf.Variable(tf.random_normal([n_hidden_4])),

    'decoder_h1': tf.Variable(tf.random_normal([n_hidden_3])),
    'decoder_h2': tf.Variable(tf.random_normal([n_hidden_2])),
    'decoder_h3': tf.Variable(tf.random_normal([n_hidden_1])),
    'decoder_h4': tf.Variable(tf.random_normal([n_input]))
}


# Building the enconder
def enconder(x):
    layer_1 = tf.nn.sigmoid(tf.matmul(x, weights['encoder_h1']) + biases['encoder_h1'])
    # Encoder Hidden layer with sigmoid activation
    layer_2 = tf.nn.sigmoid(tf.matmul(layer_1, weights['encoder_h2']) + biases['encoder_h2'])
    layer_3 = tf.nn.sigmoid(tf.matmul(layer_2, weights['encoder_h3']) + biases['encoder_h3'])
    # Encoder Hidden layer with sigmoid activation
    layer_4 = tf.matmul(layer_3, weights['encoder_h4']) + biases['encoder_h4']
    return layer_4


# Building the deconder
def deconder(x):
    layer_1 = tf.nn.sigmoid(tf.matmul(x, weights['decoder_h1']) + biases['decoder_h1'])
    # Decoder Hidden layer with sigmoid activation
    layer_2 = tf.nn.sigmoid(tf.matmul(layer_1, weights['decoder_h2']) + biases['decoder_h2'])
    layer_3 = tf.nn.sigmoid(tf.matmul(layer_2, weights['decoder_h3']) + biases['decoder_h3'])
    # Decoder Hidden layer with sigmoid activation
    layer_4 = tf.nn.sigmoid(tf.matmul(layer_3, weights['decoder_h4']) + biases['decoder_h4'])
    return layer_4


# Construct model
encoder_op = enconder(X)
decoder_op = deconder(encoder_op)

# prediction
y_pred = decoder_op
# Targets(Labels)are the input data
y_true = X

# Define loss and optimizer,minimize the squard error
cost = tf.reduce_mean(tf.pow(y_true - y_pred, 2))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

init = tf.global_variables_initializer()

with tf.Session() as mySess:
    mySess.run(init)
    total_batch = int(mnist.train.num_examples / batch_size)
    # Traing Cycle
    for epoch in range(training_epochs):
        # loop over all batches
        for i in range(total_batch):
            # max(x)=1,min(x)=0, has normalization
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # Run optimizer op(backprop)and cost op(to get loss value)
            _, c = mySess.run([optimizer, cost], feed_dict={X: batch_xs})

        # Display logs per epoch step
        # if epoch % display_step == 0:
        #     print("Epoch", "%4d" % (epoch + 1),
        #           "cost=", "{:.9f}".format(c))
    print("Optimizer Finished")

    encoder_result = mySess.run(encoder_op, feed_dict={X: mnist.test.images})
    # print(mnist.test.labels)
    # c为颜色
    # color=['r','b','green','yellow','orange','purple','grey','black','pink']
    plt.scatter(encoder_result[:, 0], encoder_result[:, 1], c=mnist.test.labels)
    plt.show()
