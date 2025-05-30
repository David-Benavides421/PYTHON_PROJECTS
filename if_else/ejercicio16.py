# La política de cobro de una compañía telefónica es: cuando se realiza una
# llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros
# cinco minutos cuestan 1 peso, los siguientes tres, 80 centavos,
# los siguientes dos minutos, 70 centavos, y a partir del décimo minuto, 50 centavos.
# Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
# de mañana, 15 %, y en turno de tarde, 10 %.
# Realice un algoritmo para determinar cuánto debe pagar por cada concepto
# una persona que realiza una llamada.

tiempo = int(input("¿Cuánto tiempo es la llamada?:"))
es_domingo = input("¿Es Domingo? (S/N):")
if es_domingo.upper() == "N":
    turno = input("¿Qué turno: Mañana o Tarde? (M/T)?:")
if tiempo<5:
    costo = tiempo*100
else:
    if tiempo<8:
        costo = (tiempo-5)*80+500
    else:
        if tiempo<10:
            costo = (tiempo-8)*70+240+500
        else:
            costo = (tiempo-10)*50+140+240+500
if es_domingo.upper() == "S":
    costo = costo+costo*0.03
else:
    if turno.upper() == "M":
        costo = costo+costo*0.15
    else:
        costo = costo+costo*0.10

print("El costo de la llamada: %.2f pesos." % (costo/100))