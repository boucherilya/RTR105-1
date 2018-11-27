# -*- coding : utf-8 -*-

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import random
from math import cos

N = 100

#pojavljauca 5 cisel randomnie ot 0 do 1
x = random.uniform(0,5,N)

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import cos, linspace
x = linspace(0,4,11)
y = cos(x) * cos(x)
from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $(cos(x)*cos(x))$')
plt.plot(x,y,)
plt.legend("$cos(x)$")
plt.show()


y = (cos(x))**2
print ("(cos(x))**2(%.2f) = %.2f"%(x,y))

a0 = (-1)**1*x**0*2**(-1)/(1)
S0 = a0
print ("a0 = %.2f SO = %.2f"%(a0,S0))

a1 = (-1)**2*x**2*2/(1*2)
S1 = a0 + a1
print ("a1 = %.2f S1 = %.2f"%(a1,S1))

a2  = (-1)**3*x**4*2**3/(1*2*3*4)
S2 = a0 + a1 + a2
print ("a2 = %.2f S2 = %.2f"%(a2,S2))

a3  = (-1)**4*x**6*2**5/(1*2*3*4*5*6)
S3 = a0 + a1 + a2 + a3
print ("a3 = %.2f S3 = %.2f"%(a3,S3))

y = random.uniform(0,5,N)
N1=0
from matplotlib import pyplot as plt
plt.grid()
for i in range(N):
    if x[i]>0 and x[i]<5:
        if y[i]>0 and y[i]< x[i]:
            plt.plot(x[i],y[i],'go')
            N1 = N1 + 1
        else:
            plt.plot(x[i],y[i],'ro')
plt.show()
