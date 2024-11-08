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


def plotdata(x,y1,y2,y3,y4):    
    fig, ax = plt.subplots()
    w=x[0]/5.0
    
    rects1 = ax.bar(x-w, y1, w, color='dodgerblue',label="C48-32",edgecolor='black')
    rects2 = ax.bar(x, y3, w, color='forestgreen',label="C48-64",edgecolor='black')
    
    rects3 = ax.bar(x+w, y2, w, color='lightskyblue',label="C72-32",edgecolor='black',hatch='/')
    rects4 = ax.bar(x+2*w, y4, w, color='palegreen',label="C72-64",edgecolor='black',hatch='/')

#    ly3=[y3[0],y3[0]]
#    lx3=[1.5,9.5]
#    l3 = ax.plot(lx3,ly3,color='black',linestyle='dashed')

    xt=x
    ax.set_xticks(xt)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.set_xlabel("nlevels")
    ax.set_ylabel("Time per cell (s)")

    ax.legend(bbox_to_anchor=(0.6,0.67))
    plt.title('precision performance comparison')
   
    fstem='precision_scaling'
    fname=fstem+".png"
    plt.savefig(fname,format="png")
    
    plt.show()

def plotdoubledata(x1,y1,x2,y2):    
    fig, ax = plt.subplots()
    w=x1[0]/2.0
    
    rects1 = ax.bar(x1, y1, w, color='firebrick',label="C48",edgecolor='black')
    rects2 = ax.bar(x2, y2, w, color='goldenrod',label="C72",edgecolor='black')
    

    ly1=[0,0.1]
    d=256*1024/8
    lx1=[d,d]
    l1 = ax.plot(lx1,ly1,color='black',linestyle='dashed', label='L2 64')
    
    ly2=[0,0.1]
    s=256*1024/4
    lx2=[s,s]
    l2 = ax.plot(lx2,ly2,color='black',linestyle='dotted', label='L2 32')

    

#    xt=x
#    ax.set_xticks(xt)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.set_xlabel("ncells")
    ax.set_ylabel("percentage speed up in 32-bit (diff/sum)")

    ax.legend(bbox_to_anchor=(0.6,0.67))
    plt.title('precision performance comparison II')
   
    fstem='precent_speedup'
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
    ax.legend(bbox_to_anchor=(0.75,0.4))

    fstem='adv_mpi_scale'
    fname=fstem+".png"
    plt.savefig(fname,format="png")
    
    
    plt.show()    

fname="performance.dat"
alldata=np.genfromtxt(fname, skip_header=1, usecols= range(0,4))
print(alldata)
ndata=5
C48S=alldata[0:ndata,3]
C72S=alldata[ndata:2*ndata,3]
C48D=alldata[2*ndata:3*ndata,3]
C72D=alldata[3*ndata:4*ndata,3]
L=alldata[0:ndata,0]
#print(C72D[3],C72S[3])
#print((C72D[3]-C72S[3])/(C72D[3]+C72S[3]))
#print((C72D[4]-C72S[4])/(C72D[4]+C72S[4]))
#print((C48D[3]-C48S[3])/(C48D[3]+C48S[3]) )
#print((C48D[4]-C48S[4])/(C48D[4]+C48S[4]) )

#normalise the times by datasize.
C48S=C48S/(48.0*48.0/6.0)/L
C72S=C72S/(72.0*72.0/6.0)/L
C48D=C48D/(48.0*48.0/6.0)/L
C72D=C72D/(72.0*72.0/6.0)/L

#o1=np.empty_like(omp)
plotdata(L,C48S,C72S,C48D,C72D)

PC48=( (C48D-C48S) / (C48D+C48S) )
PC72=( (C72D-C72S) / (C72D+C72S) )

S48=48*48*L/6
S72=72*72*L/6

plotdoubledata(S48,PC48,S72,PC72)

c=(45*1024*1024/18.0)
print(c/4,c/8)


