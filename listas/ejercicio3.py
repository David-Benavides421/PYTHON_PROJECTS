# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un
# alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas,
# la nota media, la nota más alta que ha sacado y la menor.

notas = []
for indice in range(1,6): # Para 5 notas
    while True:
        nota = int(input("Introduce la nota %d: " % indice))
        if nota>=0 and nota<=10:
            break
        # else: (implícito)
        #     print("Nota fuera de rango , inténtalo de nuevo.") # Opcional, para mejor UX
    notas.append(nota)

if notas: # Para evitar errores si la lista está vacía (aunque el bucle asegura 5 notas)
    print("Nota media: ",sum(notas)/len(notas))
    print("Nota max: ",max(notas))
    print("Nota min: ",min(notas))
else:
    print("No se introdujeron notas.")