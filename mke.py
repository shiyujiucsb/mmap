#!/bin/python

import math as m
import random as r
k=5.0
q=50*(2**k)
g=20.0
h=int(m.sqrt(q))
z = float(r.randint(1,q-1))
p_zt = float(h*(z**k)/g)
y = (1+r.randint(1,2)*g)/z

print "y = ", y

u = []
b = []
x = []
V = []
v = []
for i in range(int(k)):
  u.append(r.randint(1,2))
  b.append(r.randint(1,2))
  x.append(b[-1]*g/z)

x_sum = 0
for i in range(int(k)):
  x_sum += x[i]*u[i]

for i in range(int(k)+1):
  v.append(r.randint(1,2))
  V.append(v[-1]*y+x_sum)

R = []
V_prod = 1
for i in range(int(k)+1):
  V_prod *= V[i]
for i in range(int(k)+1):
  R.append((int(V_prod/V[i]*v[i]*p_zt)%q)%g)

print "z = ", z
print "b[] = ", b
print "x[] = ", x
print "u[] = ", u
print "v[] = ", v
print "V[] = ", V
print R

