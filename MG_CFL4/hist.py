#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import sys

#x=np.array([0,10,40,97,385,597,805,788,734,550,388,340,310,310,268,182,156,105,49,26,10,7,2,1])

#mname="GCR_its_mpi.dat"
#oname="GCR_its_omp.dat"

#mname="bicgstab_its_mpi.dat"
#oname="bicgstab_its_omp.dat"
oname="bicg_freq.dat"
#oname="bicgstab.its"
#m=np.genfromtxt(mname,skip_header=0, usecols=range(0,1))
#print "mpi: " + str(len(m)) + ", " +str( sum(m))
o=np.genfromtxt(oname,skip_header=0, usecols=range(0,1))
nbins=20
ave=sum(o)/len(o)
print "totals: " + str(len(o)) + ", " +str( sum(o)) + ", " + str(ave)
fig, ax = plt.subplots()
#h1=ax.hist(m, bins=nbins,color='mediumvioletred', edgecolor='black',width=0.45)
#h2=ax.hist(o+0.45, bins=nbins,color='dodgerblue', edgecolor='black',width=0.45)
h2=ax.hist(o, bins=nbins, color='dodgerblue', edgecolor='black',width=0.45)
ax.set_xlabel('Number of iterations')
ax.set_ylabel('Frequency')
plt.title('Number of BiCGStab iterations')
fstem="bicgstab_hist"
fname=fstem+".png"
#plt.savefig(fname,format="png")
fname=fstem+".eps"
#plt.savefig(fname,format="eps")    
print sun(o)
plt.show()
