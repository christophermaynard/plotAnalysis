#!/usr/local/opt/python/libexec/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

import sys

def pedata(x,y):
    z=np.empty_like(x)
    for i in range(len(x)):
        tmp = y[i]/y[0]
        z[i] = (x[0]/x[i])/tmp
    return z

def plot5pe(x, y1, y2, y3, y4, y5, y6, y7):
    fig, ax = plt.subplots()
    xlim=[96,2800]
    ax.set_xlim(xlim[0],xlim[1])
    ylim=[0,1.3]
    ax.set_ylim(ylim[0],ylim[1])

    width1=0.075*x*0.875
    width2=0.075*x*0.95
    width3=0.075*x*1.025
    width5=0.075*x*1.185
    width4=0.075*x*1.1    
    width6=0.075*x*0.8
    width7=0.075*x*1.28
   
    rects1 = ax.bar(0.875*x, y1, width1, color='saddlebrown',label="time-step",edgecolor='black')
    rects2 = ax.bar(0.805*x, y6, width6, color='saddlebrown', label="MG time-step", edgecolor='black',hatch='//')
    
    rects3 = ax.bar(0.95*x, y2, width2, color='peru',label="fast phys",edgecolor='black')
    rects4 = ax.bar(1.025*x, y3, width3, color='firebrick',label="advection",edgecolor='black')
    rects5 = ax.bar(1.1*x, y5, width5, color='goldenrod',label="slow phys",edgecolor='black')



    rects6 = ax.bar(1.185*x, y4, width4, color='coral',label="solver",edgecolor='black')    
    rects7 = ax.bar(1.28*x, y7, width7, color='coral',label="MG solver",edgecolor='black',hatch='//')

    ax.set_xscale('log')
    ax.minorticks_on()
    
    ax.set_xticks(x)
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.legend(loc='lower left')
    ax.set_xlabel("# nodes")
    ax.set_ylabel("Parallel efficiency")
    plt.title("UM scaling 11.6")
    plt.show()

def plotrdata(x,s1,s2,y1,y2,y3,z1,z2):
    fig, ax = plt.subplots()
    xlim=[96,2800]
    ax.set_xlim(xlim[0],xlim[1])
    ylim=[0,1.0]
    ax.set_ylim(ylim[0],ylim[1])

    width=0.1*x
    width2=0.1*x*1.1
    rects1 = ax.bar(x, y1/s1, width,color='saddlebrown',edgecolor='black',label='EG Adv')
    rects2 = ax.bar(x, y2/s1, width,color='firebrick',edgecolor='black',bottom=(y1/s1),label='EG phys1')
    rects3 = ax.bar(x, y3/s1, width,color='goldenrod',edgecolor='black',bottom=((y1+y2)/s1),label='EG phys2')
    rects4 = ax.bar(x, z1/s1, width,color='coral',edgecolor='black',bottom=((y1+y2+y3)/s1),label='EG solver')

    rects5 = ax.bar(1.1*x, y1/s2, width2,color='dodgerblue',edgecolor='black',label='MG adv')
    rects6 = ax.bar(1.1*x, y2/s2, width2,color='teal',edgecolor='black',bottom=(y1/s2), label='MG Phys1')
    rects7 = ax.bar(1.1*x, y3/s2, width2,color='skyblue',edgecolor='black',bottom=((y1+y2)/s2),label='MG Phys2')
    rects8 = ax.bar(1.1*x, z2/s2, width2,color='steelblue',edgecolor='black',bottom=((y1+y2+y3)/s2),label='MG solver')

    ax.set_xscale('log')
    ax.minorticks_on()
    
    ax.set_xticks(x)
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.legend(bbox_to_anchor=(0.15,0.0,1.0,1.0),loc='lower left')
    ax.set_xlabel("# nodes")
    ax.set_ylabel("fraction of timestep")
    plt.title("UM scaling 11.6")
    plt.show()    
    
fname="ts_comp.dat"
all_data=np.genfromtxt(fname, skip_header=2, usecols=range(0,6))

nodes=np.array(all_data[0:4,0])
MG_ts=np.array(all_data[0:4,1])
MG_phys2=np.array(all_data[0:4,2])
MG_adv=np.array(all_data[0:4,3])
MG_solver=np.array(all_data[0:4,4])
MG_phys1=np.array(all_data[0:4,5])

EG_ts=np.array(all_data[4:8,1])
EG_solver=np.array(all_data[4:8,4])

MG_ts_pe=pedata(MG_ts,nodes)
MG_phys2_pe=pedata(MG_phys2,nodes)
MG_adv_pe=pedata(MG_adv,nodes)
MG_solver_pe=pedata(MG_solver,nodes)
MG_phys1_pe=pedata(MG_phys1,nodes)
EG_ts_pe=pedata(EG_ts,nodes)
EG_solver_pe=pedata(EG_solver,nodes)


plot5pe(nodes,EG_ts_pe, MG_phys2_pe, MG_adv_pe, EG_solver_pe, MG_phys1_pe, MG_ts_pe, MG_solver_pe)

plotrdata(nodes,EG_ts, MG_ts, MG_adv, MG_phys2, MG_phys1, EG_solver, MG_solver)
print(MG_adv/EG_ts)
print(MG_adv/MG_ts)
