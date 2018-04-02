#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 从我网上下载数据
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


def compute_accuracy(v_xs, v_ys):
    global prediction
    # get an 1x10 vector distribution from 0 to 1,最大的概率的地方表示为要预测的数据
    y_pre = mySess.run(prediction, feed_dict={xs: v_xs, keep_prob: 0.5})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = mySess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys, keep_prob: 0.5})
    return result


def weight_variale(shape):
    # A tensor of the specified shape filled with random truncated normal values.
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variale(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    # stride[1,x_movement,y_movement,1]
    # Must have strides[0]=strides[3]=1
    # 'SAME'：不够的会填充,'VALID'：不够的舍弃
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    # Must have strides[0]=strides[3]=1,ksize（pool的窗口大小）也一样
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]), name="W")
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b  # no need to activate
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


# define placeholder for inputs
xs = tf.placeholder(tf.float32, [None, 784])
ys = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)
# -1表示sample的个数，1为黑白，3为彩色,28x28x1表示一张图片，batch是一次取多少图片
x_image = tf.reshape(xs, [-1, 28, 28, 1])
#print(x_image.shape)  # [n_samples,28,28,1]

# conv1 layer
# 5x5:patch(类似于扫描仪),1:in size（原始的图片厚度）,32:out size(输出图片的厚度，卷积核的个数，有多少个结果就有多高）
W_cov1 = weight_variale([5, 5, 1, 32])
b_cov1 = bias_variale([32])
# 输入乘以权重加上偏差！
h_conv1 = tf.nn.relu(conv2d(x_image, W_cov1) + b_cov1)  # outsize 28X28X32
h_pool1 = max_pool_2x2(h_conv1)  # 14x14x32

# conv2 layer，不断压扁
W_cov2 = weight_variale([5, 5, 32, 64])
b_cov2 = bias_variale([64])
# 输入乘以权重加上偏差！
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_cov2) + b_cov2)  # outsize 14X14X64
h_pool2 = max_pool_2x2(h_conv2)  # 7x7x64

# func1 layer
W_fc1 = weight_variale([7 * 7 * 64, 1024])
b_fc1 = bias_variale([1024])
# [n_samples,7,7,64]->>[n_samples,7*7*64]：3d->1d
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# func2 layer
W_fc2 = weight_variale([1024, 10])
b_fc2 = bias_variale([10])
# [n_samples,7,7,64]->>[n_samples,7*7*64]：3d->1d
prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

# the error between prediction and real data
# using softmax and cross_entropy to solve classification problem
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))

# 多的时候用这个。1e-4:1x10的-4次方
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

init = tf.global_variables_initializer()

# accuracy:86%
with tf.Session() as mySess:
    mySess.run(init)
    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(50)
        mySess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.5})
        if i % 50 == 0:
            print(compute_accuracy(mnist.test.images[:5000], mnist.test.labels[:5000]))
