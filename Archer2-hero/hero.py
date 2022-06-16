import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

def plotdata(x,s,w, labels):
    fig, ax = plt.subplots()
    width=0.25
    rect1 = ax.bar(x,s,width,color='teal',label='strong', edgecolor='black')
    rect2 = ax.bar(x+0.3,w,width,color='darkseagreen',label='weak', edgecolor='black')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("PE")
    ax.legend(loc='lower right')
    plt.savefig('scale.png',format="png")
    plt.show()
0    

fname="perf.dat"
all_data=np.genfromtxt(fname, skip_header=2, usecols=range(0,3))

C1P1=np.array(all_data[0:5,0])
C1P2=np.array(all_data[0:5,1])
C2P2=np.array(all_data[0:5,2])

# sum the advections 
DC1P1=np.array(C1P1[0:4])
DC1P1[3]=DC1P1[3]+C1P1[4]
DC1P2=np.array(C1P2[0:4])
DC1P2[3]=DC1P2[3]+C1P2[4]
DC2P2=np.array(C2P2[0:4])
DC2P2[3]=DC2P2[3]+C2P2[4]

# make spurious x
x=np.array(DC1P1[0:4])
for i in range(0,4):
    x[i]=i

# strong and weak scaling
s=( (DC1P1/DC1P2)/4.0 )
w=( (DC1P1/DC2P2) )
labels=['time_step','si_solve','helm_solve','adv']
print(labels)
plotdata(x,s,w,labels)
