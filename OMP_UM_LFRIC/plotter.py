##!/usr/local/opt/python/libexec/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

import sys

def square(x):
    y=np.empty_like(x)
    for i in range(len(x)):
        y[i]=math.pow(x[i],2)
    return y;

def dabs_nparray(x,y):
    z=np.empty_like(x)
    for i in range(len(x)):
        z[i]=math.fabs( (x[i]-y[i]) )
    return z;

def ratio_data(x):
    z=np.empty_like(x)
    for i in range(len(x)):
        z[i] = x[i]/x[0]
    return z

def pedata(x,y):
    z=np.empty_like(x)
    for i in range(len(x)):
        tmp = y[i]/y[0]
        z[i] = (x[0]/x[i])/tmp
    return z


def plotseries(x,y1,y2, y3):    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, y1, 0.25, color='dodgerblue',label="C192",edgecolor='black')
    rects2 = ax.bar(x+0.25, y2, 0.25, color='lightskyblue',label="C384",edgecolor='black')
    rects3 = ax.bar(x+0.5, y3, 0.25, color='teal',label="C768",edgecolor='black')

#    xt=[1,6,9]
#    ax.set_xticks(xt)
#    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
#    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.set_xlabel("week")
    ax.set_ylabel("Time (s)")

    ax.legend(bbox_to_anchor=(0.25,0.85))
#    plt.title('Thread scaling')
#   
    fstem='global_ts'
#    fstem='gh_transport_ts'
    fname=fstem+".png"
    plt.savefig(fname,format="png")
    
    plt.show()

def plotlogdata(x,y1,y2):    
    fig, ax = plt.subplots()
    width=0.1*x
    rects1 = ax.bar(0.95*x, y1, width, color='firebrick',label="UM",edgecolor='black')
    rects2 = ax.bar(1.05*x, y2,      width, color='goldenrod',label="LFric",edgecolor='black')
    #    rects3 = ax.bar(1.05*x, y3, width, color='goldenrod',label="T=9",edgecolor='black')

    xl=[0.9,9]
    yl=[1,1]
    line=ax.plot(xl,yl,color='black',linestyle='dashed')
    xt=x
    ax.set_xscale('log')    
    ax.set_xticks(xt)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.set_xlabel("# threads")
    ax.set_ylabel("ratio")
    plt.title('x(Tn)/x(T1)')
    ax.legend(bbox_to_anchor=(0.25,0.4))

    fstem='thread-scale'
    fname=fstem+".png"
    plt.savefig(fname,format="png")
    
    
    plt.show()    

fname="perf.dat"
alldata=np.genfromtxt(fname, skip_header=1, usecols= range(0,3))
print(alldata)

T=alldata[:,0]
print(T)
um=alldata[:,1]
lfric=alldata[:,2]
print(lfric)
plfric=ratio_data(lfric)
print(plfric)
pum=ratio_data(um)
print(pum)
plotlogdata(T,pum,plfric)





