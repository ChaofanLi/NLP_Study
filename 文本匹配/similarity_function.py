import numpy as np
import jieba
import json
import math
import os
import pickle
import sys
from typing import Dict, List

'''

包含编辑距离和jaccard距离的实现

'''

#编辑距离
def editing_distance(string1, string2):
    matrix = np.zeros((len(string1) + 1, len(string2) + 1))
    for i in range(len(string1) + 1):
        matrix[i][0] = i
    for j in range(len(string2) + 1):
        matrix[0][j] = j
    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if string1[i - 1] == string2[j - 1]:
                d = 0
            else:
                d = 1
            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + d)
    edit_distance = matrix[len(string1)][len(string2)]
    return 1 - edit_distance / max(len(string1), len(string2))


#jaccard距离
def jaccard_distance(string1, string2):
    words1 = set(string1)
    words2 = set(string2)
    distance = len(words1 & words2) / len(words1 | words2)
    return distance

class BM25:
    EPSILON = 0.25
    PARAM_K1 = 1.5  # BM25算法中超参数
    PARAM_B = 0.6  # BM25算法中超参数

    def __init__(self, corpus: Dict):
        """
            初始化BM25模型
            :param corpus: 文档集, 文档集合应该是字典形式，key为文档的唯一标识，val对应其文本内容，文本内容需要分词成列表
        """

        self.corpus_size = 0  # 文档数量
        self.wordNumsOfAllDoc = 0  # 用于计算文档集合中平均每篇文档的词数 -> wordNumsOfAllDoc / corpus_size
        self.doc_freqs = {}  # 记录每篇文档中查询词的词频
        self.idf = {}  # 记录查询词的 IDF
        self.doc_len = {}  # 记录每篇文档的单词数
        self.docContainedWord = {}  # 包含单词 word 的文档集合
        self._initialize(corpus)


    def _initialize(self, corpus: Dict):
        """
            根据语料库构建倒排索引
        """
        # nd = {} # word -> number of documents containing the word
        for index, document in corpus.items():
            self.corpus_size += 1
            self.doc_len[index] = len(document)  # 文档的单词数
            self.wordNumsOfAllDoc += len(document)

            frequencies = {}  # 一篇文档中单词出现的频率
            for word in document:
                if word not in frequencies:
                    frequencies[word] = 0
                frequencies[word] += 1
            self.doc_freqs[index] = frequencies

            # 构建词到文档的倒排索引，将包含单词的和文档和包含关系进行反向映射
            for word in frequencies.keys():
                if word not in self.docContainedWord:
                    self.docContainedWord[word] = set()
                self.docContainedWord[word].add(index)

        # 计算 idf
        idf_sum = 0  # collect idf sum to calculate an average idf for epsilon value
        negative_idfs = []
        for word in self.docContainedWord.keys():
            doc_nums_contained_word = len(self.docContainedWord[word])
            idf = math.log(self.corpus_size - doc_nums_contained_word +
                           0.5) - math.log(doc_nums_contained_word + 0.5)
            self.idf[word] = idf
            idf_sum += idf
            if idf < 0:
                negative_idfs.append(word)

        average_idf = float(idf_sum) / len(self.idf)
        eps = BM25.EPSILON * average_idf
        for word in negative_idfs:
            self.idf[word] = eps

    @property
    def avgdl(self):
        return float(self.wordNumsOfAllDoc) / self.corpus_size


    def get_score(self, query: List, doc_index):
        """
        计算查询 q 和文档 d 的相关性分数
        :param query: 查询词列表
        :param doc_index: 为语料库中某篇文档对应的索引
        """
        k1 = BM25.PARAM_K1
        b = BM25.PARAM_B
        score = 0
        doc_freqs = self.doc_freqs[doc_index]
        for word in query:
            if word not in doc_freqs:
                continue
            score += self.idf[word] * doc_freqs[word] * (k1 + 1) / (
                    doc_freqs[word] + k1 * (1 - b + b * self.doc_len[doc_index] / self.avgdl))
        return [doc_index, score]

    def get_scores(self, query):
        scores = [self.get_score(query, index) for index in self.doc_len.keys()]
        return scores




if __name__ == "__main__":
    a = "abcd"
    b = "acde"
    print(editing_distance(a, b))
    print(jaccard_distance(a, b))