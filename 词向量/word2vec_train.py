
import json
import jieba
import numpy as np
import gensim
from gensim.models import Word2Vec
from collections import defaultdict

'''
词向量模型的简单实现
'''

#训练模型
def train_word2vec_model(corpus, dim):
    model = Word2Vec(corpus, vector_size=dim, sg=1)
    model.save("model.w2v")
    return model

#加载训练好的模型
def load_word2vec_model(path):
    model = Word2Vec.load(path)
    return model

def main():
    sentences = []
    with open(r"G:\NLP\Code\NLP_Code\3_词向量\corpus.txt", encoding="utf8") as f:
        for line in f:
            sentences.append(jieba.lcut(line))
    model = train_word2vec_model(sentences, 100)
    return model

if __name__ == "__main__":
    # model = main()  #训练

    model = load_word2vec_model(r"G:\NLP\Code\NLP_Code\3_词向量\model.w2v")  #加载
 
    print(model.wv.most_similar(positive=["北京", "上海"], negative=["经济"])) #类比

    while True:  #找相似
        string = input("input:")
        try:
            print(model.wv.most_similar(string))
        except KeyError:
            print("输入词不存在")