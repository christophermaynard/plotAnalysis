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

def pedata(x,y):
    z=np.empty_like(x)
    for i in range(len(x)):
        tmp = y[i]/y[0]
        z[i] = (x[0]/x[i])/tmp
    return z


def plotdata(x,y1,y2,y3):    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x-0.5, y1, 0.5, color='dodgerblue',label="nodes=24",edgecolor='black')
    rects2 = ax.bar(x, y2, 0.5, color='lightskyblue',label="nodes=12",edgecolor='black')
    rects3 = ax.bar(x+0.5, y3, 0.5, color='palegreen',label="nodes=6",edgecolor='black')

    ly1=[y1[0],y1[0]]
    lx1=[0.5,8.5]
    l1 = ax.plot(lx1,ly1,color='black',linestyle='dashed',label="perfect scaling")

    ly2=[y2[0],y2[0]]
    lx2=[1,9]
    l2 = ax.plot(lx2,ly2,color='black',linestyle='dashed')

    ly3=[y3[0],y3[0]]
    lx3=[1.5,9.5]
    l3 = ax.plot(lx3,ly3,color='black',linestyle='dashed')

    xt=[1,6,9]
    ax.set_xticks(xt)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.set_xlabel("# omp threads")
    ax.set_ylabel("Time (s)")

    ax.legend(bbox_to_anchor=(0.25,0.85))
    plt.title('Thread scaling')
   
    fstem='adv_omp_scale'
    fname=fstem+".png"
    plt.savefig(fname,format="png")
    
    plt.show()

def plotlogdata(x,y1,y2,y3):    
    fig, ax = plt.subplots()
    width=0.05*x
    rects1 = ax.bar(0.95*x, y1, width, color='firebrick',label="T=1",edgecolor='black')
    rects2 = ax.bar(x, y2,      width, color='darkorange',label="T=6",edgecolor='black')
    rects3 = ax.bar(1.05*x, y3, width, color='goldenrod',label="T=9",edgecolor='black')

    xt=x
    ax.set_xscale('log')    
    ax.set_xticks(xt)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.set_xlabel("# nodes")
    ax.set_ylabel("PE")
    plt.title('Node scaling')
    ax.legend(bbox_to_anchor=(0.25,0.4))

    fstem='adv_mpi_scale'
    fname=fstem+".png"
    plt.savefig(fname,format="png")
    
    
    plt.show()    

fname="performance.dat"
alldata=np.genfromtxt(fname, skip_header=1, usecols= range(0,4))
print(alldata)
omp=alldata[0:3,0]
mpi=np.empty_like(omp)
mpi[0]=alldata[0,1]
mpi[1]=alldata[3,1]
mpi[2]=alldata[6,1]
m6=alldata[0:3,3]
m12=alldata[3:6,3]
m24=alldata[6:9,3]
o1=np.empty_like(omp)
o1[0]=alldata[0,3]
o1[1]=alldata[3,3]
o1[2]=alldata[6,3]
o6=np.empty_like(omp)
o6[0]=alldata[1,3]
o6[1]=alldata[4,3]
o6[2]=alldata[7,3]
o9=np.empty_like(omp)
o9[0]=alldata[2,3]
o9[1]=alldata[5,3]
o9[2]=alldata[8,3]

peo1=pedata(o1,mpi)
peo6=pedata(o6,mpi)
peo9=pedata(o9,mpi)

plotdata(omp,m24,m12,m6)
plotlogdata(mpi,peo1,peo6,peo9)



