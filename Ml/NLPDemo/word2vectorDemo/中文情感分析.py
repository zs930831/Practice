import numpy as np
import pandas as pd
import jieba
import os

# def load_file_and_preprocessing():
data_path = "E:\\python\Practice\\Ml\\NLPDemo\\word2vectorDemo\\Chinese-sentiment-analysis"
neg_word_path = os.path.join(data_path, 'neg.csv')
pos_word_path = os.path.join(data_path, 'pos.csv')
neg = pd.read_csv(neg_word_path, encoding='gb18030', header=None)
pos = pd.read_csv(pos_word_path, encoding='gb18030', header=None)

cw = lambda x: list(jieba.cut(x))
pos['words'] = pos[0].apply(cw)
neg['words'] = neg[0].apply(cw)

from sklearn.model_selection import train_test_split

train_data = np.concatenate((pos['words'], neg['words']), axis=0)
y = np.concatenate((np.ones(len(pos['words'])), np.zeros(len(neg['words']))), axis=0)
x_train, x_test, y_train, y_test = train_test_split(train_data, y, test_size=0.2)

np.save(os.path.join(data_path, 'y_train.npy'), y_train)
np.save(os.path.join(data_path, 'y_test.npy'), y_test)


# 对每一个句子的所有词取平均值，来生成一个句子的vector
def build_sentence_vector(text, size, imdb_w2v):
    vec = np.zeros(size).reshape((1, size))
    count = 0
    for word in text:
        try:
            vec += imdb_w2v[word].reshape((1, size))
            count += 1
        except KeyError:
            continue
    if count != 0:
        vec /= count
    return vec


from gensim.models.word2vec import Word2Vec


# 计算词向量
def get_train_vecs(x_train, x_test):
    n_dim = 300
    # 初始化模型和词表
    imdb_w2v = Word2Vec(size=n_dim, min_count=10)
    imdb_w2v.build_vocab(x_train)

    # 在评论训练集上建模(可能会花费几分钟)
    imdb_w2v.train(x_train)

    train_vecs = np.concatenate([build_sentence_vector(z, n_dim, imdb_w2v) for z in x_train])
    np.save(os.path.join(data_path, 'train_vecs.npy'), train_vecs)
    # 在测试集上训练
    imdb_w2v.train(x_test)
    imdb_w2v.save(os.path.join(data_path, 'w2v_model.pkl'))
    # Build test tweet vectors then scale
    test_vecs = np.concatenate([build_sentence_vector(z, n_dim, imdb_w2v) for z in x_test])
    # test_vecs = scale(test_vecs)
    np.save(os.path.join(data_path, 'test_vecs.npy'), test_vecs)


def get_data():
    train_vecs = np.load(os.path.join(data_path, 'train_vecs.npy'))
    y_train = np.load(os.path.join(data_path, 'y_train.npy'))
    test_vecs = np.load(os.path.join(data_path, 'test_vecs.npy'))
    y_test = np.load(os.path.join(data_path, 'y_test.npy'))
    return train_vecs, y_train, test_vecs, y_test


# train svm model
from sklearn.externals import joblib
from sklearn.svm import SVC


def svm_train(train_vecs, y_train, test_vecs, y_test):
    clf = SVC(kernel='rbf', verbose=True)
    clf.fit(train_vecs, y_train)
    joblib.dump(clf, os.path.join(data_path, 'model.pkl'))
    print(clf.score(test_vecs, y_test))


# 构造待预测的句子的向量
def get_predict_vecs(words):
    n_dim = 300
    imdb_w2v = Word2Vec.load(os.path.join(data_path, 'w2v_model.pkl'))
    # imdb_w2v.train(words)
    train_vecs = build_sentence_vector(words, n_dim, imdb_w2v)
    # print train_vecs.shape
    return train_vecs


# 对单个句子进行情感判断
def svm_predict(string):
    words = jieba.lcut(string)
    words_vecs = get_predict_vecs(words)
    clf = joblib.load(os.path.join(data_path, 'model.pkl'))

    result = clf.predict(words_vecs)

    if int(result[0]) == 1:
        print(string, ' positive')
    else:
        print(string, ' negative')


##对输入句子情感进行判断
string='电池充完了电连手机都打不开.简直烂的要命.真是金玉其外,败絮其中!连5号电池都不如'
#string='牛逼的手机，从3米高的地方摔下去都没坏，质量非常好'
svm_predict(string)