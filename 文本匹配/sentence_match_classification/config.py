# -*- coding: utf-8 -*-

"""
配置参数信息
""" 

Config = {
    "model_path": r"G:\NLP\Code\NLP_Code\7_文本匹配任务\sentence_match_as_sentence_encoder\model_output",
    "schema_path": r"G:\NLP\Code\NLP_Code\7_文本匹配任务\data\schema.json",
    "train_data_path": r"G:\NLP\Code\NLP_Code\7_文本匹配任务\data\train.json",
    "valid_data_path": r"G:\NLP\Code\NLP_Code\7_文本匹配任务\data\valid.json",
    "pretrain_model_path":r"G:\NLP\pretrain_models\bert-base-chinese",
    "vocab_path":r"G:\NLP\Code\NLP_Code\7_文本匹配任务\chars.txt",
    "max_length": 20,
    "hidden_size": 256,
    "epoch": 10,
    "batch_size": 128,
    "epoch_data_size": 10000,     #每轮训练中采样数量
    "positive_sample_rate":0.5,  #正样本比例
    "optimizer": "adam",
    "learning_rate": 1e-3,
}