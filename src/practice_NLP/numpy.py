#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy 
import matplotlib.pylab as plt



def step_function(x):
    return numpy.array(x > 0, dtype=numpy.int)


x = numpy.arange(-5.0, 5.0, 0.1)
y = step_function(X)
plt.plot(x, y)
plt.ylim(-0.1,1.1)
plt.show()


