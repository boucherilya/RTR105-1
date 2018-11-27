import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import cos, linspace
x = linspace(0,10,1)
y = x
from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $(x)$')
plt.plot(x, y)
plt.legend("$(x)$")
plt.show()
