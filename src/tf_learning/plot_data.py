#!/usr/bin/env python
#-*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

data = np.loadtxt(fname = "sales.csv",
                  dtype = "int",
                  delimiter = ",",
                  skiprows = 1
                  )
train_x = data[:, 0]
train_y = data[:, 1]

plt.plot(train_x,
         train_y,
         "o"
         )
plt.show()
