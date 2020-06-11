#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sys


odata=np.array([[96,216,386],[119.6,50.4,29.1],[53.9, 36.94, 23.9]])
mdata=np.array([[96,216,386],[139.5, 63.6, 37.53],[33.5,25.83, 30.0]])

print odata
print mdata

x=odata[0,:]
od1=odata[1,:]
od2=odata[2,:]

md1=mdata[1,:]
md2=mdata[2,:]

fig, ax =plt.subplots()
xlim=[72,576]
ax.set_xlim(xlim[0],xlim[1])

width=0.075*x
rects1 = ax.bar(0.95*x, od1, width=width, color='goldenrod', label='OMP MV', edgecolor='black')
rects2 = ax.bar(1.025*x, md1, width=width, color='firebrick', label='MPI MV', edgecolor='black', hatch='//')

rects3 = ax.bar(1.1*x, od2, width=width, color='darkorange', label='OMP HE', edgecolor='black')
rects4 = ax.bar(1.175*x, md2, width=width, color='sienna', label='MPI HE', edgecolor='black', hatch='//')

ax.set_xscale('log')
ax.minorticks_on()
ax.set_xticks(x)
ax.set_xticks(x)
ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
ax.get_xaxis().set_minor_locator(ticker.NullLocator())
ax.set_xlabel("# nodes")
ax.set_ylabel("time (s)")
ax.legend(loc='upper right')        
plt.title('Strong Scaling on C576 for 100 time-steps')


fstem='omp_ss'
fname=fstem+".png"
plt.savefig(fname,format="png")
plt.show()
