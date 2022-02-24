from math import *
def vZF(x):
    return -a**3+5*a**2 #vereinfachte Zielfunktion
randMin = 0 #Minimum Rand
randMax = 5 #Maximum Rand
l = []
x = randMin
while x <= randMax :
    l.append(x)
    x += 0.1 #Genauigkeit
v = []
for a in l:
    v.append(vZF(a))
print("Max x-Stelle:", l[v.index(max(v))])
print("Maximalwert:", max(v))
print("Min x-Stelle:", l[v.index(min(v))])
print("Minimalwert:", min(v))
