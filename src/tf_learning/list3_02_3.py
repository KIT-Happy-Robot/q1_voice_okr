#!/usr/bin/env python
#-*- coding: utf-8 -*-

import numpy as np

def standardize(x):
    '''標準化を行う
    Parameters:
     x(ndarray):標準化前のx
    '''

    x_mean = x.mean()
    std =x.std()
    return (x - x_mean) / std

if __name__ == "__main__":
    x = np.random.randint(0, 10, 10)
    print("引数が", x, "の場合")
    print(standardize(x))

