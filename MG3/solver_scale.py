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
    xlim=[288,4374]
    ax[0].set_xlim(xlim[0],xlim[1])
    ax[0].set_xscale('log')
    width1=0.1*x
#    rects1 = ax[1].bar(0.95*x, y1, width1, color='dodgerblue',label="MG",edgecolor='black')
    rects1 = ax[1].bar(0.95*x, y1, width1, color='black',label="MG",edgecolor='black')
#    rects2 = ax[1].bar(1.05*x, y2, width1, color='mediumblue',label="Kr2",edgecolor='black',hatch='//')
    rects2 = ax[1].bar(1.05*x, y2, width1, color='gray',label="Kr2",edgecolor='black',hatch='//')
#    rects3 = ax[1].bar(1.15*x, y3, width1, color='skyblue',label="Kr6",edgecolor='black',hatch='\\\\')
    rects3 = ax[1].bar(1.15*x, y3, width1, color='lightgray',label="Kr6",edgecolor='black',hatch='\\\\')    

#    rects4 = ax[0].bar(0.95*x, z1, width1, color='firebrick',label="MG",edgecolor='black')
    rects4 = ax[0].bar(0.95*x, z1, width1, color='dimgrey',label="MG",edgecolor='black')
#    rects5 = ax[0].bar(1.05*x, z2, width1, color='goldenrod',label="Kr2",edgecolor='black',hatch='//')
    rects5 = ax[0].bar(1.05*x, z2, width1, color='silver',label="Kr2",edgecolor='black',hatch='//')
#    rects6 = ax[0].bar(1.15*x, z3, width1, color='sienna',label="Kr6",edgecolor='black',hatch='\\\\')
    rects6 = ax[0].bar(1.15*x, z3, width1, color='whitesmoke',label="Kr6",edgecolor='black',hatch='\\\\')

    ax[1].minorticks_on()
    ax[1].set_xticks(x)
    ax[1].set_xticks(x)
    ax[1].get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax[1].get_xaxis().set_minor_locator(ticker.NullLocator())
    ax[1].set_xlabel("# nodes")
    ax[1].set_ylabel("MPI_allreduce (s)")
    ax[0].set_ylabel("MPI_send/receive (s)")
    
    ax[1].legend(loc='upper left',bbox_to_anchor=(0.2,1.0))
    ax[0].legend(loc='upper right')
        
    
    fname="comms_scale_bw.png"
    plt.savefig(fname,format="png")
    fname="comms_scale_bw.eps"
    plt.savefig(fname,format="eps")    
    plt.show()    

def make2plots(x, y1, y2, y3, z1, z2, name):

    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
    fig.subplots_adjust(hspace=0)
    xlim=[288,4374]
    ax[0].set_xlim(xlim[0],xlim[1])
    ax[0].set_xscale('log')    

    psx=[384,3456]
    psy=[1.0, 1.0]
    l1 = ax[1].plot(psx,psy,color='black',linestyle='dashed',label="perfect scaling")

        
    width1=0.1*x
#    rects1 = ax[1].bar(0.95*x, y1, width1, color='dodgerblue',label="MG",edgecolor='black')
    rects1 = ax[1].bar(0.95*x, y1, width1, color='black',label="MG",edgecolor='black')
#    rects2 = ax[1].bar(1.05*x, y2, width1, color='mediumblue',label="Kr2",edgecolor='black',hatch='//')
    rects2 = ax[1].bar(1.05*x, y2, width1, color='gray',label="Kr2",edgecolor='black',hatch='//')
    rects3 = ax[1].bar(1.15*x, y3, width1, color='lightgrey',label="Kr6",edgecolor='black',hatch='\\\\')

#    rects4 = ax[0].bar(0.95*x, z1, width1, color='teal',label="Kr2",edgecolor='black',hatch='--')
    rects4 = ax[0].bar(0.95*x, z1, width1, color='dimgrey',label="Kr2",edgecolor='black',hatch='--')    
#    rects5 = ax[0].bar(1.05*x, z2, width1, color='powderblue',label="Kr6",edgecolor='black')
    rects5 = ax[0].bar(1.05*x, z2, width1, color='whitesmoke',label="Kr6",edgecolor='black')
    
    ax[1].minorticks_on()
    ax[1].set_xticks(x)
    ax[1].set_xticks(x)
    ax[1].get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax[1].get_xaxis().set_minor_locator(ticker.NullLocator())
    ax[1].set_xlabel("# nodes")
    ax[1].set_ylabel("PE")
    ax[0].set_ylabel("R=Kr/MG")
    
    ax[1].legend(loc='lower left')
    ax[0].legend(loc='upper left')#,bbox_to_anchor=(1.0,1.15))
        
    
    fname=name+"_scale_bw.png"
    plt.savefig(fname,format="png")
    fname=name+"_scale_bw.eps"
    plt.savefig(fname,format="eps")
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

    

fname="all_data.dat"
mgdata=np.genfromtxt(fname, skip_header=1, usecols= range(0,8))
allnodes=np.array(mgdata[:,0])
nodes=np.array(mgdata[0:4,0])

mg_wc=np.array(mgdata[0:4,1])
mg_ts=np.array(mgdata[0:4,2])
mg_si=np.array(mgdata[0:4,3])
mg_mp=np.array(mgdata[0:4:,4])
mg_awc=np.array(mgdata[0:4:,5])
mg_gs=np.array(mgdata[0:4:,6])
mg_he=np.array(mgdata[0:4:,7])

kr_wc=np.array(mgdata[4:8,1])
kr_ts=np.array(mgdata[4:8,2])
kr_si=np.array(mgdata[4:8,3])
kr_mp=np.array(mgdata[4:8:,4])
kr_awc=np.array(mgdata[4:8:,5])
kr_gs=np.array(mgdata[4:8:,6])
kr_he=np.array(mgdata[4:8:,7])

kr6_wc=np.array(mgdata[8:12,1])
kr6_ts=np.array(mgdata[8:12,2])
kr6_si=np.array(mgdata[8:12,3])
kr6_mp=np.array(mgdata[8:12:,4])
kr6_awc=np.array(mgdata[8:12:,5])
kr6_gs=np.array(mgdata[8:12:,6])
kr6_he=np.array(mgdata[8:12:,7])

#print mg_si/400.0
#print mg_mp/400.0

#print kr_si/400.0
#print kr_mp/400.0

#print kr6_si/400.0
#print kr6_mp/400.0


#plot4Data(nodes, mg_si, kr_si, mg_spre, kr_spre)
pemg_mp=pedata(mg_mp,nodes)
pekr_mp=pedata(kr_mp,nodes)
pekr6_mp=pedata(kr6_mp,nodes)

mp_rat1=kr_mp/mg_mp
mp_rat2=kr6_mp/mg_mp
make2plots(nodes, pemg_mp, pekr_mp, pekr6_mp, mp_rat1, mp_rat2, "pressure")

smg_gs=mg_gs/400.0
skr_gs=kr_gs/400.0
skr6_gs=kr6_gs/400.0
smg_he=mg_he/400.0
skr_he=kr_he/400.0
skr6_he=kr6_he/400.0
comms2plots(nodes, smg_gs, skr_gs, skr6_gs, smg_he, skr_he, skr6_he)

pemg_si=pedata(mg_si, nodes)
pekr_si=pedata(kr_si,nodes)
pekr6_si=pedata(kr6_si,nodes)
si_rat1=kr_si/mg_si
si_rat2=kr6_si/mg_si
make2plots(nodes, pemg_si, pekr_si, pekr6_si, si_rat1, si_rat2, "semi-implicit")

#print mg_si/mg_ts
#print kr_si/kr_ts
#print kr6_si/kr6_ts
pemg_ts=pedata(mg_ts, nodes)
pekr_ts=pedata(kr_ts,nodes)
pekr6_ts=pedata(kr6_ts,nodes)
ts_rat1=kr_ts/mg_ts
ts_rat2=kr6_ts/mg_ts
#make2plots(nodes, pemg_ts, pekr_ts, pekr6_ts, ts_rat1, ts_rat2, "time-step")


mg_si_op=np.fromstring('190.0, 94.0, 51.0, 25.0',dtype=float, sep=",")
print(mg_si_op/mg_wc)
print(mg_si_op/mg_ts)
print(mg_si_op/mg_si)
print(mg_si_op/mg_mp)
print()
#                                          16 is spoofed.
kr_si_op=np.fromstring('133.0, 61.0, 32.0, 16.0',dtype=float, sep=",")
print(kr_si_op/kr_wc)
print(kr_si_op/kr_ts)
print(kr_si_op/kr_si)
print(kr_si_op/kr_mp)

print()
print(mg_si_op/kr_si_op)

print((mg_si_op-kr_si_op)/mg_mp)
