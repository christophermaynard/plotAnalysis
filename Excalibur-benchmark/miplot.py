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
    rects1 = ax.bar(x-0.25, y1, 0.25, color='dodgerblue',label="AMD/Intel",edgecolor='black')
    rects2 = ax.bar(x, y2, 0.25, color='lightskyblue',label="Intel opt",edgecolor='black')
    rects3 = ax.bar(x+0.25, y3, 0.25, color='palegreen',label="AMD opt",edgecolor='black')

    ax.set_xlim(0.5,4.5)
    xt=[1,2,3,4]
    xlab=["CSR","AVX512","MF","LFRic"]
    #    ax.set_xticks(xt,labels=xlab)
    plt.xticks(xt,xlab)
 #   ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
 #   ax.get_xaxis().set_minor_locator(ticker.NullLocator())

#    ax.set_xlabel("comparison")
    ax.set_ylabel("E=Orig/var")

#    ax.legend(bbox_to_anchor=(0.25,0.85))
    ax.legend(loc="upper left")
#    plt.title('')
   
    fstem='HPCG'
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

fname="perf.dat"
alldata=np.genfromtxt(fname, skip_header=1, usecols= range(0,3))
print(alldata)
intel=alldata[0:4,1]
amd=alldata[0:4,2]
arch=amd/intel
arch[1]=0.0
print(arch)

opt=np.empty_like(arch)
opt[1]=intel[1]/intel[0]
opt[2]=intel[2]/intel[0]
opt[3]=intel[3]/intel[0]
opt[0]=0.0
print(opt)

amdopt=np.empty_like(arch)
amdopt[2]=amd[2]/amd[0]
amdopt[3]=amd[3]/amd[0]
amdopt[0]=0.0
amdopt[1]=0.0
print(amdopt)

x=alldata[0:4,0]
print(x)

plotdata(x,arch,opt,amdopt)



