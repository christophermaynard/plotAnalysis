#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import sys

def pedata(x,y):
    z=np.empty_like(x)
    for i in range(len(x)):
        tmp = y[i]/y[0]
        z[i] = (x[0]/x[i])/tmp
    return z

def plot2Data(x, y1, y2, flag):

    fig, ax = plt.subplots()
    xlim=[72,1944]
    ax.set_xlim(xlim[0],xlim[1])

    c1='firebrick','purple'
    c2='goldenrod','hotpink'
    titles='Strong scaling on C1152 for 100 time-steps','Parallel Efficiency on C1152 for 100 time-steps'
    fstem='strong-scale','parallel_efficiency'

    if flag==1:
        psx=[96,1536]
        psy=[1.0, 1.0]
        l1 = ax.plot(psx,psy,color='black',linestyle='dashed',label="perfect scaling")
        ax.legend(loc='lower center')
    else:
        ax.legend(loc='upper right')        
        
    width1=0.1*x
    width2=0.1*x
    rects1 = ax.bar(0.95*x, y1, width1, color=c1[flag],label="MG",edgecolor='black')
    rects2 = ax.bar(1.05*x, y2, width2, color=c2[flag],label="Krylov",edgecolor='black')

    ax.set_xscale('log')
    ax.minorticks_on()
    
    
    ax.set_xticks(x)
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.set_xlabel("# nodes")
    ax.set_ylabel("time (s)")
    plt.title(titles[flag])

    fname=fstem[flag]+".png"
    plt.savefig(fname,format="png")
    fname=fstem[flag]+".eps"
    plt.savefig(fname,format="eps")    
    plt.show()


lname="mg-scale.dat"
sdata=np.genfromtxt(lname, skip_header=1, usecols=range(0,3))
nodes=np.array(sdata[:,0])
mgdat=np.array(sdata[:,1])
bicgstabdat=np.array(sdata[:,2])

plot2Data(nodes, mgdat, bicgstabdat,0)

mgpe=pedata(mgdat,nodes)
bicgstabpe=pedata(bicgstabdat,nodes)

plot2Data(nodes, mgpe, bicgstabpe,1)


