#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import os
import pandas as pd
from tqdm import tqdm
from random import shuffle
import cv2

LR = 1e-3  # learning rate
MODEL_NAME = 'plantclassfication-{}-{}.model'.format(LR, '2conv-basic')  # just so we remember which save
datadir = 'E:\\python\\Practice\\Ml\\KaggleLearning\\plant-seedlings-classification\\'
train_dir = os.path.join(datadir, 'train')
test_dir = os.path.join(datadir, 'test')
tensorboard_dir = os.path.join(datadir, 'log')
IMG_SIZE = 128

# list of categories in array format
CATEGORIES = ['Black-grass', 'Charlock', 'Cleavers', 'Common Chickweed', 'Common wheat', 'Fat Hen', 'Loose Silky-bent',
              'Maize', 'Scentless Mayweed', 'Shepherds Purse', 'Small-flowered Cranesbill', 'Sugar beet']
NUM_CATEGORIES = len(CATEGORIES)


def label_img(word_label):
    if word_label == 'Black-grass':
        return [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif word_label == 'Charlock':
        return [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif word_label == 'Cleavers':
        return [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif word_label == 'Common Chickweed':
        return [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    elif word_label == 'Common wheat':
        return [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    elif word_label == 'Fat Hen':
        return [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    elif word_label == 'Loose Silky-bent':
        return [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    elif word_label == 'Maize':
        return [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    elif word_label == 'Scentless Mayweed':
        return [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    elif word_label == 'Shepherds Purse':
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    elif word_label == 'Small-flowered Cranesbill':
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    elif word_label == 'Sugar beet':
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]


def create_train_data():
    train = []
    for category_id, category in enumerate(CATEGORIES):
        for img in tqdm(os.listdir(os.path.join(train_dir, category))):
            label = label_img(category)
            path = os.path.join(train_dir, category, img)
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            train.append([np.array(img), np.array(label)])
    shuffle(train)
    return train


train_data = create_train_data()


def create_test_data():
    test = []
    for img in tqdm(os.listdir(test_dir)):
        path = os.path.join(test_dir, img)
        img_num = img
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        test.append([np.array(img), img_num])

    shuffle(test)
    return test


test_data = create_test_data()

import tensorflow as tf
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import fully_connected, input_data, dropout
from tflearn.layers.estimator import regression

tf.reset_default_graph()

convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 1], name='input')

'''
conv_2d
S=Stride（default=1）
1、如果padding = ‘VALID’

new_height = new_width = (W – F + 1) / S （结果向上取整）
也就是说，conv2d的VALID方式不会在原有输入的基础上添加新的像素（假定我们的输入是图片数据，因为只有图片才有像素），输出矩阵的大小直接按照公式计算即可。

2、如果padding = ‘SAME’

new_height = new_width = W / S （结果向上取整）

'''

# conv1,default padding=same
convnet = conv_2d(convnet, nb_filter=32, filter_size=5, activation='relu')
# max pooling整个图片被不重叠的分割成若干个同样大小的小块（pooling size）。每个小块内只取最大的数字，再舍弃其他节点后，保持原有的平面结构得出 output。
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 64, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

# convnet = conv_2d(convnet, 32, 5, activation='relu')
# convnet = max_pool_2d(convnet, 5)
#
# convnet = conv_2d(convnet, 64, 5, activation='relu')
# convnet = max_pool_2d(convnet, 5)
#
# convnet = conv_2d(convnet, 32, 5, activation='relu')
# convnet = max_pool_2d(convnet, 5)
#
# convnet = conv_2d(convnet, 64, 5, activation='relu')
# convnet = max_pool_2d(convnet, 5)

convnet = fully_connected(convnet, 1024, activation='relu')
convnet = dropout(convnet, 0.8)

convnet = fully_connected(convnet, 12, activation='softmax')
convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

model = tflearn.DNN(convnet, tensorboard_dir=tensorboard_dir)

if os.path.exists('{}.meta'.format(MODEL_NAME)):
    model.load(MODEL_NAME)
    print('model loaded!')

train = train_data
test = train_data

train_x = np.array([i[0] for i in train]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
train_y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
test_y = [i[1] for i in test]

# 当一个完整的数据集通过了神经网络一次并且返回了一次，这个过程称为一个 epoch。
model.fit({'input': train_x}, {'targets': train_y}, n_epoch=5, validation_set=({'input': test_x}, {'targets': test_y}),
          snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

model.save(MODEL_NAME)


# return Indexes of the maximal elements of a array
def label_return(model_out):
    if np.argmax(model_out) == 0:
        return 'Black-grass'
    elif np.argmax(model_out) == 1:
        return 'Charlock'
    elif np.argmax(model_out) == 2:
        return 'Cleavers'
    elif np.argmax(model_out) == 3:
        return 'Common Chickweed'
    elif np.argmax(model_out) == 4:
        return 'Common wheat'
    elif np.argmax(model_out) == 5:
        return 'Fat Hen'
    elif np.argmax(model_out) == 6:
        return 'Loose Silky-bent'
    elif np.argmax(model_out) == 7:
        return 'Maize'
    elif np.argmax(model_out) == 8:
        return 'Scentless Mayweed'
    elif np.argmax(model_out) == 9:
        return 'Shepherds Purse'
    elif np.argmax(model_out) == 10:
        return 'Small-flowered Cranesbill'
    elif np.argmax(model_out) == 11:
        return 'Sugar beet'


import matplotlib.pyplot as plt

fig = plt.figure(figsize=(18, 10))
for num, data in enumerate(test_data[:12]):
    img_num = data[1]
    img_data = data[0]
    y = fig.add_subplot(3, 4, num + 1)
    orig = img_data
    data = img_data.reshape(IMG_SIZE, IMG_SIZE, 1)
    model_out = model.predict([data])[0]
    str_label = label_return(model_out)
    y.imshow(orig, cmap='gray', interpolation='nearest')
    plt.title(str_label)
    y.axes.get_xaxis().set_visible(False)
    y.axes.get_yaxis().set_visible(False)
plt.show()

sample_submission = pd.read_csv(os.path.join(datadir, 'sample_submission.csv', 'sample_submission.csv'))
sample_submission.head(2)

with open(os.path.join(datadir, 'submission.csv'), 'w') as f:
    f.write('file,species\n')
    for data in test_data:
        img_num = data[1]
        img_data = data[0]
        orig = img_data
        data = img_data.reshape(IMG_SIZE, IMG_SIZE, 1)
        model_out = model.predict([data])[0]
        str_label = label_return(model_out)
        file = img_num
        species = str_label
        row = file + "," + species + "\n"
        f.write(row)

submission = pd.read_csv(os.path.join(datadir, 'submission.csv'))
submission.head(10)
