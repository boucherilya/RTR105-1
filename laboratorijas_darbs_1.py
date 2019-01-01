# -*- coding: utf-8 -*-
from math import cos

#(1.) * (2.) = (2.) - float * int = float
#(1.) * (2.) = (2.) - float * float = float#float(input()) -> float
x = float( input("Lietotāj, lūdzu, ievadi argumentu (x): "))
#print type(x)
print ("x = %.f cos(x)*cos(x) = %.2f"%(x,cos(x)))

print(" 500")
print("------")
print("\\              k+1  2k  2k-1")
print(" \\          (-1)   *x  *2")
print("    cos(2) => |-------------------")
print(" /           (2*k)!")
print("/")
print("------")
print(" k=1")

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

x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = cos(x)*cos(x)

print("cos(%.2f) = %.2f"%(x,y))
a0 = (-1)**1*x**0*2**(-1)/(1)
S = a0
print("a0 = %.2f S0 = %.2f"%(a0,S0))

S = S + a1
print("a1 = %.2f S1 = %.2f"%(a1,S))

a2 = (-1)**3*x**4*2**3/(1*2*3*4)
S = S + a2
print("a2 = %.2f S2 = %.2f"%(a2,S))

a3 = (-1)**4*x**6*2**5/(1*2*3*4*5*6)
S3 = S + a3
print("a3 = %.2f S3 = %.2f"%(a3,S))
