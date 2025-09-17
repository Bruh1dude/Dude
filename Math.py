import math
from math import sin

print("Kalkulacka na povrcha a obsah gule")

a = int(input("Zadaj polomer"))

c = (a*a)*(3.14*4)

d = (4/3*3.14) * (a*a*a)
print("Povrch")
print(c)
print("Objem")
print(d)