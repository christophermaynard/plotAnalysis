#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import sys

def makeplot(x,y1,y2,y3,y4,y5,y6,z1,z2,z3,z4,z5,z6):
    w=0.08
    fig, ax = plt.subplots(nrows=1, ncols=1)#, sharex=True)

    irects1 = ax.bar(x,     y1, width=w, color='dodgerblue',label="ivp",edgecolor='black')
    irects2 = ax.bar(x+w,   y2, width=w, color='dodgerblue',label="iva",edgecolor='black',hatch='//')

    irects3 = ax.bar(x+2*w, y3, width=w, color='mediumblue',label="icp",edgecolor='black')
    irects4 = ax.bar(x+3*w, y4, width=w, color='mediumblue',label="ica",edgecolor='black',hatch='//')
    
    irects5 = ax.bar(x+4*w, y5, width=w, color='teal',label="iop",edgecolor='black')
    irects6 = ax.bar(x+5*w, y6, width=w, color='teal',label="ioa",edgecolor='black',hatch='//')

    x=x+0.48
    crects1 = ax.bar(x,     z1, width=w, color='firebrick',label="cvp",edgecolor='black')
    crects2 = ax.bar(x+w,   z2, width=w, color='firebrick',label="cva",edgecolor='black',hatch='//')

    crects3 = ax.bar(x+2*w, z3, width=w, color='darkorange',label="ccp",edgecolor='black')
    crects4 = ax.bar(x+3*w, z4, width=w, color='darkorange',label="cca",edgecolor='black',hatch='//')
    
    crects5 = ax.bar(x+4*w, z5, width=w, color='saddlebrown',label="cop",edgecolor='black')
    crects6 = ax.bar(x+5*w, z6, width=w, color='saddlebrown',label="coa",edgecolor='black',hatch='//')

    ax.set_ylabel("time (s)")
    ax.set_xlabel("different runs")
    plt.title("OMP run comparison")
    ax.minorticks_on()
    ax.legend(bbox_to_anchor=(0.9, 1),loc='upper left')                
    ax.set_xticklabels("")
    fname="OMP_wait_policy.png"
    plt.savefig(fname,format="png")    
    plt.show()    

rdata=np.genfromtxt("wait.dat",skip_header=0, usecols=range(0,3))

#print rdata
ivp=np.array(rdata[0:4,0])
iva=np.array(rdata[4:8,0])

icp=np.array(rdata[0:4,1])
ica=np.array(rdata[4:8,1])

iop=np.array(rdata[0:4,2])
ioa=np.array(rdata[4:8,2])

cvp=np.array(rdata[9:13,0])
cva=np.array(rdata[13:17,0])

ccp=np.array(rdata[9:13,1])
cca=np.array(rdata[13:17,1])
.   .
cop=np.array(rdata[9:13,2])
coa=np.array(rdata[13:17,2])

xx=np.array(range(1,5))
makeplot(xx,ivp,iva,icp,ica,iop,ioa,cvp,cva,ccp,cca,cop,coa)


