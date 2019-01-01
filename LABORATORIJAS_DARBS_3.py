# Fails : 191. py
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
xcur = xnull
# Atvasinajuma vertiba
xar = 0
xar2 = 0

datu_fails = open("91.dat", "w") #Tiek izveidots fails ar tiesībām tajā rakstīt

# Apsatrades cikls :
while ( xcur <= xtarg ):
    xar = (f(xcur + h) - f(xcur))/h
    datu_fails.write("(");
    datu_fails.write(str(xcur) + " ") #Failā tiek veikts ieraksts
    datu_fails.write(str(f(xcur)) + " ")
    datu_fails.write(str(xar)+ ")\n")
    datu_fails.write(str(xar)+ ")\n")
    xcur += h

datu_fails.close() #Fails tiek aizvērts ciet !!!
