#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import sys

def pedata(x,y):
    z=np.empty_like(x)
    for i in range(len(x)):
        tmp = y[i]/y[0]
        z[i] = (x[0]/x[i])/tmp
    return z

def plot2Data(x, y1, y2, flag):

    fig, ax = plt.subplots()
    xlim=[72,1944]
    ax.set_xlim(xlim[0],xlim[1])

    c1='firebrick','purple'
    c2='goldenrod','hotpink'
    titles='Strong scaling of time-step for 100 time-steps','Parallel Efficiency on C1152 for 100 time-steps'
    fstem='ts_strong_scale','parallel_efficiency'

    if flag==1:
        psx=[96,1536]
        psy=[1.0, 1.0]
        l1 = ax.plot(psx,psy,color='black',linestyle='dashed',label="perfect scaling")

        
    width1=0.1*x
    width2=0.1*x
    rects1 = ax.bar(0.95*x, y1, width1, color=c1[flag],label="MG",edgecolor='black')
    rects2 = ax.bar(1.05*x, y2, width2, color=c2[flag],label="Krylov",edgecolor='black')

    ax.set_xscale('log')
    ax.minorticks_on()
    
    
    ax.set_xticks(x)
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.set_xlabel("# nodes")
    ax.set_ylabel("time (s)")
    plt.title('Strong scaling of solver on C1152')
    ax.legend(loc='upper right')        
        
    
    fname="inner_solve_scale.png"
    plt.savefig(fname,format="png")
#    fname=fstem[flag]+".eps"
#    plt.savefig(fname,format="eps")    
    plt.show()

def plot4Data(x, ya1, ya2, yb1, yb2, yc1, yc2, yd1, yd2 ):

    fig, ax = plt.subplots()
    xlim=[72,2304]
    ax.set_xlim(xlim[0],xlim[1])

    c1='firebrick','purple'
    c2='goldenrod','hotpink'
    titles='Strong scaling on C1152 for 100 time-steps','Parallel Efficiency on C1152 for 100 time-steps'
    fstem='ts_strong_scale','parallel_efficiency'

        
    width1=0.075*x
    width2=0.05*x*1.1
    width3=.05*x*1.2
    width4=.05*x*1.3
    
    rects1 = ax.bar(0.9*x, ya1, width1, color='red',label="MG_ts",edgecolor='black')
    rects2 = ax.bar(0.975*x, ya2, width1, color='goldenrod',label="Kr_ts",edgecolor='black',hatch='//')
    rects3 = ax.bar(1.1*x, yb1, width2, color='firebrick',label="MG_nons",edgecolor='black')
    rects4 = ax.bar(1.15*x, yb1, width2, color='darkorange',label="Kr_nons",edgecolor='black',hatch='//')
    rects5 = ax.bar(1.2*x, yc1, width2, color='sienna',label="MG_solv",edgecolor='black')
    rects6 = ax.bar(1.25*x, yc2, width2, color='salmon',label="Kr_solv",edgecolor='black',hatch='//')
    rects7 = ax.bar(1.325*x, yd1, width2, color='saddlebrown',label="MG_si",edgecolor='black')
    rects8 = ax.bar(1.375*x, yd2, width2, color='bisque',label="Kr_si",edgecolor='black',hatch='//')

    ax.set_xscale('log')
    ax.minorticks_on()
    
    
    ax.set_xticks(x)
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())


    ax.set_xlabel("# nodes")
    ax.set_ylabel("time (s)")
    plt.title(titles[0])

    fname=fstem[0]+".png"
    plt.savefig(fname,format="png")
    fname=fstem[0]+".eps"
    plt.savefig(fname,format="eps")    
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
    
    rects1 = ax.bar(0.875*x, y1, width1, color='midnightblue',label="MG fore",edgecolor='black')
    rects2 = ax.bar(0.95*x, y2, width1, color='teal',label="KR fore",edgecolor='black', hatch='//')
    rects3 = ax.bar(1.025*x, z1, width2, color='dodgerblue',label="MG Helm",edgecolor='black')
    rects4 = ax.bar(1.1225*x, z2, width2, color='seagreen',label="KR Helm",edgecolor='black',hatch='//')
    rects5 = ax.bar(1.2*x, w1, width3, color='lightskyblue',label="MG back",edgecolor='black')
    rects6 = ax.bar(1.3*x, w2, width3, color='palegreen',label="KR back",edgecolor='black',hatch='//')

    ax.set_xscale('log')
    ax.minorticks_on()
    
    
    ax.set_xticks(x)
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())
    ax.legend(loc='upper left')        

    ax.set_xlabel("# nodes")
    ax.set_ylabel("Parallel Efficiency")
  #  plt.title('Parallel Efficiency of solver components')
   
    fstem='pe_msp_comp'
    fname=fstem+".png"
    plt.savefig(fname,format="png")
    fname=fstem+".eps"
    plt.savefig(fname,format="eps")
 
    plt.show()    

    

fname="mg_solver.dat"
mgdata=np.genfromtxt(fname, skip_header=2, usecols= range(0,11))
nodes=np.array(mgdata[:,0])
mg_ts=np.array(mgdata[:,1])
mg_rhs=np.array(mgdata[:,2])
mg_adv=np.array(mgdata[:,3])
mg_si=np.array(mgdata[:,4])
mg_solv=np.array(mgdata[:,5])
mg_mschur_pre=np.array(mgdata[:,6])
mg_helm_mg=np.array(mgdata[:,7])
mg_helm_lhs=np.array(mgdata[:,8])
mg_back=np.array(mgdata[:,9])
mg_mop=np.array(mgdata[:,10])
mg_ts=mg_ts/(nodes*36)
#print mg_ts
mg_nonsolv = (mg_rhs+mg_adv)/(nodes*36)
mg_si=mg_si/(nodes*36)
mg_solv=mg_solv/(nodes*36)
#print mg_nonsolv
mg_mschur_pre=mg_mschur_pre/(nodes*36)
#print mg_mschur_pre
mg_helms=(mg_helm_mg+mg_helm_lhs)/(nodes*36)
#print mg_helms
mg_back=mg_back/(nodes*36)
#print mg_back
mg_mop=mg_mop/(nodes*36)
#print mg_mop


#print
fname="bicgstab_solver.dat"
bicgdata=np.genfromtxt(fname, skip_header=2, usecols= range(0,10))
nodes=np.array(bicgdata[:,0])
bicg_ts=np.array(bicgdata[:,1])
bicg_rhs=np.array(bicgdata[:,2])
bicg_adv=np.array(bicgdata[:,3])
bicg_si=np.array(bicgdata[:,4])
bicg_solv=np.array(bicgdata[:,5])
bicg_mschur_pre=np.array(bicgdata[:,6])
bicg_helm_lhs=np.array(bicgdata[:,7])
bicg_back=np.array(bicgdata[:,8])
bicg_mop=np.array(bicgdata[:,9])
bicg_ts=bicg_ts/(nodes*36)
#print bicg_ts
bicg_nonsolv = (bicg_rhs+bicg_adv)/(nodes*36)
bicg_si=bicg_si/(nodes*36)
bicg_solv=bicg_solv/(nodes*36)
#print bicg_nonsolv
bicg_mschur_pre=bicg_mschur_pre/(nodes*36)
#print bicg_mschur_pre
bicg_helms=(bicg_helm_lhs)/(nodes*36)
#print bicg_helms
bicg_back=(bicg_back)/(nodes*36)
#print bicg_back
bicg_mop=(bicg_mop)/(nodes*36)
#print bicg_mop


#print
#for i in range(0,4):
#    print str(pedata(bicg_helms[i:(i+2)],nodes[i:(i+2)])[1]) + " " + str(pedata(mg_helms[i:(i+2)],nodes[i:(i+2)])[1])

ns=pedata(mg_nonsolv,nodes)
mgp=pedata(mg_solv, nodes)
bicgp=pedata(bicg_solv, nodes)
#plot3Data(nodes,ns,mgp,bicgp)

mg_mschur_p=pedata(mg_mschur_pre,nodes)
bicg_mschur_p=pedata(bicg_mschur_pre,nodes)

mopp=pedata(bicg_mop,nodes)
#plot3Data(nodes,mopp,mg_mschur_p,bicg_mschur_p)

mg_mschur_rest=mg_mschur_pre - mg_helms - mg_back
bicg_mschur_rest=bicg_mschur_pre - bicg_helms - bicg_back
print

    
m1=pedata(mg_mschur_rest,nodes)
m2=pedata(mg_helms,nodes)
m3=pedata(mg_back,nodes)
b1=pedata(bicg_mschur_rest,nodes)
b2=pedata(bicg_helms,nodes)
b3=pedata(bicg_back,nodes)

#plot6Data(nodes, m1, b1, m2, b2, m3, b3)


#mgpe=pedata(mgdat,nodes)
#bicgstabpe=pedata(bicgstabdat,nodes)

#plot2Data(nodes, mg_helms, bicg_helms,0)
m4=pedata(mg_ts,nodes)
b4=pedata(bicg_ts,nodes)
#plot2Data(nodes, m4, b4,0)
plot2Data(nodes, mg_helms, bicg_helms,0)

