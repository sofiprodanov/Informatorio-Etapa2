#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
#pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe
#mostrar por pantalla las asignaturas que el usuario tiene que repetir.

materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
#BLOQUE 1: EVALUA MATERIAS APROBADAS
aprobadas = []
for materia in materias:
    nota = float(input(f"¿Que nota sacaste en {materia}? "))
    if nota > 5:
        aprobadas.append(materia) #va materia entre () porque debe eliminar las materias aprobadas.
#BLOQUE 2: ELIMINA MATERIAS APROBADAS QUEDANDO LAS QUE DEBE RENDIR
for materia in aprobadas: #para la materia que se encuentren en la lista de aprobadas, va a eliminar las de la lista materias
    materias.remove(materia)
print(f"Tienes que repetir {materias}")

