import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

changelog = [['4/1 r33206', ''],
             ['11/1 r33285', ''],
             ['18/1 r33436', 'Update to lfric performance test'],
             ['25/1 r33540', ''],
             ['1/2 r33720', 'Transport rewrite & addition C48 lfric test'],
             ['8/2 r33808', ''],
             ['15/2 r33872', ''],
             ['22/2 r34114', ''],
             ['1/3 r34207', ''],
             ['8/3 r34390', ''],
             ['15/3 r34476', ''],
             ['22/3 r34719', ''],
             ['29/3 r34854', ''],
             ['05/4 r35008', ''],
             ['19/4 r35275', '']]

#=== Results from gungho tests
# Times of omp6_*nodes job
nodes6 = [468.30, 469.00, 468.78, 470.47, 456.47, 449.55, 465.29, 465.36, 464.51, 450.13, 451.23, 451.41, 457.19, 456.49, 464.98]
nodes12 = [235.79, 239.34, 232.02, 236.77, 227.29, 231.21, 225.25, 234.95, 223.30, 223.36, 226.43, 224.83, 225.72, 234.61, 226.68]
nodes24 = [128.12, 127.02, 143.3, 126.83, 122.20, 121.68, 125.75, 128.82, 129.60, 119.75, 123.95, 119.86, 121.46, 125.10, 122.22]
speedup6to12 = np.divide(nodes6,nodes12)
speedup12to24 = np.divide(nodes12,nodes24)

# Timestepping time of omp*_12nodes job
omp1 = [218.82, 223.33, 243.05, 218.62, 206.67, 215.16, 211.28, 208.24, 214.35, 205.38, 205.30, 206.23, 207.18, 213.53, 207.34]
omp6 = [218.33, 222.55, 212.38, 220.77, 207.15, 210.44, 204.77, 214.26, 202.93, 203.41, 207.07, 205.02, 206.11, 215.02, 206.87]
omp9 = [230.20, 227.20, 223.91, 231.26, 217.72, 216.54, 226.96, 223.33, 220.28, 212.80, 213.35, 213.58, 225.71, 218.58, 217.25]

# Component cost of omp6_*nodes jobs
solver6nodes = [242.44, 241.49, 243.33, 246.32, 246.62, 243.27, 251.09, 244.26, 251.03, 243.77, 243.09, 244.77, 245.74, 241.98, 245.08]
solver12nodes = [119.19, 119.39, 116.36, 121.15, 118.60, 118.93, 117.54, 122.64, 117.27, 116.61, 119.51, 119.23, 118.97, 118.14, 117.95]
solver24nodes = [64.68, 62.62, 71.86, 64.54, 64.53, 64.16, 64.24, 68.97, 67.55, 63.41, 68.48, 64.52, 64.97, 66.36, 62.79]
solverspeedup6to12 = np.divide(solver6nodes,solver12nodes)
solverspeedup12to24 = np.divide(solver12nodes,solver24nodes)

rhs6nodes = [20.80, 21.02, 21.17, 22.03, 22.98, 21.17, 25.51, 24.54, 25.65, 21.55, 21.38, 23.49, 21.02, 21.70, 23.61]
rhs12nodes = [10.36, 11.31, 10.67, 11.19, 11.45, 12.54, 11.43, 10.71, 10.53, 10.63, 11.41, 10.88, 10.67, 10.66, 10.63]
rhs24nodes = [5.45, 5.40, 9.22, 5.44, 5.95, 5.61, 5.45, 6.19, 6.28, 5.41, 5.54, 5.94, 5.42, 5.45, 5.62]
rhsspeedup6to12 = np.divide(rhs6nodes,rhs12nodes)
rhsspeedup12to24 = np.divide(rhs12nodes,rhs24nodes)

advection6nodes = [75.23, 75.77, 74.15, 74.60, 54.91, 53.33, 53.55, 54.86, 53.15, 53.53, 51.71, 51.25, 51.04, 53.64, 53.38]
advection12nodes = [37.00, 36.63, 36.07, 36.95, 27.44, 25.78, 26.81, 27.14, 24.80, 23.62, 26.30, 24.47, 24.78, 28.15, 24.57]
advection24nodes = [18.26, 17.99, 17.73, 18.12, 12.30, 12.18, 15.20, 12.90, 14.58, 11.51, 12.04, 11.66, 11.48, 12.55, 12.36]
advectionspeedup6to12 = np.divide(advection6nodes,advection12nodes)
advectionspeedup12to24 = np.divide(advection12nodes,advection24nodes)

# 12 nodes omp scaling
solver6threads = solver12nodes
rhs6threads = rhs12nodes
advection6threads = advection12nodes

solver1thread = [115.87, 115.99, 124.68, 113.00, 113.65, 119.47, 118.94, 118.65, 119.35, 114.55, 116.00, 116.46, 117.00, 120.57, 114.17]
solver9threads = [127.62, 122.96, 123.28, 125.84, 126.29, 124.56, 129.15, 129.73, 128.96, 124.33, 124.66, 124.41, 127.08, 127.57, 123.55]
rhs1thread = [11.58, 11.63, 11.42, 11.19, 11.42, 11.68, 11.65, 11.74, 12.22, 12.65, 11.33, 12.00, 11.32, 12.96, 11.21]
rhs9threads = [11.43, 10.59, 10.85, 10.74, 11.03, 12.29, 13.11, 11.11, 12.49, 10.53, 10.61, 10.85, 11.88, 11.80, 11.18]
advection1thread =[38.02, 37.40, 36.60, 36.34, 25.64, 25.78, 26.38, 24.47, 26.04, 23.65, 24.24, 25.13, 23.83, 24.77, 24.30]
advection9threads = [38.46, 39.98, 38.40, 38.74, 28.36, 28.58, 30.64, 30.26, 27.87, 28.14, 27.36, 27.16, 31.42, 27.10, 27.71]
advectionompspeedup1to6 = np.divide(advection1thread,advection6threads)
advectionompspeedup1to9 = np.divide(advection1thread,advection9threads)
rhsompspeedup1to6 = np.divide(rhs1thread,rhs6threads)
rhsompspeedup1to9 = np.divide(rhs1thread,rhs9threads)
solverompspeedup1to6 = np.divide(solver1thread,solver6threads)
solverompspeedup1to9 = np.divide(solver1thread,solver9threads)

# Times of C64-omp2_*mpi job
mpi96 = [0.0 ,0.0, 0.0, 0.0, 855.69, 819.15, 869.55, 882.53, 817.59, 828.66, 817.64, 815.66, 852.17, 841.24, 844.51]
mpi192 = [0.0 ,0.0, 0.0, 0.0, 533.96, 496.03, 529.84, 516.40, 477.08, 499.56, 490.48, 489.27, 522.11, 495.57, 507.36] 
mpi384 = [0.0 ,0.0, 0.0, 0.0, 395.30, 320.02, 331.31, 320.14, 331.60, 350.68, 324.89, 326.53, 332.99, 326.95, 327.06]
speedup96to192 = np.divide(mpi96,mpi192)
speedup192to384 = np.divide(mpi192,mpi384)

crun_per_year = 365./30.
day = 86400.
sypd_mpi96 = day/(crun_per_year*np.array(mpi96))
sypd_mpi192 = day/(crun_per_year*np.array(mpi192))
sypd_mpi384 = day/(crun_per_year*np.array(mpi384))

print( 'sypd96 = ',sypd_mpi96)
print( 'sypd192 = ',sypd_mpi192)
print( 'sypd384 = ',sypd_mpi384)

# Results from basic_gal (NWP) test

gal_lfric_nodes24 = [1426.41, 1518.82, 1070.74, 1059.81, 835.56, 876.20, 829.84, 831.57, 840.15, 836.20, 826.52, 837.38, 846.77, 851.11, 871.91]
gal_lfric_nodes96 = [1255.52, 1291.03, 725.76, 731.88, 663.17, 695.85, 680.65, 660.05, 659.83, 742.30, 652.68, 673.69, 677.52, 678.94, 677.37]

gal_lfric_solver_nodes24 = [155.56, 160.76, 151.53, 150.46, 147.56, 161.12, 147.69, 142.75, 139.43, 143.05, 142.94, 146.08, 143.47, 150.92, 149.69]
gal_lfric_solver_nodes96 = [64.34, 57.17, 56.71, 58.13, 55.54, 59.99, 57.30, 52.19, 55.03, 52.09, 52.92, 56.92, 54.44, 57.39, 52.65]

gal_lfric_rhs_nodes24 = [26.51, 26.76, 24.23, 25.76, 23.72, 23.25, 26.25, 25.42, 23.46, 23.27, 23.26, 23.82, 22.90, 23.11, 25.12]
gal_lfric_rhs_nodes96 = [7.15, 7.39, 7.10, 7.22, 7.26, 7.13, 7.17, 7.03, 6.94, 7.03, 6.96, 6.95, 6.93, 6.96, 7.07]

gal_lfric_advection_nodes24 = [483.65, 550.46, 310.50, 320.72, 192.29, 198.86, 196.15, 199.15, 198.26, 198.88, 193.56, 200.83, 207.02, 208.08, 214.67]
gal_lfric_advection_nodes96 = [140.06, 141.44, 82.01, 88.13, 50.02, 52.03, 56.99, 50.95, 50.95, 48.32, 48.90, 52.64, 55.48, 57.55, 63.84]

gal_lfric_fast_nodes24 = [87.47, 85.42, 58.04, 58.11, 58.79, 58.42, 58.05, 58.55, 58.39, 60.02, 62.39, 58.93, 63.26, 62.03, 61.14]
gal_lfric_fast_nodes96 = [64.73, 67.34, 16.33, 15.37, 15.83, 16.36, 15.82, 16.08, 15.06, 15.70, 15.12, 16.44, 15.39, 15.89, 15.30]

gal_lfric_slow_nodes24 = [310.38, 320.62, 213.71, 211.57, 126.80, 128.14, 122.49, 121.00, 121.16, 119.02, 123.31, 120.49, 119.48, 119.81, 120.64]
gal_lfric_slow_nodes96 = [329.23, 344.21, 60.46, 59.54, 38.10, 44.63, 35.69, 33.81, 34.13, 33.70, 34.62, 35.48, 33.91, 33.74, 34.12]

gal_lfric_timestep_nodes24 = [1174.46, 1258.71, 866.53, 876.70, 656.81, 672.70, 654.80, 651.47, 645.60, 654.03, 651.98, 660.87, 664.98, 673.27, 678.29]
gal_lfric_timestep_nodes96 = [637.05, 655.19, 254.23, 260.24, 197.97, 211.68, 205.97, 195.42, 195.17, 189.09, 191.87, 200.80, 199.65, 206.03, 206.52]

gal_lfric_setup_nodes24 = [251.95, 260.11, 204.21, 183.12, 178.75, 203.5, 175.04, 180.10, 194.55, 182.17, 174.54, 176.51, 181.79, 177.84, 193.62]
gal_lfric_setup_nodes96 = [618.47, 635.84, 471.53, 471.64, 465.2, 484.17, 474.68, 464.63, 464.66, 553.21, 460.81, 472.89, 477.87, 472.91, 470.85]


speedup24to96 = np.divide(gal_lfric_nodes24,gal_lfric_nodes96)
solverspeedup24to96 = np.divide(gal_lfric_solver_nodes24,gal_lfric_solver_nodes96)
rhsspeedup24to96 = np.divide(gal_lfric_rhs_nodes24,gal_lfric_rhs_nodes96)
advectionspeedup24to96 = np.divide(gal_lfric_advection_nodes24,gal_lfric_advection_nodes96)
fastspeedup24to96 = np.divide(gal_lfric_fast_nodes24,gal_lfric_fast_nodes96)
slowspeedup24to96 = np.divide(gal_lfric_slow_nodes24,gal_lfric_slow_nodes96)
setupspeedup24to96 = np.divide(gal_lfric_setup_nodes24,gal_lfric_setup_nodes96)
timestepspeedup24to96 = np.divide(gal_lfric_timestep_nodes24,gal_lfric_timestep_nodes96)

# UM times
um_labels = ['Total', 'Solver', 'Transport', 'Fast physics', 'Slow physics', 'Setup']
um = [211.52, 28.01, 28.53, 54.3, 84.17, 3.44]
um_factor = 1.0/0.72
um2lfric_total = np.multiply(um_factor/um[0],gal_lfric_nodes24)
um2lfric_solver = np.multiply(um_factor/um[1],gal_lfric_solver_nodes24)
um2lfric_transport = np.multiply(um_factor/um[2],gal_lfric_advection_nodes24)
um2lfric_fast = np.multiply(um_factor/um[3],gal_lfric_fast_nodes24)
um2lfric_slow = np.multiply(um_factor/um[4],gal_lfric_slow_nodes24)
um2lfric_setup = np.multiply(um_factor/um[5],gal_lfric_setup_nodes24)
print('um2lfric_total = ',um2lfric_total)


# Results from proto_gal (climate) test

proto_gal_lfric_nodes3 = [0.0, 0.0, 0.0, 0.0, 4802.61, 4854.46, 4828.29, 4822.05, 4743.58, 4825.96, 4742.62, 4755.42, 4880.91, 3042.82, 3176.71]
proto_gal_lfric_nodes6 = [0.0, 0.0, 0.0, 0.0, 2535.32, 2589.61, 2526.20, 2536.04, 2518.50, 2577.55, 2492.63, 2480.07, 2557.72, 1667.40, 1708.20]

proto_gal_lfric_solver_nodes3 = [0.0, 0.0, 0.0, 0.0, 427.68, 431.02, 433.56, 438.74, 408.63, 423.09, 415.35, 416.79, 457.22, 412.31, 439.78]
proto_gal_lfric_solver_nodes6 = [0.0, 0.0, 0.0, 0.0, 257.56, 253.65, 249.20, 264.95, 243.52, 234.80, 245.77, 239.33, 244.91, 249.35, 255.71]

proto_gal_lfric_rhs_nodes3 = [0.0, 0.0, 0.0, 0.0, 77.04, 78.22, 76.34, 75.71, 73.85, 73.97, 75.98, 76.01, 77.67, 75.52, 77.17]
proto_gal_lfric_rhs_nodes6 = [0.0, 0.0, 0.0, 0.0, 42.96, 42.27, 41.80, 44.30, 42.49, 40.42, 42.13, 42.13, 45.65, 41.97, 42.29]

proto_gal_lfric_advection_nodes3 = [0.0, 0.0, 0.0, 0.0, 939.78, 964.09, 962.28, 967.20, 949.96, 949.18, 940.46, 956.74, 958.20, 981.38, 1004.26]
proto_gal_lfric_advection_nodes6 = [0.0, 0.0, 0.0, 0.0, 463.43, 468.13, 469.83, 488.83, 492.36, 462.68, 465.58, 464.80, 478.03, 510.40, 490.65]

proto_gal_lfric_fast_nodes3 = [0.0, 0.0, 0.0, 0.0, 191.42, 190.04, 192.85, 198.06, 191.62, 190.5, 191.11, 189.00, 211.07, 206.88, 214.05]
proto_gal_lfric_fast_nodes6 = [0.0, 0.0, 0.0, 0.0, 103.08, 100.52, 99.73, 102.34, 101.51, 100.32, 101.08, 99.92, 108.80, 113.47, 147.60]

proto_gal_lfric_slow_nodes3 = [0.0, 0.0, 0.0, 0.0, 599.02, 625.98, 574.01, 572.89, 574.04, 596.86, 567.69, 563.47, 590.27, 570.21, 592.87]
proto_gal_lfric_slow_nodes6 = [0.0, 0.0, 0.0, 0.0, 327.90, 353.06, 306.40, 303.78, 306.24, 396.52, 300.35, 296.91, 308.67, 298.47, 295.64]

proto_gal_lfric_ukca_nodes3 = [0.0, 0.0, 0.0, 0.0, 2054.67, 2051.31, 2062.46, 2057.82, 2056.08, 2060.84, 2057.80, 2059.74, 2061.35, 362.97, 363.65]
proto_gal_lfric_ukca_nodes6 = [0.0, 0.0, 0.0, 0.0, 1029.04, 1028.39, 1030.93, 1027.44, 1029.80, 1032.29, 1030.17, 1031.98, 1033.44, 182.06, 182.47]

proto_gal_lfric_setup_nodes3 = [0.0, 0.0, 0.0, 0.0, 64.59, 75.36, 77.69, 64.26, 60.5, 81.10, 57.89, 59.16, 54.85, 59.27, 73.16]
proto_gal_lfric_setup_nodes6 = [0.0, 0.0, 0.0, 0.0, 52.53, 87.14, 68.86, 50.93, 54.59, 60.42, 53.36, 57.11, 52.34, 51.47, 53.17]

speedup3to6 = np.divide(proto_gal_lfric_nodes3,proto_gal_lfric_nodes6)
solverspeedup3to6 = np.divide(proto_gal_lfric_solver_nodes3,proto_gal_lfric_solver_nodes6)
rhsspeedup3to6 = np.divide(proto_gal_lfric_rhs_nodes3,proto_gal_lfric_rhs_nodes6)
advectionspeedup3to6 = np.divide(proto_gal_lfric_advection_nodes3,proto_gal_lfric_advection_nodes6)
fastspeedup3to6 = np.divide(proto_gal_lfric_fast_nodes3,proto_gal_lfric_fast_nodes6)
slowspeedup3to6 = np.divide(proto_gal_lfric_slow_nodes3,proto_gal_lfric_slow_nodes6)
ukcaspeedup3to6 = np.divide(proto_gal_lfric_ukca_nodes3,proto_gal_lfric_ukca_nodes6)
setupspeedup3to6 = np.divide(proto_gal_lfric_setup_nodes3,proto_gal_lfric_setup_nodes6)

crun_per_year = 365./15.
day = 86400.
sypd_nodes3 = day/(crun_per_year*np.array(proto_gal_lfric_nodes3))
sypd_nodes6 = day/(crun_per_year*np.array(proto_gal_lfric_nodes6))

print( 'sypd3 = ',sypd_nodes3)
print( 'sypd6 = ',sypd_nodes6)

labels = [changelog[i][0] for i in range(len(nodes6))]
print(labels[:])

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
# Plot the cost for 6omp threads
fig, (ax, bx) = plt.subplots(2,1,figsize=(15,7),gridspec_kw={'height_ratios': [3, 1]})
rects1 = ax.bar(x - width, nodes6, width, label='6 Nodes')
rects2 = ax.bar(x        , nodes12, width, label='12 Nodes')
rects3 = ax.bar(x + width, nodes24, width, label='24 Nodes')

ax.set_ylabel('Time (s)')
ax.set_title('Gungho model cost, 6 omp threads')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

bx.plot(x,speedup6to12,'b',label='Speedup 6 to 12 nodes')
bx.plot(x,speedup12to24,'g',label='Speedup 12 to 24 nodes')
bx.set_xticks(x)
bx.set_xticklabels(labels)
bx.legend()


fig.tight_layout()
fig.autofmt_xdate(rotation=45)

plt.savefig('Gungho-mpi.png')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

# Plot the cost for C64 2omp threads test
fig, (ax, bx, cx) = plt.subplots(3,1,figsize=(15,7),gridspec_kw={'height_ratios': [3, 1, 1]})
rects1 = ax.bar(x - width, mpi96, width, label='96 mpi')
rects2 = ax.bar(x        , mpi192, width, label='192 mpi ')
rects3 = ax.bar(x + width, mpi384, width, label='384 mpi')

ax.set_ylabel('Time (s)')
ax.set_title('C64 Gungho model cost, 2 omp threads')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

bx.plot(x,speedup96to192,'b',label='Speedup 96 to 192 mpi parts')
bx.plot(x,speedup192to384,'g',label='Speedup 96 to 384 mpi parts')
bx.set_xticks(x)
bx.set_xticklabels(labels)
bx.legend()

cx.plot(x,sypd_mpi96,'b',label='SYPD - 96 mpi parts')
cx.plot(x,sypd_mpi192,'g',label='SYPD - 192 mpi parts')
cx.plot(x,sypd_mpi384,'r',label='SYPD - 384 mpi parts')
cx.set_xticks(x)
cx.set_xticklabels(labels)
cx.legend()


fig.tight_layout()
fig.autofmt_xdate(rotation=45)

plt.savefig('Gungho-C64-mpi.png')


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
# Plot the cost for 12 nodes
fig, (ax, bx) = plt.subplots(2,1,figsize=(15,7),gridspec_kw={'height_ratios': [3, 1]})
rects1 = ax.bar(x - width, omp1, width, label='1 Thread')
rects2 = ax.bar(x        , omp6, width, label='6 Threads')
rects3 = ax.bar(x + width, omp9, width, label='9 Threads')

ax.set_ylabel('Time (s)')
ax.set_title('Gungho model cost, 12 nodes')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
bx.plot(x,solverompspeedup1to6,'b',label='Solver Speedup 1 to 6 threads')
bx.plot(x,solverompspeedup1to9,'b--',label='Solver Speedup 1 to 9 threads')
bx.plot(x,rhsompspeedup1to6,'g',label='RHS Speedup 1 to 6 threads')
bx.plot(x,rhsompspeedup1to9,'g--',label='RHS Speedup 1 to 9 threads')
bx.plot(x,advectionompspeedup1to6,'r',label='Advection Speedup 1 to 6 threads')
bx.plot(x,advectionompspeedup1to9,'r--',label='Advection Speedup 1 to 9 threads')
bx.set_xticks(x)
bx.set_xticklabels(labels)
bx.legend(bbox_to_anchor=(1.05, 1), loc='upper left',)
fig.autofmt_xdate(rotation=45)
fig.tight_layout()
plt.savefig('Gungho-omp.png')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
# Plot the gungho component cost
fig, (ax, bx) = plt.subplots(2,1,figsize=(15,7),gridspec_kw={'height_ratios': [3, 1]})
rects1 = ax.bar(x - width, solver12nodes, width, label='Solver')
rects2 = ax.bar(x        , rhs12nodes, width, label='RHS')
rects3 = ax.bar(x + width, advection12nodes, width, label='Advection')

ax.set_ylabel('Time (s)')
ax.set_title('Gungho component cost, 12 nodes, 6 threads')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

bx.plot(x,solverspeedup6to12,'b',label='Solver Speedup 6 to 12 nodes')
bx.plot(x,solverspeedup12to24,'b--',label='Solver Speedup 12 to 24 nodes')
bx.plot(x,rhsspeedup6to12,'g',label='RHS Speedup 6 to 12 nodes')
bx.plot(x,rhsspeedup12to24,'g--',label='RHS Speedup 12 to 24 nodes')
bx.plot(x,advectionspeedup6to12,'r--',label='Advection Speedup 6 to 12 nodes')
bx.plot(x,advectionspeedup12to24,'r--',label='Advection Speedup 12 to 24 nodes')
bx.set_xticks(x)
bx.set_xticklabels(labels)
bx.legend(bbox_to_anchor=(1.05, 1), loc='upper left',)
fig.tight_layout()
fig.autofmt_xdate(rotation=45)
plt.savefig('GH-component.png')


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

# Plot the cost for the gal_lfric_atm job
#fig, ax = plt.subplots(1,1,figsize=(15,7))
fig, (ax, bx, cx) = plt.subplots(3,1,figsize=(15,7),gridspec_kw={'height_ratios': [3, 1, 1]})
rects1 = ax.bar(x[:]-width/2, gal_lfric_nodes24[:], width, label='24 Nodes')
rects2 = ax.bar(x[:]+width/2, gal_lfric_nodes96[:], width, label='96 Nodes')

ax.set_ylabel('Time (s)')
ax.set_title('GAL LFRic_atm model cost')
ax.set_xticks(x[:])
ax.set_xticklabels(labels[:])
fig.autofmt_xdate(rotation=45)
ax.legend()

bx.plot(x,gal_lfric_timestep_nodes24,'b',label='Timestepping 24 nodes')
bx.set_xticks(x)
bx.set_xticklabels(labels)
bx.legend()


cx.plot(x,speedup24to96,'b',label='Speedup 24 to 96 nodes')
cx.set_xticks(x)
cx.set_xticklabels(labels)
cx.legend()


plt.savefig('GAL-LFRic.png')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
# Plot the GAL LFRic component cost
width2 = width * 3.0/6.0
fig, (ax, bx) = plt.subplots(2,1,figsize=(15,7),gridspec_kw={'height_ratios': [3, 1]})
rects1 = ax.bar(x - 3.0*width2, gal_lfric_timestep_nodes24, width2, label='Timestepping')
rects2 = ax.bar(x - 2.0*width2, gal_lfric_solver_nodes24, width2, label='Solver')
rects3 = ax.bar(x - 1.0*width2, gal_lfric_rhs_nodes24, width2, label='RHS')
rects4 = ax.bar(x,              gal_lfric_advection_nodes24, width2, label='Advection')
rects5 = ax.bar(x + 1.0*width2, gal_lfric_slow_nodes24, width2, label='Slow Physics')
rects6 = ax.bar(x + 2.0*width2, gal_lfric_fast_nodes24, width2, label='Fast Physics')
rects7 = ax.bar(x + 3.0*width2, gal_lfric_setup_nodes24, width2, label='Non timestepping')

ax.set_ylabel('Time (s)')
ax.set_title('GAL LFRic_atm Component cost, 24 nodes, 1 thread')
ax.set_xticks(x[:])
ax.set_xticklabels(labels[:])
ax.legend()

bx.plot(x,timestepspeedup24to96,'b',label='Timestepping speedup')
bx.plot(x,solverspeedup24to96,'tab:orange',label='Solver speedup')
bx.plot(x,rhsspeedup24to96,'g',label='RHS speedup')
bx.plot(x,advectionspeedup24to96,'r',label='Advection speedup')
bx.plot(x,slowspeedup24to96,'k',label='Slow Physics speedup')
bx.plot(x,fastspeedup24to96,'m',label='Fast physics speedup')
bx.plot(x,setupspeedup24to96,'c',label='Non timestepping speedup')

bx.set_xticks(x)
bx.set_xticklabels(labels)
bx.legend(bbox_to_anchor=(1.05, 1), loc='upper left',)

fig.tight_layout()
fig.autofmt_xdate(rotation=45)
plt.savefig('GAL-LFRic-component.png')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
# Plot the GAL LFRic to UM ratio cost
width2 = width * 3.0/6.0
fig, (ax) = plt.subplots(1,1,figsize=(15,7))
rects1 = ax.bar(x - 2.5*width2, um2lfric_total, width2, label='Total')
rects2 = ax.bar(x - 1.5*width2, um2lfric_solver, width2, label='Solver')
rects3 = ax.bar(x - 0.5*width2, um2lfric_transport, width2, label='Advection')
rects4 = ax.bar(x + 0.5*width2, um2lfric_slow, width2, label='Slow Physics')
rects5 = ax.bar(x + 1.5*width2, um2lfric_fast, width2, label='Fast Physics')
#rects6 = ax.bar(x + 2.5*width2, um2lfric_setup, width2, label='Non timestepping')

ax.set_ylabel('X times UM cost')
ax.set_title('GAL LFRic_atm to UM Component cost, 24 nodes, 1 thread')
ax.set_xticks(x[:])
ax.set_xticklabels(labels[:])
ax.legend()

fig.tight_layout()
fig.autofmt_xdate(rotation=45)
plt.savefig('GAL-LFRic2UM-component.png')
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

# Plot the cost for the proto_gal_lfric_atm job
#fig, ax = plt.subplots(1,1,figsize=(15,7))
fig, (ax, bx, cx) = plt.subplots(3,1,figsize=(15,7),gridspec_kw={'height_ratios': [3, 1, 1]})
rects1 = ax.bar(x[:]-width/2, proto_gal_lfric_nodes3[:], width, label='3 Nodes')
rects2 = ax.bar(x[:]+width/2, proto_gal_lfric_nodes6[:], width, label='6 Nodes')

ax.set_ylabel('Time (s)')
ax.set_title('Proto-GAL LFRic_atm model cost')
ax.set_xticks(x[:])
ax.set_xticklabels(labels[:])
fig.autofmt_xdate(rotation=45)
ax.legend()

bx.plot(x,speedup3to6,'b',label='Speedup 3 to 6 nodes')
bx.set_xticks(x)
bx.set_xticklabels(labels)
bx.legend()

cx.plot(x,sypd_nodes3,'b',label='SYPD - 3 nodes')
cx.plot(x,sypd_nodes6,'g',label='SYPD - 6 nodes')
cx.set_xticks(x)
cx.set_xticklabels(labels)
cx.legend()

plt.savefig('Proto-GAL-LFRic.png')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
# Plot the GAL LFRic component cost
width2 = width * 1.0/4.0
fig, (ax, bx) = plt.subplots(2,1,figsize=(15,7),gridspec_kw={'height_ratios': [3, 1]})
rects1 = ax.bar(x - 3*width2, proto_gal_lfric_solver_nodes6, width2, label='Solver')
rects2 = ax.bar(x - 2*width2, proto_gal_lfric_rhs_nodes6, width2, label='RHS')
rects3 = ax.bar(x - 1*width2, proto_gal_lfric_advection_nodes6, width2, label='Advection')
rects4 = ax.bar(x,            proto_gal_lfric_slow_nodes6, width2, label='Slow Physics')
rects5 = ax.bar(x + 1*width2, proto_gal_lfric_fast_nodes6, width2, label='Fast Physics')
rects6 = ax.bar(x + 2*width2, proto_gal_lfric_ukca_nodes6, width2, label='UKCA')
rects7 = ax.bar(x + 3*width2, proto_gal_lfric_setup_nodes6, width2, label='Non timestepping')

ax.set_ylabel('Time (s)')
ax.set_title('Proto-GAL LFRic_atm Component cost, 6 nodes, 1 thread')
ax.set_xticks(x[:])
ax.set_xticklabels(labels[:])
ax.legend()

bx.plot(x,solverspeedup3to6,'b',label='Solver speedup')
bx.plot(x,rhsspeedup3to6,'g',label='RHS speedup')
bx.plot(x,advectionspeedup3to6,'r',label='Advection speedup')
bx.plot(x,slowspeedup3to6,'k',label='Slow Physics speedup')
bx.plot(x,fastspeedup3to6,'m',label='Fast physics speedup')
bx.plot(x,ukcaspeedup3to6,'y',label='UKCA physics speedup')
bx.plot(x,setupspeedup3to6,'c',label='Non timestepping speedup')

bx.set_xticks(x)
bx.set_xticklabels(labels)
bx.legend(bbox_to_anchor=(1.05, 1), loc='upper left',)

fig.tight_layout()
fig.autofmt_xdate(rotation=45)
plt.savefig('Proto-GAL-LFRic-component.png')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

plt.show()
