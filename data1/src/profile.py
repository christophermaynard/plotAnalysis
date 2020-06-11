import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

import sys
fstem="../data/run_gungho_gh_profile_omp"
ompl="1","6","9"
mstem="nodes_C192_dt-900p0_intel_64-bit_"
nodel="6","12","24"
jobl="fast-debug","production"
estem="/timer.txt"

#alg_name="gungho"
#alg_pos=0

#alg_name="mass_matrix_solver"
#alg_pos=1

#alg_name="iter_timestep_alg"
#alg_pos=2

#alg_name="map_physics_fields"
#alg_pos=3

#alg_name="rhs_alg"
#alg_pos=4

#alg_name="advection_alg"
#alg_pos=5

alg_name="calc_phys_predictors"
alg_pos=6

#alg_name="semi_implicit_solver"
#alg_pos=8



count=0
ts_data=np.arange(18,dtype=np.float)


fname="../data/run_gungho_gh_profile_omp1_6nodes_C192_dt-900p0_intel_64-bit_fast-debug/timer.txt"
for job in jobl:
    for omp in ompl:
        for node in nodel:
            fname=fstem+omp+"_"+node+mstem+job+estem
            alldata=np.genfromtxt(fname, skip_header=1, usecols= range(2,3), delimiter="||")
            ts_data[count]=alldata[alg_pos]
            count=count+1

x=np.arange(3)
x[0]=6
x[1]=12
x[2]=24
### Slice 'n' dice
y1=np.array(ts_data[0:3])
y2=np.array(ts_data[3:6])
y3=np.array(ts_data[6:9])
z1=np.array(ts_data[9:12])
z2=np.array(ts_data[12:15])
z3=np.array(ts_data[15:18])

fig, ax = plt.subplots()
xlim=[4,32]
ax.set_xlim(xlim[0],xlim[1])
width=0.075*x
offset=0.075 
rects1 = ax.bar(x*(1-2*offset),y1,width,color='teal',edgecolor='black',label="FD1")
rects2 = ax.bar(x*(1-offset),y2,width,color='seagreen',edgecolor='black',label="FD6")
rects3 = ax.bar(x*1,y3,width,color='palegreen',edgecolor='black',label="FD9")
hects1 = ax.bar(x*(1+offset),z1,width,color='midnightblue',edgecolor='black',hatch='//',label="P1")
hrects2 = ax.bar(x*(1+2*offset),z2,width,color='dodgerblue',edgecolor='black',hatch='//',label="P6")
hrects3 = ax.bar(x*(1+3*offset),z3,width,color='lightskyblue',edgecolor='black',hatch='//',label="P9")
            
ax.set_xscale('log')
ax.minorticks_on()

ax.set_xticks(x)
ax.set_xticks(x)
ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
ax.get_xaxis().set_minor_locator(ticker.NullLocator())

ax.set_xlabel("# nodes")
ax.set_ylabel("time (s)")
plt.title(alg_name)
ax.legend(loc='upper right')        

pname=alg_name+str(".png")
plt.savefig(pname,format="png")
plt.show()    
