#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn import svm
from sklearn.metrics import accuracy_score

train_data = [[0, 0], [1, 0], [0, 1], [1, 1]]
train_label = [0, 1, 1, 0]
test_data = [[0, 0], [1, 0], [0, 1], [1, 1]]

clf = svm.SVC(C=10, gamma=0.1)
clf.fit(train_data,train_label)

test_label = clf.predict(test_data)
print("テストデータ：{0},予測ラベル：{1}".format(test_data,test_label))
print("正解率= {}".format(accuracy_score([0, 1, 1, 0], test_label)))
