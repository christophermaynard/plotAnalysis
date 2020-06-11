#!/usr/local/opt/python/libexec/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

import sys

fname="cfl.dat"
adata=np.genfromtxt(fname, skip_header=0, usecols= range(0,4))
print(adata)
x=np.array(adata[:,0])
mg=np.array(adata[:,1])
kr2=np.array(adata[:,2])
kr6=np.array(adata[:,3])


fig, ax = plt.subplots()
width=0.5
xlim=[0,12]
ax.set_xlim(xlim[0],xlim[1])

rects1 = ax.bar(x, mg, width, color='midnightblue',label="MG",edgecolor='black')
rects2 = ax.bar(x+width, kr2, width, color='teal',label="KR 2",edgecolor='black', hatch='//')
rects3 = ax.bar(x+width+width, kr6, width, color='dodgerblue',label="KR 6",edgecolor='black', hatch='\\')
ax.legend(loc='upper left')        
ax.set_xlabel("CFL")
ax.set_ylabel("Time (s)")
plt.title('CFL scaling of SI solver')
plt.show()    
