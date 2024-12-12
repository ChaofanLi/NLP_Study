# -*- coding: utf-8 -*-

"""
配置参数信息
"""

Config = {
    "model_path": r"G:\NLP\Code\NLP_Code\8_序列标注任务\NER\model_output",
    "schema_path": r"G:\NLP\Code\NLP_Code\8_序列标注任务\NER\ner_data\schema.json",
    "train_data_path": r"G:\NLP\Code\NLP_Code\8_序列标注任务\NER\ner_data\train",
    "valid_data_path": r"G:\NLP\Code\NLP_Code\8_序列标注任务\NER\ner_data\test",
    "vocab_path":r"G:\NLP\Code\NLP_Code\8_序列标注任务\NER\chars.txt",
    "max_length": 100,
    "hidden_size": 512,
    "num_layers": 4,
    "epoch": 40,
    "batch_size": 16,
    "optimizer": "adam",
    "learning_rate": 5e-4,
    "use_crf": False,
    "class_num": 9,
    "bert_path": r"G:\NLP\pretrain_models\bert-base-chinese"
}

