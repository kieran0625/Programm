import jieba
import os
import numpy as np

def tokenizer(s): #分词
    words = []
    cut = jieba.cut(s)
    for word in cut:
        if word not in stopwords and word != ' ':
            words.append(word)
    return words
def cosSimilaryty(q1,q2):
    qSize = q1.shape[0]
    nums = 0
    nums1 = 0
    nums2 = 0
    for i in range(qSize):
        nums = nums + q1[i]*q2[i]
        nums1 = nums1 + q1[i]*q1[i]
        nums2 = nums2 + q2[i]*q2[i]
    return nums/np.sqrt(nums1*nums2)


if __name__=="__main__":
    stopwords_path = 'D:/test/stopwords1893_cn.txt'
    stopwords = [] #停用词列表
    with open(stopwords_path, 'r', encoding='utf-8') as f:
        for line in f:
            if len(line) > 0:
                stopwords.append(line.strip())

    path = 'D:/NLP实验1/中文信息检索任务数据集/训练集'
    files = os.listdir(path)
    train_data=[] #将文档集合存入列表中
    paths = [] #路径集合
    for file in files:
        position = path+'/'+file
        ffiles = os.listdir(position)
        for ffile in ffiles:
            last_path = position + '/' + ffile
            paths.append(last_path)
            with open(last_path, 'r', encoding='gb18030', errors='ignore') as f:
                train1 = []
                for line in f:
                    s = tokenizer(line.strip())
                    train1.extend(s)
                train_data.append(train1)

    features = [] #特征词列表
    for file in train_data:
        for word in file:
            if word not in features:
                features.append(word)

    tf_idf = [] #特征权值
    for word in features:  #特征词
        tf_idf_i = []
        num = 0  #包含该词的文档的数量
        for file in train_data:
            if word in file:
                num = num + 1
        idf = np.log(len(train_data)/(num+1)) #计算idf值
        for file in train_data:
            tf = file.count(word) / len(file) #计算tf值
            tf_idf_i.append(tf*idf)
        tf_idf.append(tf_idf_i)
    original_query = [] #查询Q
    processed_query = [] #分词后的查询Q
    test_path = 'D:/NLP实验1/中文信息检索任务数据集/测试集.txt'
    with open(test_path, 'r', encoding='gb18030', errors='ignore') as f:
        for line in f:
            original_query.append(line)
            s = tokenizer(line.strip())
            processed_query.append(s)
    query_tf_idf = [] #计算查询向量的特征权重
    for sentence in processed_query:
        q_tf_idf = []
        for word in features:
            num = 1  # 包含该词的文档的数量
            for file in train_data:
                if word in file:
                    num = num + 1
            idf = np.log(len(train_data)/num)
            tf = sentence.count(word)/len(sentence)
            q_tf_idf.append(idf*tf)
        query_tf_idf.append(q_tf_idf)
    tf_idf = np.array(tf_idf)
    query_tf_idf = np.array(query_tf_idf)
    tf_idf = np.transpose(tf_idf)
    #相似度计算
    for i in range(query_tf_idf.shape[0]):
        similarity = []
        for j in range(tf_idf.shape[0]):
            Similarity_Path = []
            Similarity_Path.append(cosSimilaryty(query_tf_idf[i], tf_idf[j]))
            Similarity_Path.append(paths[j])
            similarity.append(Similarity_Path)
        similarity = sorted(similarity, key=lambda x: x[0], reverse=True) #相似度排序
        print('------------------------------------------------------')
        print('第%d次查询为:' % (i+1), end='')
        print(original_query[i])
        print('所在地址为:', end='')
        print(similarity[0][1])
        print('相似度为:', end='')
        print(similarity[0][0])
        print('查询结果为:')
        with open(similarity[0][1], 'r', encoding='gb18030', errors='ignore') as f:
            for line in f:
                print(line,end='')
        print('------------------------------------------------------')








