# Fails : 171. py
# Autors : Iļja Dočuks
# Apliecibas numurs : 181REB294
# Datums : 01.01.2019
# Sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi

# -*- coding : utf -8 -*-
from math import cos , fabs
from time import sleep

def f(x):
    return cos(x) * cos(x) -0.5

# Definejam argumenta x robezhas :
a = 0
b = 1.5

# Definejam mainigo iteraciju skaita noteiksanai:
count = 0

# Aprekjinam funkcijas vertibas dotajos punktos :
funa = f(a)
funb = f(b)

# Paarbaudam , vai dotajaa intervaalaa ir saknes :
if ( funa * funb > 0.0 ):
    print ("Dotajaa intervaalaa [%s, %s] saknju nav"%(a,b))
    sleep(1); exit() # Zinjo uz ekraana , gaida 1 sec . un darbu pabeidz

# Defineejam precizitaati , ar kaadu mekleesim sakni :
deltax = 0.0001

# Sashaurinam saknes mekleeshanas robezhas :
while ( fabs(b-a) > deltax ):
    count += 1
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0. ):
        b = x
    else:
        a = x

print ("x=", x)
print ("cos(x)*cos(x)-0.5=", f(x))
print ("Nepieciesamu iteraciju skaits ir", count)


