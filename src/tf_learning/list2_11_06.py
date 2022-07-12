#!/usr/bin/env python
#-*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
#%matlib inline

def classify(x, w):
    if np.dot(w, x):
        return 1
    else:
        return -1

def learn_weight(x, t):
    w = np.random.rand(2)
    loop = 5
    count = 0

    for i in range(loop):
        for element_x, element_t in zip(x, t):
            if classify(element_x, w) != element_t:
                w = w + element_t * element_x
                print("更新後のw = ", w)
        count += 1

        print("[{}回目]: w = {}***".format(count, w))
    
    return w

def main():
    data = np.loadtxt('negaposi.csv',
                      delimiter = ',',
                      skiprows = 1,
                      )
    x = data[:,0:2]
    t = data[:,2]

    w = learn_weight(x, t)


    x1 = np.arange(0, 600)

    plt.plot(
        x[t == 1, 0], x[t == -1, 1], 'o'
        )

    plt.plot(
        x[t == -1, 0], x[t == -1, 1], 'x'
        )

    plt.plot(
        x1, -w[0] / w[1] * x1, linestyle = 'solid'
        )
    plt.show


if __name__ == '__main__':
    main()
