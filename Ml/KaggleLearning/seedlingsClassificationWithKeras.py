#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

import numpy as np
# 对图像进行简单处理的库比不上cv2
from PIL import Image, ImageOps
from sklearn.preprocessing import LabelBinarizer
from tqdm import tqdm

datadir = 'E:\\python\\Practice\\Ml\\KaggleLearning\\plant-seedlings-classification\\'
train_dir = os.path.join(datadir, 'train')
test_dir = os.path.join(datadir, 'test')

IMG_SIZE = 48
IMG_CHANNELS = 3
# list of categories in array format
CATEGORIES = ['Black-grass', 'Charlock', 'Cleavers', 'Common Chickweed', 'Common wheat', 'Fat Hen', 'Loose Silky-bent',
              'Maize', 'Scentless Mayweed', 'Shepherds Purse', 'Small-flowered Cranesbill', 'Sugar beet']
NUM_CATEGORIES = len(CATEGORIES)

ori_images = []
ori_label = []
for category_id, category in enumerate(CATEGORIES):
    for img in tqdm(os.listdir(os.path.join(train_dir, category))):
        ori_label.append(category)
        path = os.path.join(train_dir, category, img)
        new_img = Image.open(path)
        '''
        Image.NEAREST	低质量
        Image.BILINEAR	双线性
        Image.BICUBIC 	三次样条插值
        Image.ANTIALIAS	高质量
        '''
        ori_images.append(ImageOps.fit(new_img, (IMG_SIZE, IMG_SIZE), Image.ANTIALIAS).convert('RGB'))

# ori_images[1]
imgs = np.array([np.array(im) for im in ori_images])
# 标准化
imgs = imgs.reshape(imgs.shape[0], IMG_SIZE, IMG_SIZE, IMG_CHANNELS) / 255
# 别用fit_transform,不然下面的用不了逆
lb = LabelBinarizer().fit(ori_label)
label = lb.transform(ori_label)
from  sklearn.model_selection import train_test_split

trainX, validX, trainY, validY = train_test_split(imgs, label, test_size=0.05, random_state=42, shuffle=True)

from keras.layers import Dropout, Input, Dense, Activation, GlobalMaxPooling2D, BatchNormalization, Conv2D, \
    MaxPooling2D
from keras.models import Model, load_model
from keras.optimizers import Adam

IM_input = Input(shape=(IMG_SIZE, IMG_SIZE, IMG_CHANNELS))
IM = Conv2D(filters=16, kernel_size=(3, 3), padding='valid')(IM_input)
# 整数，指定要规范化的轴，通常为特征轴,这里为什么为3呢？
IM = BatchNormalization(axis=3)(IM)
IM = Activation(activation='relu')(IM)

IM = Conv2D(filters=16, kernel_size=(3, 3), padding='valid')(IM)
# 整数，指定要规范化的轴，通常为特征轴
IM = BatchNormalization(axis=3)(IM)
IM = Activation(activation='relu')(IM)
IM = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(IM)

IM = Conv2D(filters=16, kernel_size=(3, 3), padding='valid')(IM)
# 整数，指定要规范化的轴，通常为特征轴
IM = BatchNormalization(axis=3)(IM)
IM = Activation(activation='relu')(IM)

IM = Conv2D(filters=16, kernel_size=(3, 3), padding='valid')(IM)
# 整数，指定要规范化的轴，通常为特征轴
IM = BatchNormalization(axis=3)(IM)
IM = Activation(activation='relu')(IM)
# Global Average Pooling一般用于放在网络的最后，用于替换全连接FC层
IM = GlobalMaxPooling2D()(IM)

IM = Dense(64, activation='relu')(IM)
IM = Dropout(0.5)(IM)
IM = Dense(32, activation='relu')(IM)
IM = Dropout(0.5)(IM)
IM = Dense(12, activation='softmax')(IM)

model = Model(inputs=IM_input, outputs=IM)
model.summary()
# lr is should shrink
# 1e-4:acc=0.5420
# 1e-6:acc=0.6303
model.compile(optimizer=Adam(lr=1e-6), loss='categorical_crossentropy', metrics=['acc'])

from keras.callbacks import LearningRateScheduler, EarlyStopping
from keras.callbacks import ModelCheckpoint

batch_size = 64
# 该回调函数是学习率调度器
annealer = LearningRateScheduler(lambda x: 1e-3 * 0.9 ** x)
# 当监测值不再改善时，该回调函数将中止训练,
# patience：当early stop被激活（如发现loss相比上一个epoch训练没有下降），则经过patience个epoch后停止训练。
earlystop = EarlyStopping(patience=10)
# 该回调函数将在每个epoch后保存模型到filepath
filepath = os.path.join(datadir, 'model', 'model.h5')
modelsave = ModelCheckpoint(filepath=filepath, save_best_only=True, verbose=1)
model.fit(
    trainX, trainY, batch_size=batch_size,
    epochs=200,
    validation_data=(validX, validY),
    callbacks=[annealer, earlystop, modelsave]
)

# 创建预测的数据
test_images = []
names = []
for img in tqdm(os.listdir(test_dir)):
    path = os.path.join(test_dir, img)
    names.append(img)
    new_img = Image.open(path)
    '''
    Image.NEAREST	低质量
    Image.BILINEAR	双线性
    Image.BICUBIC 	三次样条插值
    Image.ANTIALIAS	高质量
    '''
    test_images.append(ImageOps.fit(new_img, (IMG_SIZE, IMG_SIZE), Image.ANTIALIAS).convert('RGB'))

model = load_model(filepath=filepath)

timgs = np.array([np.array(im) for im in test_images])
testX = timgs.reshape(timgs.shape[0], IMG_SIZE, IMG_SIZE, IMG_CHANNELS) / 255

yhat = model.predict(testX)
# one_hot->category
test_y = lb.inverse_transform(yhat)

import pandas as pd

df = pd.DataFrame(data={'file': names, 'species': test_y})
df_sort = df.sort_values(by=['file'])
df_sort.to_csv(os.path.join(datadir, 'keras_sub_4_9.csv'), index=False)

sub = pd.read_csv(os.path.join(datadir, 'keras_sub_4_9.csv'))
sub.head(10)
