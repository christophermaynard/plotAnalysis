#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import sys

fname="ts.dat"
dat=np.genfromtxt(fname,skip_header=1, usecols=range(0,2))
ympi=dat[:,0]
yomp=dat[:,1]
x=np.arange(1,11)
print x
print ympi

fig, ax = plt.subplots()
rects1 = ax.bar(x, ympi, width=0.45, color='teal',label="mpi",edgecolor='black')
rects2 = ax.bar(x+0.45, yomp, width=0.45, color='dodgerblue',label="omp",edgecolor='black', hatch='//')
ax.set_xlabel('time-step band')
ax.set_ylabel('time in seconds')
#plt.title('Number of GCR iterations')
#fstem="bicgstab_hist"
#fname=fstem+".png"
#plt.savefig(fname,format="png")
#fname=fstem+".eps"
#plt.savefig(fname,format="eps")    
mpi_s=sum(ympi)
omp_s=sum(yomp)
print mpi_s
print omp_s

lx=[1,10.5]
lmpi=[(mpi_s/10.0),(mpi_s/10.0)]
lomp=[(omp_s/10.0),(omp_s/10.0)]
l1=ax.plot(lx,lmpi,color='black',label='mpi ave')
l2=ax.plot(lx,lomp,color='black',label='omp ave', linestyle='dashed')

plt.show()
