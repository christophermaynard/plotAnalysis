#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

import sys

def plot2Data(x, y1, y2, y3, y4):
    fig, ax = plt.subplots()
    width = 10

    rects1 = ax.bar(x-5,y1, width, color='goldenrod', edgecolor='black', label='Kr')
    rects2 = ax.bar(x+5,y2, width, color='firebrick', edgecolor='black', label='MG')
    rects3 = ax.bar(x[0]+15,y3, width, color='darkorange', edgecolor='black', label='Kr-solve',hatch='//')
    rects4 = ax.bar(x[0]+25,y4, width, color='saddlebrown', edgecolor='black', label='MG-solve',hatch='//')


    ax.minorticks_on()
    ax.set_xticks(x)
    ax.set_xlabel("# nodes")
    ax.set_ylabel("Time (s)")
    ax.legend(loc='upper center')    

    plt.title("ENDGame WC")
    plt.show()    

#  Get the data
fname="EG.dat"
rawdata=np.genfromtxt(fname, skip_header=0, usecols=range(0,3) )

nt=np.array(rawdata[:,0])
mg=np.array(rawdata[:,1])
kr=np.array(rawdata[:,2])
eg_frac=1262.0/3675.0
kr_frac=1839.0/4236.0

print eg_frac, kr_frac
mg_solv=mg[0]*eg_frac
kr_solv=kr[0]*kr_frac
print mg_solv, kr_solv

print nt
plot2Data(nt,  kr,mg, kr_solv,mg_solv)
