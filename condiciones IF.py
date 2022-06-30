from __future__ import print_function
from operator import truediv
from re import T


a = 1
b = 1

if a < b:
    print("A es menor que b")
elif a == b:
    print("A es igual a B")
else:
    print("A es mayor que B")

c = True

if c:
    print("C es verdadero")
else:
    print("C es falso")

if type(c) is bool:
    print("A es booleano")
else:
    print("A es otro tiopo de dato")

d = 10
e = 5
f = 1

if d>e and e>f:
    print("Las condiciones son verdaderas")

if d>e or e>f:
    print("Las condiciones son verdaderas")