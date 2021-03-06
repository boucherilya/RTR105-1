#4.labaratorijas darbs
#Ielādējam savu repozitāriju terminālā un islēdzam  idle & vidi kur sākam veidot funkciju #
import sys
sys.path.append("user/local/anaconda3/lib/python3.6/site-packages")

#sys importē iebūvēto moduli (bibliotēku), kas nosaukts sys.

from numpy import random, cos
#from math import sqrt
#from math import cos

#importē izlases moduli no Python standarta bibliotēkas.

N = 7000
N1 = 0

#Pieškiram vienību skaitu cik punktu būs attēlot funkcijā (7000)

x = random.uniform(0,5,N)
y = random.uniform(0,5,N)

#Noskām grafika iedalijuma punktus pa x asi 5 iedalijumi pa y asi 80 

funct = cos(x)*cos(x)
#Norādam kāda funkcija būs attēlota 

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)*cos(x)$ ')
plt.plot(x, funct, 'o', color = "#990000")
for i in range(N):
#Pievienojam krāsas punktiem zaļo un sarkano kas sadalīs grafika 2 daļās
    
    #plt.plot(x[i],y[i],"ko")
    if x[i] > 0 and x[i] < 5:
        if y[i] > 0 and y[i] < funct[i]:
            plt.plot(x[i],y[i],"go")
            N1 = N1 + 1
        else:
            plt.plot(x[i],y[i],"ro")
#Grafika punkti kas atrodas zem tā ir iekrasoti zaļā krāsā, bet virs grafika sarkanā lidz ar to mēs to pieprasām un galu galā saņemam iekrāsotu taisnstūri
plt.show()

s_zinh = 5 * 5
s_nez = 1. * s_zin * N1/N
print(s_cos)
print(s_nez)

#Ierakstām kurā momentā punktiem ir jāizmaina krāsa lai sanāktu krāsu dalijums pēc grafika līknes
