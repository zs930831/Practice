#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tensorflow as tf

matrix1=tf.constant([[3,3]])#constant value
matrix2=tf.constant([[2],[2]])

product=tf.matmul(matrix1,matrix2)

#method1
# sess=tf.Session()
# result=sess.run(product)
# print(result)
# sess.close()

#method
with tf.Session() as mySess:
    result2=mySess.run(product)
    print(result2)
