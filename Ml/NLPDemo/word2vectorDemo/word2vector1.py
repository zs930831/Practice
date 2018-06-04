#!/usr/bin/python
# -*- coding: UTF-8 -*-

# nltk.download()
# from nltk.corpus import brown
# print(brown.categories())


import nltk
# nltk.download()
# sentence="hello wxs"
# tokens=nltk.word_tokenize(sentence)
# print(tokens)

# import jieba
# #default cut_all=Flase
# seglist=jieba.cut('我来到北京清华大学',cut_all=True)
# print('/'.join(seglist))
# seglist=jieba.cut('我来到北京清华大学')
# print('/'.join(seglist))
# #serach_enginee model
# seglist=jieba.cut_for_search('我来到北京清华大学')
# print(','.join(seglist))

#处理网络语言
# import re
# emoticons_str = r"""
#     (?:
#         [:=;] # 眼睛
#         [oO\-]? # ⿐鼻⼦子
#         [D\)\]\(\]/\\OpP] # 嘴
#     )"""
# regex_str = [
#     emoticons_str,
#     r'<[^>]+>', # HTML tags
#     r'(?:@[\w_]+)', # @某⼈人
#     r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # 话题标签
#     r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',
#                    # URLs
#     r'(?:(?:\d+,?)+(?:\.?\d+)?)', # 数字
#     r"(?:[a-z][a-z'\-_]+[a-z])", # 含有 - 和 ‘ 的单词
#     r'(?:[\w_]+)', # 其他
#     r'(?:\S)' # 其他
# ]
# tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
# emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)
#
#
# def tokenize(s):
#     return tokens_re.findall(s)
#
#
# def preprocess(s, lowercase=False):
#     tokens = tokenize(s)
#     if lowercase:
#         tokens = [token if emoticon_re.search(token) else token.lower() for token in
#                   tokens]
#     return tokens
#
#
# tweet = 'RT @angelababy: love you baby! :D http://ah.love #168cm'
# print(preprocess(tweet))
# ['RT', '@angelababy', ':', 'love', 'you', 'baby',
# ’!', ':D', 'http://ah.love', '#168cm']

#词形归一化
from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer('english')
snowball_stemmer.stem('provision')

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
porter_stemmer.stem('maximum')

#NLTK实现Lemma
# 木有POS Tag，默认是NN 名词

from nltk.stem import WordNetLemmatizer
wnl=WordNetLemmatizer()
wnl.lemmatize("dogs")
wnl.lemmatize('churches')
#解决词性的问题
wnl.lemmatize('are')
wnl.lemmatize('are',pos="v")


#Nltk标注pos
text = nltk.word_tokenize('what does the fox say')
nltk.pos_tag(text)


#Stopwords
from nltk.corpus import stopwords
s='this is an apple'
token_list=nltk.word_tokenize(s)
filtered_words=[word for word in token_list if word not in stopwords.words('english')]




