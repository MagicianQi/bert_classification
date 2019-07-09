# Bert 分类（带词权重）

* 代码来自https://github.com/google-research/bert
* 主要修改在run_classifier.py
    1. 增加ChiProcessor类：https://github.com/MagicianQi/bert_classification/blob/master/run_classifier.py#L428
    2. 修改分类模型：https://github.com/MagicianQi/bert_classification/blob/master/run_classifier.py#L658
    3. Test时写词权重：https://github.com/MagicianQi/bert_classification/blob/master/run_classifier.py#L1062


## Environment

* Python 3.6.5 |Anaconda, Inc.
* tensorflow >= 1.11.0   # CPU Version of TensorFlow.
* tensorflow-gpu  >= 1.11.0  # GPU version of TensorFlow.

## How to use

* Get code : 
    * `git clone https://github.com/MagicianQi/bert_classification`
* Download and unzip model : 
    * `cd bert_classification && mkdir models && cd models`
    * `wget https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip && unzip chinese_L-12_H-768_A-12.zip && cd ../`
* Train and Eval : 
    * `bash train_eval.sh`
* Test : 
    * `bash predict.sh`
