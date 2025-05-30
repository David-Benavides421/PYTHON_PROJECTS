import math

x1 = float(input("Dime cordenadas x primera circunferencia: "))
y1 = float(input("Dime cordenadas y primera circunferencia: "))
r1 = float(input("Dime el radio de la primera circunferencia: "))
x2 = float(input("Dime cordenadas x segunda circunferencia: "))
y2 = float(input("Dime cordenadas y segunda circunferencia: "))
r2 = float(input("Dime el radio de la segunda circunferencia: "))
# Distancia entre los centros de las circunferencias    
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# Si la distancia entre los centros es menor que la suma de los radios, las circunferencias se intersectan
if d < r1 + r2:
    print("Las circunferencias se intersectan")
elif d == r1 + r2:
    print("Las circunferencias son tangentes")
# Si la distancia entre los centros es mayor que la suma de los radios, las circunferencias no se intersectan
elif d >(r1 + r2) and d > abs(r1 - r2):
    print("Las circunferencias secantes")
# Si la distancia entre los centros es igual a la suma de los radios, las circunferencias son tangentes
if d == abs(r1 - r2):
    print("Las circunferencias tangentes interiores")
# Si la distancia entre los centros es menor que la diferencia de los radios, una circunferencia está dentro de la otra
if d < 0 and d < abs(r1 - r2):
    print("Circuferencias interiores")

if d == 0:
    print("Circunferencia concetricas")