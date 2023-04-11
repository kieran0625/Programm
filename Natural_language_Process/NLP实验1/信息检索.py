'''
NLP 信息检索程序实现
实现步骤：
(1)文件预处理：文本导入，分词，虚词过滤(停用词表下载连接：https://github.com/goto456/stopwords)
(2)文本指引：文本特征选择，权重计算TF-IDF方法，编码为向量矩阵
(3)相似度估计：相似度计算，排序
'''
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


# 构建停用词表
stop_words = './cn_stopwords.txt'
stopwords = codecs.open(stop_words, 'r', encoding='utf8').readlines()
stopwords = [w.strip() for w in stopwords]
# jieba分词后的停用词性
# [标点符号、连词、助词、副词、介词、时语素、'的'、数词、方位词、代词]
stop_flag = ['x', 'c', 'u', 'd', 'p', 't', 'uj', 'm', 'f', 'r']

# 进行分词和虚拟此过滤


def tokenization(filename):
    result = []
    with open(filename, 'r', encoding='gb18030', errors='ignore') as f:  # TODO: 编码我要哭死，直接忽略吧
        text = f.read()
        words = pseg.cut(text)  # 分词
    for word, flag in words:
        if flag not in stop_flag and word not in stopwords:
            result.append(word)  # 虚词过滤
    return result


class TF_IDF(object):
    def __init__(self, corpus):
        self.f = []
        self.df = {}
        self.idf={} # 计算tf值
        self.tf = {}  # 计算idf值
        self.corpus = corpus
        self.corpus_size = len(corpus)

    def initialize(self):
        for document in corpus:
            frequencies = {}
            for word in document:
                if word not in frequencies:
                    frequencies[word] = 0
                frequencies[word] += 1
            for word in frequencies:
                self.tf[word] = frequencies[word]/len(frequencies)
            self.f.append(frequencies)
            for word, freq in iteritems(frequencies):
                if word not in self.df:
                    self.df[word] = 0
                self.df[word] += 1  # 计算包含word的文档数

        for word, freq in iteritems(self.df): # freq为包含了word的文档个数
            self.idf[word] = math.log(self.corpus_size) - math.log(freq+1.0) # IDF

    def get_tfidf(self,document,index):
        tfidf = 0
        for word in document:
            idf = self.idf[word]
            tfidf += idf * (self.f[index][word] / len(self.f[index]))
        return tfidf
    
    def get_tfidfs(self, document):
        tfidfs = []
        for index in range(self.corpus_size):
            tfidf = self.get_tfidf(document, index)
            tfidfs.append(tfidf)
        return tfidfs

def tfidfs_weigit(corpus):
    TF_IDF_Moel = TF_IDF(corpus)

    weights = []
    for doc in corpus:
        scores = TF_IDF_Moel.get_tfidfs(doc)
        weights.append(scores)

    return weights

if __name__ == "__main__":
    corpus = []
    rootname = 'C:\\Users\\kieran\\Desktop\\项目代码\\Natural_language_Process\\NLP实验1\\中文信息检索任务数据集\\训练集'
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
            #print(file_name)
            corpus.append(tokenization(file_name))
    dictionary = corpora.Dictionary(corpus)
    TfidfModel = bm25.BM25(corpus)
    # print(len(corpus)) # 文档个数
    # print("========================================================")
    # print(dictionary.token2id) # 单词与编号之间的映射关系
    # print("----------------------------------------------------------------")
    # print(len(dictionary)) # 单词总数

    tfidfModel = TF_IDF(corpus)
    
    query_str = '中国 女曲 能否 击败 韩国 圆梦'
    query = []
    for word in query_str.strip().split():
        query.append(word.encode('utf-8').decode('utf-8'))
    scores = TfidfModel.get_scores(query)
    # scores = TF_IDF.get_tfidfs(query)
    # scores.sort(reverse=True)
    print(scores)
    idx = scores.index(max(scores))
    print(idx)
    file = list(chain.from_iterable(filenames))
    fname = file[idx]
    print(fname)
    with open(fname,'r') as f:
        print(f.read())


'''
    上面这些步骤，我们利用gensim.corpora.dictionary.Dictionary类为每个出现在语料库中的单词分配了一个独一无二的
    整数编号id,这个操作收集了单词计数及其他相关的统计信息。

    # 列出1(0).txt文件中排名前5的words
    doc_vectors = [dictionary.doc2bow(text) for text in corpus]
    vec1 = doc_vectors[0]
    vec1_sorted = sorted(vec1, key=lambda x_y:x_y[1], reverse=True)
    print(len(vec1_sorted))
    for term, freq in vec1_sorted[:5]:
        print(dictionary[term])
'''
