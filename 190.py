# Fails : 190. py
# Autors : Iļja Dočuks
# Apliecibas numurs : 181REB294
# Datums : 01.01.2019

# -*- coding : utf -8 -*-
from math import cos , fabs
from time import sleep

def f(x):
    return cos(x) * cos(x)

# Defineejam precizitaati , ar kaadu mekleesim sakni :
h = 0.01
# Sakuma X :
xnull = -2
# Merka X :
xtarg = 2
# Tekosais X :
xcur = xnul
# Atvasinajuma vertiba
xar = 0

# Apsatrades cikls :
while ( xcur <= xtarg ):
    xar = (f(xcur + h) - f(xcur))/h
    print (xcur)
    print (f(xcur))
    print (xar)
    xcur += h
