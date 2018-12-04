# -*- coding : utf-8 -*-

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import random
from math import cos

N = 100

#pojavljauca 5 cisel randomnie ot 0 do 1
x = random.uniform(0, 5, N)

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import cos, linspace
x = linspace(0, 4, 11)
y = cos(x) * cos(x)
from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $(cos(x)*cos(x))$')
plt.plot(x, y)
plt.legend("$cos(x)$")
plt.show()

y = random.uniform(0, 5, N)
N1 = 0
from matplotlib import pyplot as plt
plt.grid()
for i in range(N):
    print(x[i], y[i])
    if x[i] > 2 and y[i] < 1:
        if y[i] < 1 and x[i] > y[i]:
            plt.plot(x[i], y[i], 'go')
            N1 = N1 + 1
        else:
            plt.plot(x[i], y[i], 'ro')
plt.show()
