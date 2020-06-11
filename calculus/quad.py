bash-3.2$ ls -lrt
total 16
-rwxr-xr-x  1 cmaynard  staff  1349  9 Nov 12:02 scale.py
-rw-r--r--  1 cmaynard  staff   152  9 Nov 12:17 linear.py
bash-3.2$ chmod 755 linear.py 
bash-3.2$ ./linear.py 
Traceback (most recent call last):
  File "./linear.py", line 9, in <module>
    x=np.array(0.0,2.0)
TypeError: data type not understood
bash-3.2$ TypeError: data type not understood
bash-3.2$ 
bash: TypeError:: command not found
bash-3.2$ bash: bash-3.2$: command not found
bash-3.2$ ./linear.py 
[0. 2.]
bash-3.2$ ./linear.py 
Traceback (most recent call last):
  File "./linear.py", line 13, in <module>
    ax.plot(x, y, 'r')
NameError: name 'ax' is not defined
bash-3.2$ ./linear.py 
Traceback (most recent call last):
  File "./linear.py", line 13, in <module>
    ax.plot(x, y, 'r')
NameError: name 'ax' is not defined
bash-3.2$ ./linear.py 
bash-3.2$ ./linear.py 
bash-3.2$ ./linear.py 
bash-3.2$ ./linear.py 
bash-3.2$ ./linear.py 
bash-3.2$ ./linear.py 
bash-3.2$ ./linear.py 
bash-3.2$ ls -lrt 
total 56
-rwxr-xr-x  1 cmaynard  staff   1349  9 Nov 12:02 scale.py
-rwxr-xr-x  1 cmaynard  staff    329  9 Nov 12:33 linear.py
-rw-r--r--  1 cmaynard  staff  19841  9 Nov 12:33 linear.png
bash-3.2$ chmod 755 quad.py 
bash-3.2$ ./quad.py 
./quad.py: line 1: bash-3.2$: command not found
./quad.py: line 2: total: command not found
./quad.py: line 3: -rwxr-xr-x: command not found
./quad.py: line 4: -rw-r--r--: command not found
./quad.py: line 5: bash-3.2$: command not found
./quad.py: line 6: bash-3.2$: command not found
./quad.py: line 7: syntax error near unexpected token `most'
./quad.py: line 7: `Traceback (most recent call last):'
bash-3.2$ ls -lrt
total 64
-rwxr-xr-x  1 cmaynard  staff   1349  9 Nov 12:02 scale.py
-rw-r--r--@ 1 cmaynard  staff  19841  9 Nov 12:33 linear.png
-rwxr-xr-x@ 1 cmaynard  staff   1203  9 Nov 12:36 quad.py
-rwxr-xr-x  1 cmaynard  staff    352  9 Nov 12:37 linear.py
bash-3.2$ more quad.py 
bash-3.2$ ls -lrt
total 16
-rwxr-xr-x  1 cmaynard  staff  1349  9 Nov 12:02 scale.py
-rw-r--r--  1 cmaynard  staff   152  9 Nov 12:17 linear.py
bash-3.2$ chmod 755 linear.py 
bash-3.2$ ./linear.py 
Traceback (most recent call last):
  File "./linear.py", line 9, in <module>
    x=np.array(0.0,2.0)
TypeError: data type not understood
bash-3.2$ TypeError: data type not understood
bash-3.2$ 
bash: TypeError:: command not found
bash-3.2$ bash: bash-3.2$: command not found
bash-3.2$ ./linear.py 
[0. 2.]
bash-3.2$ ./linear.py 
Traceback (most recent call last):
  File "./linear.py", line 13, in <module>
    ax.plot(x, y, 'r')
quad.py 
NameError: name 'ax' is not defined
bash-3.2$ ./linear.py 
Traceback (most recent call last):
  File "./linear.py", line 13, in <module>
    ax.plot(x, y, 'r')
NameError: name 'ax' is not defined
bash-3.2$ ./linear.py 
bash-3.2$ ./linear.py 
bash-3.2$ ./linear.py 
bash-3.2$ ./linear.py 
bash-3.2$ ./linear.py 
bash-3.2$ ./linear.py 
bash-3.2$ ./linear.py 
bash-3.2$ ls -lrt 
total 56
-rwxr-xr-x  1 cmaynard  staff   1349  9 Nov 12:02 scale.py
-rwxr-xr-x  1 cmaynard  staff    329  9 Nov 12:33 linear.py
-rw-r--r--  1 cmaynard  staff  19841  9 Nov 12:33 linear.png
bash-3.2$ 
bash-3.2$ ls -lrt
total 64
-rwxr-xr-x  1 cmaynard  staff   1349  9 Nov 12:02 scale.py
-rw-r--r--@ 1 cmaynard  staff  19841  9 Nov 12:33 linear.png
-rwxr-xr-x@ 1 cmaynard  staff   1203  9 Nov 12:36 quad.py
-rwxr-xr-x  1 cmaynard  staff    352  9 Nov 12:37 linear.py
bash-3.2$ more quad.py 
bash-3.2$ ls -lrt
total 16
-rwxr-xr-x  1 cmaynard  staff  1349  9 Nov 12:02 scale.py
-rw-r--r--  1 cmaynard  staff   152  9 Nov 12:17 linear.py
bash-3.2$ chmod 755 linear.py 
bash-3.2$ ./linear.py 
Traceback (most recent call last):
  File "./linear.py", line 9, in <module>
    x=np.array(0.0,2.0)
TypeError: data type not understood
bash-3.2$ TypeError: data type not understood
bash-3.2$ 
bash: TypeError:: command not found
bash-3.2$ bash: bash-3.2$: command not found
bash-3.2$ ./linear.py 
[0. 2.]
bash-3.2$ ./linear.py 
Traceback (most recent call last):
  File "./linear.py", line 13, in <module>
    ax.plot(x, y, 'r')
quad.py
NameError: name 'ax' is not defined
:
bash-3.2$ ./linear.py 
:
Traceback (most recent call last):
:
  File "./linear.py", line 13, in <module>
:q
bash-3.2$ bash-3.2$ more quad.py 
#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import sys

x=np.array(range(-2.0,2.0,100))
print x
#y=np.array([-0.5,1.5])

#fig,ax = plt.subplots()
#l1=ax.plot(x, y, 'r')
#plt.axhline(0, color='black')
#plt.axvline(0, color='black')

#plt.savefig("linear.png",format="png")
#plt.show()
quad.py (END)q
bash-3.2$ bash-3.2$ ./quad.py 
Traceback (most recent call last):
  File "./quad.py", line 9, in <module>
    x=np.array(range(-2.0,2.0,100))
TypeError: range() integer end argument expected, got float.
bash-3.2$ ./quad.py 
[-2]
bash-3.2$ ./quad.py 
  File "./quad.py", line 11
    for i in range(101)
                      ^
SyntaxError: invalid syntax
bash-3.2$ SyntaxError: invalid syntax
bash-3.2$ 
bash: SyntaxError:: command not found
bash-3.2$ bash: bash-3.2$: command not found
bash-3.2$ ./quad.py 
Traceback (most recent call last):
  File "./quad.py", line 8, in <module>
    x=np.array()
TypeError: Required argument 'object' (pos 1) not found
bash-3.2$ ./quad.py 
Traceback (most recent call last):
  File "./quad.py", line 12, in <module>
    x.add(xval)
AttributeError: 'numpy.ndarray' object has no attribute 'add'
bash-3.2$ ./quad.py 
[-2.         -1.95959596 -1.91919192 -1.87878788 -1.83838384 -1.7979798
 -1.75757576 -1.71717172 -1.67676768 -1.63636364 -1.5959596  -1.55555556
 -1.51515152 -1.47474747 -1.43434343 -1.39393939 -1.35353535 -1.31313131
 -1.27272727 -1.23232323 -1.19191919 -1.15151515 -1.11111111 -1.07070707
 -1.03030303 -0.98989899 -0.94949495 -0.90909091 -0.86868687 -0.82828283
 -0.78787879 -0.74747475 -0.70707071 -0.66666667 -0.62626263 -0.58585859
 -0.54545455 -0.50505051 -0.46464646 -0.42424242 -0.38383838 -0.34343434
 -0.3030303  -0.26262626 -0.22222222 -0.18181818 -0.14141414 -0.1010101
 -0.06060606 -0.02020202  0.02020202  0.06060606  0.1010101   0.14141414
  0.18181818  0.22222222  0.26262626  0.3030303   0.34343434  0.38383838
  0.42424242  0.46464646  0.50505051  0.54545455  0.58585859  0.62626263
  0.66666667  0.70707071  0.74747475  0.78787879  0.82828283  0.86868687
  0.90909091  0.94949495  0.98989899  1.03030303  1.07070707  1.11111111
  1.15151515  1.19191919  1.23232323  1.27272727  1.31313131  1.35353535
  1.39393939  1.43434343  1.47474747  1.51515152  1.55555556  1.5959596
  1.63636364  1.67676768  1.71717172  1.75757576  1.7979798   1.83838384
  1.87878788  1.91919192  1.95959596  2.        ]
bash-3.2$ ./quad.py 
[ 3.          2.84001632  2.68329762  2.52984389  2.37965514  2.23273135
  2.08907254  1.94867871  1.81154984  1.67768595  1.54708703  1.41975309
  1.29568411  1.17488011  1.05734109  0.94306703  0.83205795  0.72431385
  0.61983471  0.51862055  0.42067136  0.32598714  0.2345679   0.14641363
  0.06152433 -0.02009999 -0.09845934 -0.17355372 -0.24538312 -0.31394756
 -0.37924702 -0.4412815  -0.50005102 -0.55555556 -0.60779512 -0.65676972
 -0.70247934 -0.74492399 -0.78410366 -0.82001837 -0.8526681  -0.88205285
 -0.90817264 -0.93102745 -0.95061728 -0.96694215 -0.98000204 -0.98979696
 -0.99632691 -0.99959188 -0.99959188 -0.99632691 -0.98979696 -0.98000204
 -0.96694215 -0.95061728 -0.93102745 -0.90817264 -0.88205285 -0.8526681
 -0.82001837 -0.78410366 -0.74492399 -0.70247934 -0.65676972 -0.60779512
 -0.55555556 -0.50005102 -0.4412815  -0.37924702 -0.31394756 -0.24538312
 -0.17355372 -0.09845934 -0.02009999  0.06152433  0.14641363  0.2345679
  0.32598714  0.42067136  0.51862055  0.61983471  0.72431385  0.83205795
  0.94306703  1.05734109  1.17488011  1.29568411  1.41975309  1.54708703
  1.67768595  1.81154984  1.94867871  2.08907254  2.23273135  2.37965514
  2.52984389  2.68329762  2.84001632  3.        ]
bash-3.2$ ./quad.py 
[ 3.          2.84001632  2.68329762  2.52984389  2.37965514  2.23273135
  2.08907254  1.94867871  1.81154984  1.67768595  1.54708703  1.41975309
  1.29568411  1.17488011  1.05734109  0.94306703  0.83205795  0.72431385
  0.61983471  0.51862055  0.42067136  0.32598714  0.2345679   0.14641363
  0.06152433 -0.02009999 -0.09845934 -0.17355372 -0.24538312 -0.31394756
 -0.37924702 -0.4412815  -0.50005102 -0.55555556 -0.60779512 -0.65676972
 -0.70247934 -0.74492399 -0.78410366 -0.82001837 -0.8526681  -0.88205285
 -0.90817264 -0.93102745 -0.95061728 -0.96694215 -0.98000204 -0.98979696
 -0.99632691 -0.99959188 -0.99959188 -0.99632691 -0.98979696 -0.98000204
 -0.96694215 -0.95061728 -0.93102745 -0.90817264 -0.88205285 -0.8526681
 -0.82001837 -0.78410366 -0.74492399 -0.70247934 -0.65676972 -0.60779512
 -0.55555556 -0.50005102 -0.4412815  -0.37924702 -0.31394756 -0.24538312
 -0.17355372 -0.09845934 -0.02009999  0.06152433  0.14641363  0.2345679
  0.32598714  0.42067136  0.51862055  0.61983471  0.72431385  0.83205795
  0.94306703  1.05734109  1.17488011  1.29568411  1.41975309  1.54708703
  1.67768595  1.81154984  1.94867871  2.08907254  2.23273135  2.37965514
  2.52984389  2.68329762  2.84001632  3.        ]
bash-3.2$ ./quad.py 
bash-3.2$ ./quad.py 
Traceback (most recent call last):
  File "./quad.py", line 13, in <module>
    y2=x1*x1-1.0  
NameError: name 'x1' is not defined
bash-3.2$ ./quad.py 
Traceback (most recent call last):
  File "./quad.py", line 16, in <module>
    l2=ax.plot(x1,y2,'b')
NameError: name 'x1' is not defined
bash-3.2$ ./quad.py 
bash-3.2$ ./quad.py 
bash-3.2$ ./quad.py 
bash-3.2$ ./quad.py 
bash-3.2$ ./quad.py 
bash-3.2$ ./quad.py 
bash-3.2$ ./quad.py 
bash-3.2$ ./quad.py 
bash-3.2$ ls -lrt
total 232
-rwxr-xr-x  1 cmaynard  staff   1349  9 Nov 12:02 scale.py
-rw-r--r--@ 1 cmaynard  staff  19841  9 Nov 12:33 linear.png
-rwxr-xr-x  1 cmaynard  staff    328  9 Nov 12:39 linear.py
-rw-r--r--  1 cmaynard  staff  20685  9 Nov 12:55 Q1.png
-rw-r--r--  1 cmaynard  staff  28830  9 Nov 12:56 Q2.png
-rwxr-xr-x@ 1 cmaynard  staff    396  9 Nov 12:57 quad.py
-rw-r--r--  1 cmaynard  staff  24582  9 Nov 12:57 Q3.png
bash-3.2$ ./quad.py 
bash-3.2$ 