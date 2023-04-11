#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU LGPL v2.1 - http://www.gnu.org/licenses/lgpl.html
import os
import math
from six import iteritems
import os
import numpy as np
import math
from six import iteritems  # iteritems()返回一个迭代器如"a 1    b 2"
import codecs  # 编码转换
import jieba.posseg as pseg  # 分词用
from gensim import corpora  # 设置id编码
from gensim.summarization import bm25
from itertools import chain

# BM25 parameters.
PARAM_K1 = 1.5
PARAM_B = 0.75
EPSILON = 0.25


class BM25(object):

    def __init__(self, corpus):
        self.corpus_size = len(corpus)
        self.corpus = corpus
        self.f = []
        self.df = {}
        self.idf = {}
        self.initialize()

    def initialize(self):
        for document in self.corpus:
            frequencies = {}
            for word in document:
                if word not in frequencies:
                    frequencies[word] = 0
                frequencies[word] += 1
            self.f.append(frequencies)

            for word, freq in iteritems(frequencies):
                if word not in self.df:
                    self.df[word] = 0
                self.df[word] += 1

        for word, freq in iteritems(self.df):
            self.idf[word] = math.log(self.corpus_size - freq + 0.5) - math.log(freq + 0.5)

#     def get_score(self, document, index, average_idf):
#         score = 0
#         for word in document:
#             if word not in self.f[index]:
#                 continue
#             idf = self.idf[word] if self.idf[word] >= 0 else EPSILON * average_idf
#             score += (idf * self.f[index][word] * (PARAM_K1 + 1)
#                       / (self.f[index][word] + PARAM_K1 * (1 - PARAM_B + PARAM_B * self.corpus_size / self.avgdl)))
#         return score

#     def get_scores(self, document, average_idf):
#         scores = []
#         for index in range(self.corpus_size):
#             score = self.get_score(document, index, average_idf)
#             scores.append(score)
#         return scores


# def get_bm25_weights(corpus):
#     bm25 = BM25(corpus)
#     average_idf = sum(map(lambda k: float(bm25.idf[k]), bm25.idf.keys())) / len(bm25.idf.keys())

#     weights = []
#     for doc in corpus:
#         scores = bm25.get_scores(doc, average_idf)
#         weights.append(scores)

#     return weights

# 构建停用词表
stop_words = './cn_stopwords.txt'
stopwords = codecs.open(stop_words, 'r', encoding='utf8').readlines()
stopwords = [w.strip() for w in stopwords]
# jieba分词后的停用词性
# [标点符号、连词、助词、副词、介词、时语素、'的'、数词、方位词、代词]
stop_flag = ['x', 'c', 'u', 'd', 'p', 't', 'uj', 'm', 'f', 'r']

def tokenization(filename):
    result = []
    with open(filename, 'r', encoding='gb18030', errors='ignore') as f:  # TODO: 编码我要哭死，直接忽略吧
        text = f.read()
        words = pseg.cut(text)  # 分词
    for word, flag in words:
        if flag not in stop_flag and word not in stopwords:
            result.append(word)  # 虚词过滤
    return result
def calculate_tfidf(document):
    f = []
    df = {}
    idf = {}
    tf = {}
    TFIDF = {}
    corpus_size = len(corpus)

    for document in corpus:
        frequencies = {}
        # print(len(document)) # 文档长度
        for word in document:
            if word not in frequencies:
                frequencies[word] = 0
            frequencies[word] += 1
        for word in frequencies:
            tf[word] = frequencies[word]/len(frequencies)

        f.append(frequencies)

        for word, freq in iteritems(frequencies):
            if word not in df:
                df[word] = 0
            df[word] += 1
    for word, freq in iteritems(df):
       idf[word] = math.log(corpus_size) - math.log(freq + 1)
       TFIDF[word] = idf[word]*tf[word]
    return TFIDF
    # print(idf)
    # print(tf)
    # print(TFIDF)
    # print(f)

if __name__ == '__main__':

    corpus = []
    rootname = 'C:\\Users\\kieran\\Desktop\\项目代码\\Natural_language_Process\\NLP实验1\\中文信息检索任务数据集\\训练集\\1'
    filenames = []  # 存放所有文件名
    file_dict = {}  # 存放所有子文件下的文件名

    for root, dirs, files in os.walk(rootname):
        filenames.append(files)
        file_dict[root] = files

    # print(file_dict) # 得到子文件夹
    # 遍历所有文件，拼接路径
    for k, v in file_dict.items():
        for i in v:
            file_name = os.path.join(k, i)
            # print(file_name)
            corpus.append(tokenization(file_name))
    dictionary = corpora.Dictionary(corpus)
    # print(corpus)

    query_str = '中国 女曲 能否 击败 韩国 圆梦'
    query = []
    for word in query_str.strip().split():
        query.append(word.encode('utf-8').decode('utf-8'))
    result = calculate_tfidf(query)
    # print(result)
    # print(filenames)
    b = list(chain.from_iterable(filenames))
    print(b)