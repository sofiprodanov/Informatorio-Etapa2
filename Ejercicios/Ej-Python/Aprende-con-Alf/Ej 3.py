#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
#pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura>
#has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
for materia in materias:
    nota = input(f"¿Que nota sacaste en {materia}? ")
    notas.append(nota) #agregar cada nueva nota ingresada por el usuario al final de la lista scores.
for i in range(len(materias)):
    print(f"En {materias[i]} has sacado {notas[i]}")

#1. range(len(materias))
#Calcula la longitud (número de elementos) de la lista materias. Esto permite iterar sobre los índices de la lista (no directamente sobre los elementos).

#2. for i in ...
#En cada iteración, i toma un valor de la secuencia (0, luego 1, luego 2). i actúa como el índice para acceder a las posiciones de ambas listas (materias y notas).

#3. print(f"En {materias[i]} has sacado {notas[i]}")
#materias[i]: Accede a la asignatura en la posición i. notas[i]: Accede a la nota correspondiente en la misma posición i.