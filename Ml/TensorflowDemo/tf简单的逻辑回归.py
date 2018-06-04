import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data",one_hot=True)

#参数定义
learning_rate = 0.01
training_epoch = 25
batch_size = 100
display_step=1

x=tf.placeholder(tf.float32,[None,784])
y=tf.placeholder(tf.float32,[None,10])

#变量定义
W=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))

#计算预测值
pred = tf.nn.softmax(tf.matmul(x,W)+b)
#计算损失值 使用相对熵计算损失值
cost=tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred),reduction_indices=1))
#定义优化器
optimizer=tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
#初始化所有变量值
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(training_epoch):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        for i in range(total_batch):
            batch_xs,batch_ys=mnist.train.next_batch(batch_size)
            _,c=sess.run([optimizer,cost],feed_dict={x:batch_xs,y:batch_ys})
            avg_cost+=c/total_batch
        if (epoch+1)%display_step==0:
            print ("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))
    print ("Optimization Finished!")

    # Test model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Calculate accuracy for 3000 examples
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print ("Accuracy:", accuracy.eval({x: mnist.test.images[:3000], y: mnist.test.labels[:3000]}))