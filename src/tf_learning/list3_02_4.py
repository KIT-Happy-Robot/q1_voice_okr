#!/usr/bin/env python
#-*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from list3_02_3 import standardize

data = np.loadtxt(fname = "sales.csv",
                  dtype = "int",
                  delimiter = ",",
                  skiprows = 1
                  )
train_x = data[:, 0]
train_y = data[:, 1]
train_x_std = standardize(train_x)
train_y_std = standardize(train_y)
plt.plot(train_x_std,
         train_y_std,
         "o"
         )
plt.show()
