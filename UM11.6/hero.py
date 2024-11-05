import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

fname="perf.dat"
all_data=np.genfromtxt(fname, skip_header=2, usecols=range(0,3))

denom=np.array(all_data[0:5,0])
print( denom )
 
