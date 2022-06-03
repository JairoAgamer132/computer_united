import random
j = int(input(" ingrese las columnas:_ "))
a = int(input(" ingrese las filas:_ "))
m = []

for i in range(j):
    ma = []
    for i in range(a):
        li = random.randint(0,10)
        ma.append(li)
    m.append(ma)
    
for o in m:
    print(o)
       
from collections import Counter

l = o
c = Counter(l)
print("El numero que mas se repitio fue")
print(max(c, key=c.get))
