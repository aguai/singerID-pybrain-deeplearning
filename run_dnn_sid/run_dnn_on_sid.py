__author__ = 'zhangxulong'

import dnn
import time
from bulid_dataset import load_dataset
# time_start
timestart = time.time()
# trainset, validset, testset = music_preprocess.load_dataset("sid.pkl")
trainset, validset, testset = load_dataset("mfcc_sid.pkl")
# train
train_data = trainset[0]
train_target = trainset[1]

# set the layers parm,and the max is 8 now
layers = [95, 1000, 1000, 1000,1000,1]
# run the dnn ,first autoencoder and then DNNRegressor
autoencoder = dnn.AutoEncoder(train_data, train_data, train_target, layers, hidden_layer="TanhLayer", final_layer="TanhLayer", compression_epochs=5, bias=True, autoencoding_only=True)
autoencoder.fit()
# time end
timeend = time.time()
# train time
traintime = timeend - timestart