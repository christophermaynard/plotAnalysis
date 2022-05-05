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

def plotlogdata(x,y,n,c):    
    fig, ax = plt.subplots()
    width=0.05*x
    rects1 = ax.bar(x, y, width, color='firebrick',label="",edgecolor='black')
    px=[1.75,18.0]
    py=[0.0,0.0]
    py[0]=c*math.pow((px[0]),n)
    py[1]=c*math.pow((px[1]),n)
    line=ax.plot(px,py,color='black',linestyle='dashed')

    ax.set_xscale('log')
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.set_yscale('log')
    ax.set_yticks(y)
    ax.get_yaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_yaxis().set_minor_locator(ticker.NullLocator())

    ax.set_xlabel("ndata")
    ax.set_ylabel("time (s)")
    cstr="{:.2f}".format(c)
    nstr="{:.2f}".format(n)    
    title_str='y = '+cstr+' * x^'+nstr+' log-log'
    plt.title(title_str)
#    ax.legend(bbox_to_anchor=(0.75,0.4))

#    fstem='adv_mpi_scale'
#    fname=fstem+".png"
#    plt.savefig(fname,format="png")
    
    plt.show()    

fname="time.dat"
alldata=np.genfromtxt(fname, skip_header=0, usecols= range(0,2))
print(alldata[0:4,0])
x=alldata[0:4,0]
y=alldata[0:4,1]

# calc the gradient of the log-log plot
n=( math.log(y[3]) - math.log(y[0]) ) / ( math.log(x[3]) - math.log(x[0]) )
print(n)
c=y[1]/math.pow(x[1],n)
print(c)
a=y[2]
b=c*math.pow(x[2],n)
print(str(a)+":"+str(b))
plotlogdata(x,y,n,c)




