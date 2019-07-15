# Bert classification（with word weights）

* Code from: https://github.com/google-research/bert
* Main changes at : "run_classifier.py"
    1. Add class "ChiProcessor" : https://github.com/MagicianQi/bert_classification/blob/master/run_classifier.py#L428
    2. Modify classification model : https://github.com/MagicianQi/bert_classification/blob/master/run_classifier.py#L658
    3. Write word weights for Test : https://github.com/MagicianQi/bert_classification/blob/master/run_classifier.py#L1062


## Environment

* Python 3.6.5 | Anaconda, Inc.
* tensorflow >= 1.11.0   # CPU Version of TensorFlow.
* tensorflow-gpu  >= 1.11.0  # GPU version of TensorFlow.

## Data

* One line is one piece of data, Format : "$label\t$text"
* The method of constructing data set can be seen in class "run_classifier.py"-"ChiProcessor" or `head ./data/news.train`

## Hyper-parameter in *.sh

* DATA_DIR : DIR of Training set、test set、validation set
* BERT_BASE_DIR : Bert pre-train word vectors and checkpoint
* CUDA_VISIBLE_DEVICES : GPU device ID
* TRAINED_CLASSIFIER : Directory of trained models

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
* Result ("./output/"): 
    * Eval result : `eval_results.txt`
    * Test result : `test_results.tsv`
* Evaluate weights:
    * `python evaluate_weights.py`
