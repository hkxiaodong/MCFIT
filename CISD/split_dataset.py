import csv

import numpy as np
import random
import os
import shutil
import math
from tqdm import tqdm
csv_path = './all_image-text_label.csv'

_0 = []
_1 = []
_2 = []

with open(csv_path, encoding='utf-8') as csv_f:
    reader = csv.reader(csv_f)
    header = next(reader)
    for row in tqdm(reader):
        id, label, url, caption = row[0], row[1], row[2], row[3]
        caption = caption.replace('\r', '').replace('\n', '').replace('\t', '')
        if label == '0':
            _0.append((id, label, caption))
        if label == '1':
            _1.append((id, label, caption))
        if label == '2':
            _2.append((id, label, caption))

train_set = _0[:math.floor(len(_0)*0.8)] +\
            _1[:math.floor(len(_1)*0.8)] +\
            _2[:math.floor(len(_2)*0.8)]

test_set = _0[math.floor(len(_0)*0.8):math.floor(len(_0)*0.9)] +\
           _1[math.floor(len(_1)*0.8):math.floor(len(_1)*0.9)] +\
           _2[math.floor(len(_2)*0.8):math.floor(len(_2)*0.9)]

valid_set = _0[math.floor(len(_0)*0.9):] + \
           _1[math.floor(len(_1)*0.9):] + \
           _2[math.floor(len(_2)*0.9):]


random.shuffle(train_set)
random.shuffle(test_set)
random.shuffle(valid_set)

data_path = './YNU-CISD/all_data/'

with open('./train_0.8.txt', 'a', encoding='utf-8') as f:
    for arr in tqdm(train_set):
        f.write(data_path + arr[0] + '.jpg' + '      ' + arr[1] + '      ' + arr[2] + '\n')

with open('./test_0.1.txt', 'a', encoding='utf-8') as f:
    for arr in tqdm(test_set):
        f.write(data_path + arr[0] + '.jpg' + '      ' + arr[1] + '      ' + arr[2] + '\n')

with open('./valid_0.1.txt', 'a', encoding='utf-8') as f:
    for arr in tqdm(valid_set):
        f.write(data_path + arr[0] + '.jpg' + '      ' + arr[1] + '      ' + arr[2] + '\n')


# a = '''不愧是环球人物唯一连续四年撰写的专栏作家
# 王源老师不仅说话果敢有'''
#
# print(a)
# print(a.strip())
# row = a.replace('\r','').replace('\n','').replace('\t','')