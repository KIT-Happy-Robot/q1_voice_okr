#!/usr/bin/env python
#-*- coding: utf-8 -*-

from list3_02_05 import a, b
import numpy as np
import tensorflow as tf

def model(x):

    '''回帰モデル y = ax + b

     Parameters:
      x(ndarray):分析するデータ
    '''

    y = a * x + b
    return y

if __name__ == "__main__":
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(model(x))
