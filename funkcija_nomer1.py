# -*- coding: utf-8 -*-
from math import cos

#(1.) * (2.) = (2.) - float * int = float
#(1.) * (2.) = (2.) - float * float = float#float(input()) -> float
x = 1. * input("Lietotāj, lūdzu, ievadi argumentu (x): ")
#print type(x)

y = (cos(x))**2
print "(cos(x))**2(%.2f) = %.2f"%(x,y)

a0 = (-1)**1*x**0*2**(-1)/(1)
S0 = a0
print "a0 = %.2f SO = %.2f"%(a0,S0)

a1 = (-1)**2*x**2*2/(1*2)
S1 = a0 + a1
print "a1 = %.2f S1 = %.2f"%(a1,S1)

a2  = (-1)**3*x**4*2**3/(1*2*3*4)
S2 = a0 + a1 + a2
print "a2 = %.2f S2 = %.2f"%(a2,S2)

a3  = (-1)**4*x**6*2**5/(1*2*3*4*5*6)
S3 = a0 + a1 + a2 + a3
print "a3 = %.2f S3 = %.2f"%(a3,S3)
