#!/usr/local/bin/python

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

def plot2DataLin(x, y1, y2,flag, title_str):
    fig, ax = plt.subplots()
    n=len(x)
    width = 0.025*(x[0]-x[n-1])
    rects1 = ax.bar(x-0.5*width, y1, width, color='teal',label="MG",edgecolor='black')
    rects2 = ax.bar(x+0.5*width, y2, width, color='darkgreen',label="Krylov",edgecolor='black')

    ylabel_str="Memory (MBytes)", "Time (s)"
    ax.set_xlabel("Local volume (N cells)")
    ax.set_ylabel(ylabel_str[flag])

    titles=title_str+' versus problem size'
    plt.title(titles)
    ax.legend(loc='upper left')
    fname=title_str+'_LV.png'
    plt.savefig(fname,format="png")
    plt.show()
    
def plot2Data(x, y1, y2, flag, title_string):

    fig, ax = plt.subplots()
    xlim=[72,1944]
    ax.set_xlim(xlim[0],xlim[1])

    c1='firebrick','royalblue'
    c2='goldenrod','mediumblue'
    titles='Strong scaling of ' + title_string,'Parallel Efficiency of ' + title_string 
    fstem='sscale_'+title_string,'pe_'+title_string
    ylabel_str='time (s)', 'Parallel Efficiency'

    if flag==1:
        psx=[96,1536]
        psy=[1.0, 1.0]
        l1 = ax.plot(psx,psy,color='black',linestyle='dashed',label="perfect scaling")

        
    width1=0.1*x
    width2=0.1*x
    rects1 = ax.bar(0.95*x, y1, width1, color=c1[flag],label="MG",edgecolor='black')
    rects2 = ax.bar(1.05*x, y2, width2, color=c2[flag],label="Kr",edgecolor='black',hatch='//')

    ax.set_xscale('log')
    ax.minorticks_on()
    
    
    ax.set_xticks(x)
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.set_xlabel("# nodes")
    ax.set_ylabel(ylabel_str[flag])
#    plt.title(titles[flag])
    legend_str='upper right', 'lower center'
    ax.legend(loc=legend_str[flag])        
        
    
    fname=fstem[flag]+'.png'
    plt.savefig(fname,format="png")
    plt.show()

def comms2plots(x, y1, y2, y3, z1, z2, z3):

    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
    fig.subplots_adjust(hspace=0)
    xlim=[72,4374]
    ax[0].set_xlim(xlim[0],xlim[1])
    ax[0].set_xscale('log')
    width1=0.1*x
    rects1 = ax[1].bar(0.95*x, y1, width1, color='dodgerblue',label="MG",edgecolor='black')
    rects2 = ax[1].bar(1.05*x, y2, width1, color='mediumblue',label="Kr2",edgecolor='black',hatch='//')
    rects3 = ax[1].bar(1.15*x, y3, width1, color='skyblue',label="Kr6",edgecolor='black',hatch='\\\\')    

    rects4 = ax[0].bar(0.95*x, z1, width1, color='firebrick',label="MG",edgecolor='black')
    rects5 = ax[0].bar(1.05*x, z2, width1, color='goldenrod',label="Kr2",edgecolor='black',hatch='//')
    rects6 = ax[0].bar(1.15*x, z3, width1, color='sienna',label="Kr6",edgecolor='black',hatch='\\\\')

    ax[1].minorticks_on()
    ax[1].set_xticks(x)
    ax[1].set_xticks(x)
    ax[1].get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax[1].get_xaxis().set_minor_locator(ticker.NullLocator())
    ax[1].set_xlabel("# nodes")
    ax[1].set_ylabel("MPI_allreduce (s)")
    ax[0].set_ylabel("Halo Exchange (s)")
    
    ax[1].legend(loc='upper left',bbox_to_anchor=(0.15,1.0))
    ax[0].legend(loc='upper right')#
        
    
    fname="comms_scale.png"
    plt.savefig(fname,format="png")
    plt.show()    

def make2plots(x, y1, y2, y3, z1, z2):

    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
    fig.subplots_adjust(hspace=0)
    xlim=[72,4374]
    ax[0].set_xlim(xlim[0],xlim[1])
    ax[0].set_xscale('log')    

    psx=[96,3456]
    psy=[1.0, 1.0]
    l1 = ax[1].plot(psx,psy,color='black',linestyle='dashed',label="perfect scaling")

        
    width1=0.1*x
    rects1 = ax[1].bar(0.95*x, y1, width1, color='dodgerblue',label="MG",edgecolor='black')
    rects2 = ax[1].bar(1.05*x, y2, width1, color='mediumblue',label="Kr2",edgecolor='black',hatch='//')
    rects3 = ax[1].bar(1.15*x, y3, width1, color='skyblue',label="Kr6",edgecolor='black',hatch='\\\\')

    rects4 = ax[0].bar(0.95*x, z1, width1, color='teal',label="Kr2",edgecolor='black',hatch='--')
    rects5 = ax[0].bar(1.05*x, z2, width1, color='powderblue',label="Kr6",edgecolor='black')
    
    ax[1].minorticks_on()
    ax[1].set_xticks(x)
    ax[1].set_xticks(x)
    ax[1].get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax[1].get_xaxis().set_minor_locator(ticker.NullLocator())
    ax[1].set_xlabel("# nodes")
    ax[1].set_ylabel("PE")
    ax[0].set_ylabel("Pressure R=Kr/MG")
    
    ax[1].legend(loc='lower center')
    ax[0].legend(loc='upper right',bbox_to_anchor=(1.0,1.15))
        
    
    fname="pressure_scale.png"
    plt.savefig(fname,format="png")
    plt.show()    

def plot4Data(x, ya1, ya2, yb1, yb2 ):

    fig, ax = plt.subplots()
    xlim=[72,2304]
    ax.set_xlim(xlim[0],xlim[1])

    c1='firebrick','purple'
    c2='goldenrod','hotpink'
#    titles='Strong scaling on C1152 for 100 time-steps','Parallel Efficiency on C1152 for 100 time-steps'
    fstem='ts_strong_scale','parallel_efficiency'

        
    width=0.1*x
    
    rects2 = ax.bar(0.95*x, ya2, width, color='white',label="Kr total",edgecolor='black',hatch='//')
    rects1 = ax.bar(1.05*x, ya1, width, color='powderblue',label="MG total",edgecolor='black')
    rects4 = ax.bar(0.95*x, yb2, width, color='mediumblue',label="Kr pressure",edgecolor='black',hatch='//')    
    rects3 = ax.bar(1.05*x, yb1, width, color='dodgerblue',label="MG pressure",edgecolor='black')


    ax.set_xscale('log')
    ax.minorticks_on()
    
    
    ax.set_xticks(x)
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())


    ax.set_xlabel("# nodes")
    ax.set_ylabel("time (s)")
#    plt.title(titles[0])
    ax.legend(loc='upper right')            

    fname=fstem[0]+".png"
    plt.savefig(fname,format="png")
    fname=fstem[0]+".eps"
#    plt.savefig(fname,format="eps")    
    plt.show()

def plot4comp(x, ya1, ya2, yb1, yb2, yc1, yc2, yd1, yd2 ):

    fig, ax = plt.subplots()
    xlim=[72,2304]
    ax.set_xlim(xlim[0],xlim[1])
    ylim=[0,250]
    ax.set_ylim(ylim[0],ylim[1])

    c1='firebrick','purple'
    c2='goldenrod','hotpink'
    titles='Strong scaling of time-step for for 100 time-steps','Parallel Efficiency on C1152 for 100 time-steps'
    fstem='ts_comp_strong','solver_comp_strong_scale_zoom'

        
    width1=0.075*x*0.8
    width2=0.075*x*0.95
    width3=0.075*x*1.125
    width4=0.075*x*1.275
    
    rects1 = ax.bar(0.8*x, ya1, width1, color='indigo',label="MG_mop",edgecolor='black')
    rects2 = ax.bar(0.875*x, ya2, width1, color='navy',label="Kr_mop",edgecolor='black', hatch='//')
    rects3 = ax.bar(0.95*x, yb1, width2, color='purple',label="MG_mschur",edgecolor='black')
    rects4 = ax.bar(1.05*x, yb2, width2, color='blue',label="Kr_mschur",edgecolor='black', hatch='//')
    rects5 = ax.bar(1.125*x, yc1, width3, color='magenta',label="MG_helm",edgecolor='black')
    rects6 = ax.bar(1.2*x, yc2, width3, color='dodgerblue',label="Kr_helm",edgecolor='black', hatch='//')
    rects7 = ax.bar(1.275*x, yd1, width4, color='hotpink',label="MG_back",edgecolor='black')
    rects8 = ax.bar(1.35*x, yd2, width4, color='lightskyblue',label="Kr_back",edgecolor='black', hatch='//')

    ax.set_xscale('log')
    ax.minorticks_on()
    
    
    ax.set_xticks(x)
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.legend(loc='upper right')
#    ax.legend(loc='upper left')        

    ax.set_xlabel("# nodes")
    ax.set_ylabel("time (s)")
    plt.title(titles[0])

    fname=fstem[1]+".png"
    plt.savefig(fname,format="png")
    fname=fstem[1]+".eps"
    plt.savefig(fname,format="eps")    
    plt.show()        

def plot3Data(x, y1, y2, y3):

    fig, ax = plt.subplots()
    xlim=[72,2304]
    ax.set_xlim(xlim[0],xlim[1])

    width1=0.1*x
    
    rects1 = ax.bar(0.95*x, y1, width1, color='darkorange',label="Mop",edgecolor='black',hatch='//')
    rects2 = ax.bar(1.05*x, y2, width1, color='firebrick',label="MG Schur",edgecolor='black')
    rects3 = ax.bar(1.15*x, y3, width1, color='goldenrod',label="KR Schur",edgecolor='black')

    ax.set_xscale('log')
    ax.minorticks_on()
    
    
    ax.set_xticks(x)
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())
    ax.legend(loc='lower center')        

    ax.set_xlabel("# nodes")
    ax.set_ylabel("Parallel Efficiency")
    plt.title('Parallel Efficiency of SI solver components')

    
    fstem='pe_solver_comp'
    fname=fstem+".png"
    plt.savefig(fname,format="png")
    fname=fstem+".eps"
    plt.savefig(fname,format="eps")
    plt.show()

def plot6Data(x, y1, y2, z1, z2, w1, w2):

    fig, ax = plt.subplots()
    xlim=[72,2304]
    ax.set_xlim(xlim[0],xlim[1])

    width1=0.075*x*0.875
    width2=0.075*x
    width3=0.075*x*1.2    
    
    rects1 = ax.bar(0.875*x, y1, width1, color='midnightblue',label="MG WC diff",edgecolor='black')
    rects2 = ax.bar(0.95*x, y2, width1, color='teal',label="KR WC diff",edgecolor='black', hatch='//')
    rects3 = ax.bar(1.025*x, z1, width2, color='dodgerblue',label="MG WC var",edgecolor='black')
    rects4 = ax.bar(1.1225*x, z2, width2, color='seagreen',label="KR WC var",edgecolor='black',hatch='//')
    rects5 = ax.bar(1.2*x, w1, width3, color='lightskyblue',label="MG Pthread join",edgecolor='black')
    rects6 = ax.bar(1.3*x, w2, width3, color='palegreen',label="KR Pthread join",edgecolor='black',hatch='//')

    ax.set_xscale('log')
    ax.minorticks_on()
    
    ax.set_xticks(x)
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())
    ax.legend(loc='upper left')        

    ax.set_xlabel("# nodes")
    ax.set_ylabel("Time (s)")
    plt.title('Shutdown cost')
   
    fstem='shutdown'
    fname=fstem+".png"
    plt.savefig(fname,format="png")
#    fname=fstem+".eps"
#    plt.savefig(fname,format="eps")
 
    plt.show()    

    

fname="MG-scale.dat"
mgdata=np.genfromtxt(fname, skip_header=1, usecols= range(0,10))
nodes=np.array(mgdata[:,0])
print nodes

mg_si=np.array(mgdata[:,1])
mg_spre=np.array(mgdata[:,2])
mg_ts=np.array(mgdata[:,3])
mg_wc=np.array(mgdata[:,4])
kr_si=np.array(mgdata[:,5])
kr_spre=np.array(mgdata[:,6])
kr_ts=np.array(mgdata[:,7])
kr_wc=np.array(mgdata[:,8])
lv=np.array(mgdata[:,9])
print lv
            

cname="crayPat.dat"
cpdata=np.genfromtxt(cname, skip_header=1, usecols= range(0,15))
mg_awc=np.array(cpdata[:,1])
mg_wcv=np.array(cpdata[:,2])
mg_mem=np.array(cpdata[:,3])
mg_mv=np.array(cpdata[:,4])
mg_gs=np.array(cpdata[:,5])
mg_he=np.array(cpdata[:,6])
mg_p=np.array(cpdata[:,7])

kr_awc=np.array(cpdata[:,8])
kr_wcv=np.array(cpdata[:,9])
kr_mem=np.array(cpdata[:,10])
kr_mv=np.array(cpdata[:,11])
kr_gs=np.array(cpdata[:,12])
kr_he=np.array(cpdata[:,13])
kr_p=np.array(cpdata[:,14])

print mg_mem
print kr_mem

#plot4Data(nodes, mg_si, kr_si, mg_spre, kr_spre)
pemg_si=pedata(mg_si,nodes)
pekr_si=pedata(kr_si,nodes)
#plot2Data(nodes, pemg_si, pekr_si, 1, "SI-solve")

pemg_spre=pedata(mg_spre,nodes)
pekr_spre=pedata(kr_spre,nodes)
#plot2Data(nodes, pemg_spre, pekr_spre, 1, "pressurek ")

mg_start=mg_wc-mg_ts
kr_start=kr_wc-kr_ts
#plot2Data(nodes, mg_start, kr_start, 0,"Start-up")

lv2=square(lv)
print "columns ..."
print lv2
lv2*=30
print "cells ..."
print lv2

#plot2DataLin(lv2, mg_mem, kr_mem, 0, "Memory")

#plot2Data(nodes, mg_mv, kr_mv, 0, "Matrix-vector")
pemg_mv=pedata(mg_mv,nodes)
pekr_mv=pedata(kr_mv,nodes)
#plot2Data(nodes, pemg_mv, pekr_mv, 1, "Matrix-vector")
#plot2DataLin(lv2,mg_mv,kr_mv, 1, "Matrix-vector")

#plot2Data(nodes,mg_gs,kr_gs,0, "Global-Sum")
#plot2Data(nodes,mg_he,kr_he,0, "Halo-Exchange")

mg_wcdiff=dabs_nparray(mg_wc,mg_awc)
kr_wcdiff=dabs_nparray(kr_wc,kr_awc)

#plot6Data(nodes, mg_wcdiff, kr_wcdiff, mg_wcv, kr_wcv, mg_p, kr_p)

si_rat= kr_si/mg_si
spre_rat=kr_spre/mg_spre
cname="kr_10m6.dat"
krdata=np.genfromtxt(cname, skip_header=1, usecols= range(0,7))
kr6_spre=np.array(krdata[:,4])
kr6_si=np.array(krdata[:,3])
pekr6_spre=pedata(kr6_spre,nodes)
kr6_gs=np.array(krdata[:,5])
kr6_he=np.array(krdata[:,6])

spre_rat2=kr6_spre/mg_spre
make2plots(nodes, pemg_spre, pekr_spre, pekr6_spre, spre_rat, spre_rat2)

comms2plots(nodes, mg_gs, kr_gs, kr6_gs, mg_he, kr_he, kr6_he)
