#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import sys

x=np.array([-2.0,2.0])
y=np.array([-0.5,1.5])

fig,ax = plt.subplots()
l1=ax.plot(x, y, 'r')
plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.savefig("linear.png",format="png")
plt.show()
