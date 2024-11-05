#!/usr/local/opt/python/libexec/bin/python

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


def plot2data(x,y1,y2,label):    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, y1, 0.25, color='dodgerblue',label=label[0],edgecolor='black')
    rects2 = ax.bar(x+0.25, y2, 0.25, color='lightskyblue',label=label[1],edgecolor='black')

    xt=x
    ax.set_xticks(xt)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.set_xlabel("Threads")
    ax.set_ylabel("Time (s)")

#    ax.legend(loc="upper center")
    ax.legend(bbox_to_anchor=(0.35,0.9))

    fname=label[2]+".png"
    plt.savefig(fname,format="png")
    
    plt.show()

def plot3data(x,y1,y2,y3, label, CS):    
    fig, ax = plt.subplots()
    width=0.25
    ColourSchemes=[['firebrick','darkorange','gold'],['dodgerblue','lightskyblue','teal']]
    rects1 = ax.bar(x, y1, width, color=ColourSchemes[CS][0],label=label[0],edgecolor='black')
    rects2 = ax.bar(x+width, y2, width, color=ColourSchemes[CS][1],label=label[1],edgecolor='black')
    rects3 = ax.bar(x+2*width, y3, width, color=ColourSchemes[CS][2],label=label[2],edgecolor='black')

    xt=x
    ax.set_xticks(xt)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.set_xlabel("Threads")
    ax.set_ylabel("time")
#    ax.legend(loc="upper center")
    ax.legend(bbox_to_anchor=(0.35,0.9))    

    fname=label[3]+".png"
    plt.savefig(fname,format="png")
    
    plt.show()    

fname="C384.dat"
alldata=np.genfromtxt(fname, skip_header=1, usecols= range(0,9))
print(alldata)

T=alldata[:,0]
time=alldata[:,1]
user=alldata[:,2]*time/100.0
MVK=alldata[:,3]*time/100.0
PGB=alldata[:,4]*time/100.0
MLU=alldata[:,5]*time/100.0
HE=alldata[:,6]*time/100.0
GS=alldata[:,7]*time/100.0
omp=alldata[:,8]*time/100.0

red=0
blue=1
label=['total','user','total']
plot2data(T,time, user, label)
label2=['MVK','PGB','MLU','kernels']
plot3data(T,MVK, PGB, MLU, label2, blue)
label3=['HE','GS','OMP','prog_model']
plot3data(T,HE, GS, omp, label3,red)
print(HE)

