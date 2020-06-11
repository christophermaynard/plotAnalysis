#!/usr/local/opt/python/libexec/bin/python

#####!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

import sys

def plot2Data(x1, y1, x2, y2,title_str):
    fig, ax = plt.subplots()
    width = 0.25
    rects1 = ax.bar(x1,y1, width, color='goldenrod', edgecolor='black', label='Opt')
    rects2 = ax.bar(x2,y2, width, color='firebrick', edgecolor='black', label='No Opt')

    ax.minorticks_off()
    ax.set_xticks(x1)
    ax.set_xlabel("# OMP threads")
    ax.set_ylabel("Time (s)")
    ax.legend(loc='lower center')    

    plt.title(title_str)
    fname=title_str+".png"
    plt.savefig(fname,format="png")
    plt.show()

    
#  Get the data
fname="C288N96.dat"
rawdata=np.genfromtxt(fname, skip_header=2, usecols=range(0,12) )

# Nthread, WC , iter, Si, MS, ADV : WC2     MV    HE GS   KMP Psykal-lite
names = 'WC','Iter', 'Si', 'MS', 'Adv','WC2', 'MV', 'HE', 'GS', 'KMP', 'Psykal-lite'
nt=np.array(rawdata[0:4,0])
nt_no=np.array(rawdata[4:6,0])
print( nt )
print( nt_no )

for i in range(1, 12):
    wc=np.array(rawdata[0:4,i])
    wc_no=np.array(rawdata[4:6,i])
    plot2Data(nt, wc, nt_no, wc_no, names[i-1])
