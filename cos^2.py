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

