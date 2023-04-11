# -*- coding: utf-8 -*-
# 导入相应的包
import os
import math
from itertools import chain #二维列表转一维列表
from six import iteritems  # iteritems()返回一个迭代器如"a 1    b 2"
import codecs  # 编码转换
import jieba.posseg as pseg  # 分词用
from gensim import corpora  # 设置id编码
from gensim.summarization import bm25

test_path = './中文信息检索任务数据集/测试集.txt'
original_query = [] #查询Q
processed_query = [] #分词后的查询Q

# 构建停用词表
stop_words = './cn_stopwords.txt'
stopwords = codecs.open(stop_words, 'r', encoding='utf8').readlines()
stopwords = [w.strip() for w in stopwords]
# jieba分词后的停用词性
# [标点符号、连词、助词、副词、介词、时语素、'的'、数词、方位词、代词]
stop_flag = ['x', 'c', 'u', 'd', 'p', 't', 'uj', 'm', 'f', 'r']

def tokenization(raw):
    result = []
    words = pseg.cut(raw)  # 分词
    for word, flag in words:
        if flag not in stop_flag and word not in stopwords:
            result.append(word)  # 虚词过滤
    return result

test_path = './中文信息检索任务数据集/测试集.txt'
with open(test_path, 'r', encoding='gb18030', errors='ignore') as f:
    for line in f:
        original_query.append(line)
        s = tokenization(line.strip())
        processed_query.append(s)
print(processed_query)
for sentence in processed_query:
    print(sentence)