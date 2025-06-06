# crea un programa que pida un numero al usuario un numero del mes
# por ejemploel 4 y diga cuantos dias tiene 
# el nombre del mes. debe usar listas para simplificarlos vamos 
# a suponer que febrero tiene 28 dias 

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

nombre_mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

while True:
    mes = int(input("Introduce el número del mes (1-12): "))
    if mes < 1 or mes > 12:
        print ("Error: mes incorrecto")
    if mes >=1 and mes <= 12: break
print("El mes de", nombre_mes[mes-1], "tiene", dias[mes-1], "días.")