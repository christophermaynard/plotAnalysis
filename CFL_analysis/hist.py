#!/usr/local/bin/python

import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker

import sys
#fstem="6/bicgstab_its_cfl6_kr6"
#fstem="6/gcr_its_cfl6_kr6"
fstem="GCR_its_400"
oname=fstem+".dat"

o=np.genfromtxt(oname,skip_header=0, usecols=range(0,1))
nbins=20
ave=sum(o)/len(o)
print "totals: " + str(len(o)) + ", " +str( sum(o)) + ", " + str(ave)
#fig, ax = plt.subplots()

#h2=ax.hist(o, bins=nbins, color='firebrick', edgecolor='black',width=0.5)
#h2=ax.hist(o, bins=nbins, color='dodgerblue', edgecolor='black',width=1.5)
#ax.set_xlabel('Number of iterations')
#ax.set_ylabel('Frequency')
#plt.title('Number of GCR iterations')
#plt.title('Number of BiCGStab iterations')
#fname=fstem+".png"
#plt.savefig(fname,format="png")
#fname=fstem+".eps"
#plt.savefig(fname,format="eps")    
#print sum(o)
#plt.show()
