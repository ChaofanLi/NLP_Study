# -*- coding: utf-8 -*-

"""
配置参数信息
"""

Config = {
    "model_path": r"G:\NLP\Code\NLP_Code\8_序列标注任务\添加标点\model_output",
    "schema_path": r"G:\NLP\Code\NLP_Code\8_序列标注任务\添加标点\dataset\schema.json",
    "train_data_path": r"G:\NLP\Code\NLP_Code\8_序列标注任务\添加标点\dataset\train_corpus",
    "valid_data_path": r"G:\NLP\Code\NLP_Code\8_序列标注任务\添加标点\dataset\valid_corpus",
    "vocab_path":r"G:\NLP\Code\NLP_Code\8_序列标注任务\添加标点\chars.txt",
    "max_length": 50,
    "hidden_size": 128,
    "epoch": 10,
    "batch_size": 128,
    "optimizer": "adam",
    "learning_rate": 1e-3,
    "use_crf": False,
    "class_num": None
}
