# El director de una escuela está organizando un viaje de estudios, y requiere
# determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de
# viajes por el servicio. La forma de cobrar es la siguiente:
# si son 100 alumnos o más, el costo por cada alumno es de 65000 pesos;
# de 50 a 99 alumnos, el costo es de 70000 pesos, de 30 a 49, de 95000 pesos,
# y si son menos de 30, el costo de la renta del autobús es de 400000 pesos,
# sin importar el número de alumnos.
# Realice un algoritmo que permita determinar el pago a la compañía de autobuses
# y lo que debe pagar cada alumno por el viaje.

num_alumnos = int(input("¿Cuántos alumnos participan en la actividad?:"))

if num_alumnos>=100:
    costo_por_alumno = 65000
if num_alumnos>=50 and num_alumnos<=99:
    costo_por_alumno = 70000
if num_alumnos>=30 and num_alumnos<=49:
    costo_por_alumno = 95000
if num_alumnos<30 and num_alumnos>0:
    costo_por_alumno = 400000/num_alumnos
if num_alumnos>0:
    costo_autobus = num_alumnos*costo_por_alumno
    print("El costo por alumno es ",costo_por_alumno,"pesos.")
    print("El costo del autobús es ",costo_autobus,"pesos.")
else:
    print("El número de alumnos debe ser un valor positivo.")